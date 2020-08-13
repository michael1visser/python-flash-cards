from peewee import *

db = PostgresqlDatabase('flashcards', user="postgres", password='', host='localhost', port=5432)
db.connect()

class BaseModel(Model):
        class Meta:
            database = db

class Cards(BaseModel):
    spanish = CharField()
    english = CharField()

round = 0



def game_setup():
    global round
    user_count = input(f"How many cards would you like to play with?\n")
    round += 1
    game_deck = Cards.select().order_by(fn.Random()).limit(user_count)

    for i in range(0, len(game_deck)):
        game_deck[i]['correct'] = 0
        game_deck[i]['incorrect'] = 0
    

game_setup()
