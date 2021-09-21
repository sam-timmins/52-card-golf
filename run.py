# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import random
from utils import delay_print
from data import user_playing_cards, computer_playing_cards, \
    display_user_cards, the_deck, game_rules, logo, computers_move_text


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('52-card-golf')


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
    logo()
    user_name = input('Please enter your name: ')
    print()
    while (len(user_name)) == 0:
        user_name = input('Please enter your name: \n')
    read_rules = input(f'Hi {user_name}, would you like to read the rules of '
                       'the game?\nyes or no: ')
    if read_rules.lower() == 'y' or read_rules.lower() == 'yes':
        print()
        game_rules()
        select_number_of_cards_for_game()
    elif read_rules.lower() == 'n' or read_rules.lower() == 'no':
        print()
        select_number_of_cards_for_game()
    else:
        delay_print("Please enter a correct option...", 2)
        user_name = input('Please enter your name: \n')


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
    number_of_cards = int(input("\n"))
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
    delay_print(f"You're game total is: {user_game_total()}", 2)


def users_move():
    """
    Picks a card from the deck, displays it and formats it to an integer
    Invites the user to swap or pass. Swap leads to a move, pass gives the
    computer a move
    """
    pick_card_from_deck()
    format_card_to_int()
    delay_print(f"The top card picked from the deck is {card_selection}", 2)
    print()
    delay_print("What's your next move?", 1)
    swap_or_not = input("'swap' or 'pass': \n")
    if swap_or_not.lower() == 'swap':
        print()
        delay_print("Which card would you like to swap?", 1)
        print()
        delay_print("Please choose from:", 2)
        delay_print("1 - your first card in the row", 2)
        delay_print("2 - your second card in the row", 2)
        delay_print("etc...", 2)

        print()
        swap_users_card()
    elif swap_or_not.lower() == 'pass':
        print()
        return


def computers_move():
    """
    Picks and formats a card from the_deck. Changes the highest number in
    computer_playing_cards if the picked card is less than 7
    """
    pick_card_from_deck()
    format_card_to_int()
    computer_playing_cards.sort()
    if formatted_card < computer_playing_cards[-1]:
        computer_playing_cards[-1] = formatted_card
    else:
        formatted_card >= computer_playing_cards[-1]
    computers_move_text()


