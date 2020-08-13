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


#START THE PROGRAM

def start_app(): 

    print("\n********************************************\n*Welcome to Spanish Vocabulary Flash Cards!*\n********************************************\n")

    while True:
        play_or_manage = input(f"Would you like to play a game or manage the cards?\nEnter 'play' to play a game or 'manage' to manage the cards: ")

        if play_or_manage in ['play', 'manage']:
            break
        else:
            print("\nInvalid entry, please try again.") 

    if play_or_manage == 'play':
        game_setup()
    elif play_or_manage == 'manage':
        choose_task()
        


# INITIALIZE GAME
def game_setup():        
    
    global round
    user_count = input("\nHow many cards would you like to play with?\n")

    while True:
        user_lang = input("Would you like to guess Spanish or English?\n").lower() 

        if user_lang in ['english', 'spanish']:
            break
        else:
            print("\nInvalid entry, please try again.")

    
    round += 1
    query = list(Cards.select().order_by(fn.Random()).limit(user_count))

    def create_card(val):
        card = {
            'spanish': val.spanish,
            'english': val.english,
            'correct': 0,
            'incorrect': 0
        }

        return card

    game_deck = list(map(create_card ,query))
    

    play_game(game_deck, user_lang)

#PLAY A ROUND OF THE GAME
def play_game(deck, lang):
    correct = 0
    incorrect = 0

    if lang == 'english':
        lang2 = 'spanish'
    else:
        lang2 = 'english'

    for i in range(0, len(deck)):
        guess = input(f"How do you say {deck[i][lang2]} in {lang.title()}?\n")

        if guess == deck[i][lang]:
            correct += 1
            deck[i]['correct'] += 1
            print("Correct!\n")
        else:
            incorrect += 1
            deck[i]['incorrect'] += 1
            print(
                f"Incorrect! The correct answer is {deck[i][lang]}.\nYou've missed this question {deck[i]['incorrect']} times this game.\n")

    end_round(correct, incorrect, deck, lang)  


#END THE ROUND AND CHOOSE TO PLAY AGAIN/RESET
def end_round(correct, incorrect, game_deck, lang):
    global round
    print(f"Game over! in round {round} you got {correct} correct and missed {incorrect}.\n")

    while True:
        end_choice = input("If you would like to play again with this deck, enter 'replay'.\n\
If you would like to return to the home screen, enter 'home.\n")

        if end_choice in ['replay', 'home']:
            break
        else:
            print("\nInvalid entry, please try again.")

    if end_choice == 'replay':
        round += 1
        game_deck = randomize_deck(game_deck)
        play_game(game_deck, lang)
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
    start_app()


#CRUD

#SET TASK TYPE
def choose_task():
    task= input("\nWhat would you like to do?\nTo create a new card, enter 'create'.\nTo edit an existing card, enter 'edit'.\nTo delete a card, enter 'delete'.\nTo return to the main screen, enter 'home'.\n")
    
    if task == 'create':
        create_card()
    elif task == 'edit':
        edit_card()
    elif task == 'delete':
        delete_card()
    elif task == 'home':
        start_app()
    else:
        print("Invalid entry, please try again. ")
        choose_task()

#CREATE A NEW CARD
def create_card():
    spanish = input(f"\nEnter the word in Spanish:\n")
    english = input(f"Enter the translation in English:\n")

    new_card = Cards(spanish=spanish, english=english)
    new_card.save()
    print(f"Success! the new card is id:{Cards.get(Cards.spanish == spanish)}\n")
    stay_or_go(choose_task)

#EDIT A CARD
def edit_card():
    to_be_edited = input("\nPlease input the Spanish word for the card to edit:\n")
    
    while True:
        s_or_e = input("Would you like to edit the Spanish or English?\n").lower()

        if s_or_e in ['spanish', 'english']:
            break
        else:
            print("\nInvalid entry, please try again.")

    new_value = input("Please enter the new word:\n")
    
    card = Cards.get(Cards.spanish == to_be_edited)
    if s_or_e == 'spanish':
        card.spanish = new_value
    elif s_or_e == 'english':
        card.english = new_value

    card.save()
    print(f"Success! card {card.id} has been updated with the new word {new_value} \n")
    stay_or_go(choose_task)

#DELETE A CARD
def delete_card():
    to_be_deleted = input("\nPlease input the spanish word for the card to delete:\n")

    card = Cards.get(Cards.spanish == to_be_deleted)
    card.delete_instance()
    print("Success, the card has been deleted.")
    stay_or_go(choose_task)

def stay_or_go(callback):
    
   
    while True:
        stay_go = input("Would you like to make another update to the cards? (y/n)\n")

        if stay_go in ['yes', 'y', 'no', 'n']:
            break
        else:
            print("\nInvalid entry, please try again.")

    if stay_go == 'y' or stay_go == 'yes':
        callback()
    elif stay_go == 'n' or stay_go == 'no':
        start_app()

start_app()
