FLASH CARDS

* GAME FLOW

1 user is asked whether they want to a) play or b) manage deck

a)  1. User is shown simple directions.
    2. User is asked how many cards they would like to play with 
    3. User is prompted to hit a key to begin.
    4. User sees Spanish word and inputs the english word.
        If the answer is incorrect, user is shown correct answer before next question is displayed.
    5. When the user has completed all the questions, they are asked whether to play again with the same deck or return to the main screen (reset).

b) 1. User is asked whether they would like to create, update, or delete a card.
    - If create user is prompted to input the Spanish and English words.
    - If update, user is asked which card and which language they would like to update. User inputs update.
    - If delete, user is asked which card to delete, and prompted to confirm.


* HIGH LEVEL FUNCTIONS

START GAME - 
    Function asking for input to play or manage. Conditional that either runs the play function or manage function based on user input. 

PLAY
    Game Setup Function - 
    First accepts user input to set X cards in play.(F)
    Randomize a list of the total number of cards (run a count against the db to get max), and select first X numbers from array.(F)
    Import cards with corresponding IDs and add to data set. 
    Add correct/incorrect attributes to each card.
    Run game play function
    (Choose which language to guess?)

    Game Play Function - 
    Select cards in order from the data set. 
    Present user with the Spanis word and ask to input the corresponding English word.
    If answer is correct, let user know. If answer is incorrect, include correct answer (Bold?). 
    Clear screen before next round (?)
    When the game has finished, show numer of rounds played, total correct, incorrect, prompt to play again.(list of missed words?)
        App reset or game replay

    App reset - 
    Reruns the start game function to clear board. 

    Game replay - 
    Increment round number
    Run randomize function against the existing list of cards. 
    Rerun gameplay function. 

MANAGE

    Choose Task - 
    Prompt user to input whether to create, edit, or delete a card. 
    Run corresponding function.

    Create card - 
    Prompt user for Spanish and English words. 
    Add to database. 
    Print confirmation message. 

    Edit card - 
    Prompt user to enter Spanish word for card. 
    Prompt user to choose Spanish or English to update. 
    Prompt user to enter new word. 
    Update card. 
    Print confirmation message. 

    Delete card - 
    Prompt user to enter Spanish word for card.
    Delete card.
    Print confirmation message. 

* FUNCTION

  start_game() 
    input for play/manage. 
    conditional to determine whether to run game_setup() or choose_task()

  game_setup()
    input for number of cards. 
    increment round number
    query db for count of cards.
    create list with total number of cards.
    run randomize_deck() against input list 
    UPDATE - use built in random function in peewee to pull initial deck
    add correct/incorrect keys to cards
    run play_game()

shuffle_deck() 
    accept list as arg
    randomize list order and 
    return new list

play_game() - 
    itterate over list of cards with for loop with max of total number of cards.
        show Spanish and prompt for English
        if answer is correct, display correct message, increment correct count. 
        if answer is incorrect, display message with correct answer, increment incorrect count.
        clear screen.
        repeat with next card. 

    end_game()

end_game()
    show totals for correct/incorrect.
    prompt user to play again or return to home screen.
        replay_game()
        reset()

replay_game()
    increment round number
    run randomize_deck() on card list
    play_game()

reset()
    clear round number 
    clear list of cards
    start_game()

manage_cards()
    choose_task()
    prompt user for additional update or return to home
        choose_task()
        reset()

choose_task()
    prompt user for create/edit/delete
        create_card()
        edit_card()
        delete_card()

create_card()
    prompt user for spanish
    prompt user for english
    query db to create new card.
    print confirmation

edit_card()
    prompt user for spanish on existing card.
    prompt user for language to update.
    prompt user for updated value
    query db to find card w/ spanish and update with new value.
    print confirmation.

delete_card()
    prompt user for spanish on existing card.
    prompt user to confirm delete (repeat input value).
    query db to delete_instance.

 PLAN OF ATTACK

1. Set up DB DONE
2. Create Models DONE
3. Create Data DONE
4. Seed Database DONE
5. Set Up Game play functions
6. Set up CUD functions.
7. Add game vs manage functions.
