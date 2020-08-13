from peewee import *
from cards import cards
cardset = cards


db = PostgresqlDatabase('flashcards', user="postgres", password='', host='localhost', port=5432)

db.connect()

class BaseModel(Model):
        class Meta:
            database = db

class Cards(BaseModel):
    spanish = CharField()
    english = CharField()

db.drop_tables([Cards])
db.create_tables([Cards])

for i in range(0, len(cardset)):
    card = Cards(spanish=cardset[i]['spanish'], english=cardset[i]['english'])
    card.save()
    print(cardset[i]['spanish'])