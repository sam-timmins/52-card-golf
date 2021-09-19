# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import time

user_playing_cards = []
computer_playing_cards = []
display_user_cards = []
the_deck = [
    'H1', 'H2',  'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10',
    'H11', 'H12', 'H13', 'S1', 'S2',  'S3', 'S4', 'S5', 'S6', 'S7',
    'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'D1', 'D2',  'D3', 'D4',
    'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'C1',
    'C2',  'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11',
    'C12', 'C13'
    ]


def delay_print(text, delay):
    """
    Delays the print statement

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
    global card_selection
    card_selection = random.choice(the_deck)
    the_deck.remove(card_selection)


def format_card_to_int():
    """
    Creates a global variable formatted_card
    Strips out the number from anything selected from the deck and
    converts the string to an integer
    """
    global formatted_card
    number_only = card_selection[1:]
    formatted_card = int(number_only)


def pre_game_username_and_rules():
    """
    Makes sure the user enters a value into the user name input, then asks for
    the user to decide if they want to read the rules or not. If they do,
    it brings up the rules, if not then starts the game
    """
    global user_name
    user_name = input('Please enter your name: ')
    print()
    while (len(user_name)) == 0:
        user_name = input('Please enter your name: ')
    read_rules = input(f'Hi {user_name}, would you like to read the rules of '
                       'the game?\nyes or no: ')
    if read_rules.lower() == 'y' or read_rules.lower() == 'yes':
        print()
        delay_print("A game of skill and pure luck!!", 3)
        delay_print("The winner will have the lowest cumulative score", 1)
        delay_print("at the end of the game.", 3)
        delay_print("We use a standard 52-card pack.", 3)
        delay_print("You will be asked how many cards you would like to "
                    "play.", 3)
        delay_print("4 cards selected will play 3 rounds", 3)
        delay_print("6 cards selected will play 5 rounds", 3)
        delay_print("8 cards selected will play 7 rounds", 3)
        delay_print("The computer will randomly deal.", 3)
        delay_print("Your cards will be shown to you at the start.", 3)
        delay_print("They will be displayed as ['D9', 'S9', 'C2', 'H1']", 3)
        delay_print("The first letter describes the suit...", 3)
        delay_print("H - Hearts, D - Diamonds, S - Spades and C - Clubs", 3)
        delay_print("The number then is the value...", 3)
        delay_print("Ace is 1, Jack is 11, Queen is 12 and King is 13", 4)
        delay_print("The computer will pick the top card from the deck", 1)
        delay_print("and show it to you", 3)
        delay_print("You then get the option to 'swap' or 'pass'", 3)
        delay_print("If it is lower than one that you have you can 'swap'", 3)
        delay_print("it with one of yours", 3)
        delay_print("Choosing 'pass' ends your turn and gives the computer a "
                    "go", 3)
        print()
        delay_print("Pick wisely, one card cannot be changed!!", 3)
        print()
        delay_print("", 3)
        select_number_of_cards_for_game()
    elif read_rules.lower() == 'n' or read_rules.lower() == 'no':
        print()
        select_number_of_cards_for_game()
    else:
        delay_print("Please enter a correct option...", 2)
        user_name = input('Please enter your name: ')


def select_number_of_cards_for_game():
    """
    Lets the user input how many cards they and the computer will play with
    during that game.
    Then calls the deal_cards function
    """
    global number_of_cards
    delay_print("Here we go.....", 2)
    print()
    delay_print("Pick the number of cards you would like...", 0)
    delay_print("Choices are 4, 6 or 8", 1)
    number_of_cards = int(input(""))
    deal_cards()


def deal_cards():
    """
    Randomly selects hand of cards from the_deck list and adds them to
    the user_playing_cards and to computer_playing_cards.
    Formats the cards into integers and removes the random cards
    from the the_deck list.
    Creates a display friendly list of cards for the user (display_user_cards)
    Shows the user their cards for playing with
    """
    while len(user_playing_cards) < number_of_cards:
        pick_card_from_deck()
        display_user_cards.append(card_selection)
        format_card_to_int()
        user_playing_cards.append(formatted_card)

    while len(computer_playing_cards) < number_of_cards:
        pick_card_from_deck()
        format_card_to_int()
        computer_playing_cards.append(formatted_card)
    print()
    delay_print(f"{user_name}, lets deal...", 2)
    print()
    delay_print(f"These are your cards.... {display_user_cards}", 2)


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
    Swaps the user's card depending on their choice of game, then the card
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


def main():
    """
    The main game loop
    """