def swap_users_card():
    """
    Swaps the user's card depending on their choice of game, then the card
    """
    swap_card_number = 0
    print(display_user_cards)
    print()
    swap_card_number = input("Card number: \n")
    formatted_swap_card_number = int(swap_card_number)
    if number_of_cards == 4:
        if formatted_swap_card_number == 1:
            user_playing_cards[0] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[0]} for {card_selection}", 2)
            display_user_cards[0] = card_selection
        elif formatted_swap_card_number == 2:
            user_playing_cards[1] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[1]} for {card_selection}", 2)
            display_user_cards[1] = card_selection
        elif formatted_swap_card_number == 3:
            user_playing_cards[2] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[2]} for {card_selection}", 2)
            display_user_cards[2] = card_selection
        elif formatted_swap_card_number == 4:
            user_playing_cards[3] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[3]} for {card_selection}", 2)
            display_user_cards[3] = card_selection
        elif formatted_card != 1 or 2 or 3 or 4:
            print("Please enter either a number between 1 and 4")
            swap_card_number = input("Card number: \n")
    elif number_of_cards == 6:
        if formatted_swap_card_number == 1:
            user_playing_cards[0] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[0]} for {card_selection}", 2)
            display_user_cards[0] = card_selection
        elif formatted_swap_card_number == 2:
            user_playing_cards[1] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[1]} for {card_selection}", 2)
            display_user_cards[1] = card_selection
        elif formatted_swap_card_number == 3:
            user_playing_cards[2] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[2]} for {card_selection}", 2)
            display_user_cards[2] = card_selection
        elif formatted_swap_card_number == 4:
            user_playing_cards[3] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[3]} for {card_selection}", 2)
            display_user_cards[3] = card_selection
        elif formatted_swap_card_number == 5:
            user_playing_cards[4] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[4]} for {card_selection}", 2)
            display_user_cards[4] = card_selection
        elif formatted_swap_card_number == 6:
            user_playing_cards[5] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[5]} for {card_selection}", 2)
            display_user_cards[5] = card_selection
        elif formatted_card != 1 or 2 or 3 or 4 or 5 or 6:
            print("Please enter either a number between 1 and 6")
            swap_card_number = input("Card number: \n")
    elif number_of_cards == 8:
        if formatted_swap_card_number == 1:
            user_playing_cards[0] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[0]} for {card_selection}", 2)
            display_user_cards[0] = card_selection
        elif formatted_swap_card_number == 2:
            user_playing_cards[1] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[1]} for {card_selection}", 2)
            display_user_cards[1] = card_selection
        elif formatted_swap_card_number == 3:
            user_playing_cards[2] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[2]} for {card_selection}", 2)
            display_user_cards[2] = card_selection
        elif formatted_swap_card_number == 4:
            user_playing_cards[3] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[3]} for {card_selection}", 2)
            display_user_cards[3] = card_selection
        elif formatted_swap_card_number == 5:
            user_playing_cards[4] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[4]} for {card_selection}", 2)
            display_user_cards[4] = card_selection
        elif formatted_swap_card_number == 6:
            user_playing_cards[5] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[5]} for {card_selection}", 2)
            display_user_cards[5] = card_selection
        elif formatted_swap_card_number == 7:
            user_playing_cards[6] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[6]} for {card_selection}", 2)
            display_user_cards[6] = card_selection
        elif formatted_swap_card_number == 8:
            user_playing_cards[7] = formatted_card
            print()
            delay_print(f"Swapping {display_user_cards[7]} for {card_selection}", 2)
            display_user_cards[7] = card_selection
        elif formatted_card != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
            print("Please enter either a number between 1 and 8")
            swap_card_number = input("Card number: \n")
    delay_print(f"You're game total is: {user_game_total()}", 2)
    print()


def user_game_total():
    """
    Adds up the cumulative score or the user
    """
    user_game_total = sum(user_playing_cards)
    print()
    return user_game_total


def computer_game_total():
    """
    Adds up the cumulative score or the computer
    """
    computer_game_total = sum(computer_playing_cards)
    return computer_game_total


def end_game():
    """
    Gives final feedback of the game depending on the score
    """
    user_score = user_game_total()
    computer_score = computer_game_total()
    delay_print("", 2)
    print("""
           _____                         ____
          / ____|                       / __ \ 
         | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __
         | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
         | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |
          \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|
          """)
    delay_print("Totaling the scores...", 3)
    delay_print("Ready in...", 2)
    delay_print("3...", 1)
    delay_print("2...", 1)
    delay_print("1...", 1)
    print()
    delay_print(f"You're total was {user_score}", 2)
    print()
    delay_print(f"Computer's total was {computer_score}", 2)
    print()
    if user_score < computer_score:
        delay_print("Great job, you're the winner!", 2)
    elif user_score > computer_score:
        delay_print("Unlucky, the computer wins!", 2)
    else:
        delay_print("It's a draw....", 2)
    print()
    delay_print("Have another game!", 2)


def main():
    """
    The main game loop
    """
    rounds = 1
    pre_game_username_and_rules()
    user_game_total()
    if number_of_cards == 4:
        while rounds < 4:
            delay_print(f"Round: {rounds} of 3", 2)
            print()
            rounds += 1
            users_move()
            computers_move()
    elif number_of_cards == 6:
        while rounds < 6:
            delay_print(f"Round: {rounds} of 5", 2)
            print()
            rounds += 1
            users_move()
            computers_move()
    elif number_of_cards == 8:
        while rounds < 8:
            delay_print(f"Round: {rounds} of 7", 2)
            print()
            rounds += 1
            users_move()
            computers_move()
    end_game()


main()