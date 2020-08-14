# :woman_technologist: Spanish/English Flash Cards :technologist:

## Introduction

Spanish/English Flash Cards is a Python command line program in which users can cycle through a set of flash cards and guess the corresponding word for each card. Users can choose the number of cards they would like to play with and the game can be set so users can guess in English or Spanish. The game keeps track of the number of rounds played with the chosen deck and will alert the user when they guess incorrectly with the correct answer and how many times the user has guessed incorrectly. 

Users can also use the interface to add new cards, update existing cards, or delete cards from the database. 

## Technologies
* Python 3.
* PeeWee
* PostgresSQL

## Requirements
Flash Cards requires a terminal shell and the ability to create and read from a PostgresSQL database. 

## Installation

To install Flash Cards, download all repository files. 
Create a PostgresSQL database named "flashcards".
Run seed.py to seed the data from cards.py into the database in a table named cards.
Run flash_cards.py and follow the prompts in terminal.

## How to Use the Program

### To play the Flash Card Game
At the first prompt, enter "play".
Choose the number of cards you would like to play with. The system will choose randomly from the entire database.
Select whether you would like to enter guesses in English or Spanish.
At each card prompt, enter your guess and the system will alert you with a correct or incorrect message.
At the end of the round, enter "replay" to play again with the same deck, or "home" to return to the home screen.

### To manage the Flash Card database
At the first prompt, enter "manage".
Select the operation you would like to perform (create, edit, delete).
Follow the prompts to complete the operation. For edit and delete you will be asked to enter the Spanish word for the card you would like to update/delete.

### Contact Me

[Github](https://github.com/michael1visser)  
[Website](https://www.michaelpvisser.com)
