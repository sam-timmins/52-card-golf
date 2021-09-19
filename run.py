# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import time


def delay_print(text, delay):
    """
    Delays the print statment

    Parameters:
        text (string) - text to be printed out
        delay (integer) - the number of seconds to delay by 
    """
    print(text)
    time.sleep(delay)


def pick_card_from_deck():
    """
    Creates a global variable card_selection
    Selects a random card from the deck and removes it from the deck
    """


def format_card_to_int():
    """
    Creates a global variable formatted_card
    Strips out the number from anything selected from the deck and
    converts the string to an integer 
    """


def pre_game_username_and_rules():
    """
    Makes sure the user enters a value into the user name input, then asks
    for the user to decide if they want to read the rules or not. If they do,
    it brings up the rules, if not then starts the game
    """


def select_number_of_cards_for_game():
    """
    Lets the user input how many cards they and computer will play with
    during that game.
    Then calls the deal_cards function
    """


def deal_cards():
    """
    Randomly selects hand of cards from the_deck list and adds them to
    the user_playing_cards and to computer_playing_cards.
    Formats the cards into integers and removes the random cards
    from the the_deck list.
    Creates a display friendly list of cards for the user (display_user_cards)
    Shows the user their cards for playing with
    """


def users_move():
    """
    Picks a card from the deck, displays it and formats it to an integer
    Invites the user to swap or pass. Swap leads to a move, pass give the
    computer a move
    """


def computers_move():
    """
    Picks and formats a card from the_deck. Changes the highest number in
    computer_playing_cards if the picked card is less than 7
    """


def swap_users_card():
    """
    Swaps the user's card depending on their choice of game and then card
    """


def user_game_total():
    """
    Adds up the cumulative score or the user
    """


def computer_game_total():
    """
    Adds up the cumulative score or the computer
    """


def end_game():
    """
    Gives final feedback of the game depending on the score 
    """


def main();
    """
    The main game loop
    """