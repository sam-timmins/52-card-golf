# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import statistics
from utils import delay_print
from data import user_playing_cards, computer_playing_cards, \
    display_user_cards, the_deck, game_rules, logo, computers_move_text, \
    game_over_text, select_number_of_cards_for_game_text, SHEET

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


def pre_game_username():
    """
    Makes sure the user enters a value into the user name input, then asks for
    the user to decide if they want to read the rules or not. If they do,
    it brings up the rules, if not then starts the game
    """
    global user_name
    logo()
    show_game_score_history()
    print()
    delay_print("Please enter your name to begin", 0)
    user_name = input('  ')
    user_name = user_name.strip()
    while True:
        if (len(user_name)) == 0:
            user_name = input('  Please enter your name: ')
            user_name = user_name.strip()
        else:
            read_rules()
            break    


def read_rules():
    """
    Either displays the rules or skips to select_number_of_cards_for_game()
    """
    global user_name
    read_rules = input(f'Hi {user_name}, would you like to read the rules of '
                       'the game?\nyes or no: ')
    while True:
        if read_rules.lower() == 'y' or read_rules.lower() == 'yes':
            print()
            game_rules()
            select_number_of_cards_for_game()
            break
        elif read_rules.lower() == 'n' or read_rules.lower() == 'no':
            print()
            select_number_of_cards_for_game()
            break
        else:
            delay_print("Please enter a correct option...", 0)
            read_rules = input('yes or no: \n')


def select_number_of_cards_for_game():
    """
    Lets the user input how many cards they and the computer will play with
    during that game.
    Then calls the deal_cards function
    """
    global number_of_cards
    select_number_of_cards_for_game_text()
    number_of_cards = int(input(""))
    while True:
        if number_of_cards < 3 or number_of_cards > 10:
            delay_print("Please enter a number betwwen 3 and 10 inclusive", 0)
            number_of_cards = int(input(""))
        else:
            deal_cards()
            break


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
    delay_print("What's your next move?", 0)
    swap_or_not = input("swap ('s') or pass ('p'): \n")
    while True:
        if swap_or_not.lower() == 'swap' or swap_or_not.lower() == 's':
            print()
            delay_print("Which card would you like to swap?\n", 1)
            swap_users_card()
            return
        elif swap_or_not.lower() == 'pass' or swap_or_not.lower() == 'p':
            print()
            return
        else:
            swap_or_not = input("Please enter 'swap' or 'pass':")


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
    print(display_user_cards)
    print()
    swap_card_number = input("Card number: \n")
    while swap_card_number:
        if swap_card_number.upper() in display_user_cards:
            delay_print(f"Swapping {swap_card_number.upper()} for {card_selection}", 2)
            display_user_cards.remove(swap_card_number.upper())
            display_user_cards.insert(0, card_selection)
            break
        else:
            swap_card_number = input("Card number: \n")
    user_playing_cards.clear()
    for i in display_user_cards:
        user_playing_cards.append(int(i[1:]))
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
    global user_score
    user_score = user_game_total()
    computer_score = computer_game_total()
    game_over_text()
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
    delay_print("Have another game by hitting the button at the top!", 0)
    print("""
          _____________________
        /                       \ 
       |    PLAY 52 CARD GOLF    |
        \ _____________________ /
    """)


def data(user, cards, scores):
    """
    Collects the game data
    Parameters:
        user (string) - Collected from the variable user_name
        cards (int) - Collected from the variable number_of_cards
        scores (int) - Collected from the variable user_score
    """
    cards = number_of_cards
    user = user_name
    scores = user_score
    return [user, cards, scores]


def update_worksheet(data):
    """
    Adds the game data to google sheets
    Parameters:
        data (list)
    """
    worksheet = SHEET.worksheet('high_scores')
    worksheet.append_row(data)


def show_game_score_history():
    """
    Shows the last player's game stats and the average number of cards played with
    """
    worksheet = SHEET.worksheet('high_scores')
    score_data = worksheet.get_all_values()
    last_player = score_data[-1]
    delay_print("Game stats", 0)
    delay_print("___________________________ \n", 2)
    delay_print(f"The last player was {last_player[0]}.", 1)
    delay_print(f"They played with {last_player[1]} cards and scored {last_player[2]} points", 1)
    delay_print("", 1)

    number_of_cards_played_list = []
    for data in score_data:
        number_of_cards_played_list.append(data[1])
    num_only = number_of_cards_played_list[1:]
    convert_to_num = [int(i) for i in num_only]
    average = sum(convert_to_num) / len(convert_to_num)

    mode_card = statistics.mode(convert_to_num)

    delay_print(f"The average number of cards played with is {int(average)} \n", 2)
    delay_print(f"The most common number of cards played with is {mode_card} \n", 2)
    delay_print("___________________________ \n", 2)


def main():
    """
    The main game loop
    """
    rounds = 1
    pre_game_username()
    user_game_total()
    number_of_rounds = number_of_cards - 1
    while rounds < number_of_rounds + 1:
        delay_print(f"Round: {rounds} of {number_of_rounds}", 2)
        print()
        rounds += 1
        users_move()
        computers_move()
    end_game()
    update_worksheet(data(user_name, number_of_cards, user_score))


main()
