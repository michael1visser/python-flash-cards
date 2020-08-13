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
    deck_count = Cards.select().count()
