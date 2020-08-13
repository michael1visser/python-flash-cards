from peewee import *
import random

db = PostgresqlDatabase('flashcards', user="postgres", password='', host='localhost', port=5432)
db.connect()

class BaseModel(Model):
        class Meta:
            database = db

class Cards(BaseModel):
    spanish = CharField()
    english = CharField()

round = 0

# INITIALIZE GAME
def game_setup():
    global round
    user_count = input(f"How many cards would you like to play with?\n")
    round += 1
    game_deck = Cards.select().order_by(fn.Random()).limit(user_count)

    for i in range(0, len(game_deck)):
        game_deck[i]['correct'] = 0
        game_deck[i]['incorrect'] = 0
    
    play_game(game_deck)

#PLAY A ROUND OF THE GAME
def play_game(deck):
    correct = 0
    incorrect = 0

    for i in range(0, len(deck)):
        guess = input(f"How do you say {deck[i]['english']} in Spanish?\n")

        if guess == deck[i]['spanish']:
            correct += 1
            deck[i]['correct'] += 1
            print("Correct!\n\n")
        else:
            incorrect += 1
            deck[i]['incorrect'] += 1
            print(
                f"Incorrect! The correct answer is {deck[i]['capital']}.\n")

        end_round(correct, incorrect)  

#END THE ROUND AND CHOOSE TO PLAY AGAIN/RESET
def end_round(correct, incorrect):
     global round
    print(f"Game over! You got {correct} correct and missed {incorrect}.\n")
    end_choice = input("If you would like to play again with this deck, enter 'replay'.\n\
If you would like to return to the home screent, enter 'home.\n")

    if end_choice == 'replay':
        round += 1
        game_deck = randomize_deck(game_deck)
        play_game(game_deck)
    elif end_choice == 'home':
        reset()

#RANDOMIZE THE EXISTING DECK
def randomize_deck(game_deck):
    random.shuffle(game_deck)
    return game_deck

#RESET APP
def reset():
    global round
    round = 0
    game_setup()


game_setup()
