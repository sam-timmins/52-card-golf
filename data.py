import gspread
from google.oauth2.service_account import Credentials
from utils import delay_print

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('52-card-golf')

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


def game_rules():
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


def logo():
    print("""
         _____ ___     _____              _    _____       _  __
        | ____|__ \   / ____|            | |  / ____|     | |/ _|
        | |__    ) | | |     __ _ _ __ __| | | |  __  ___ | | |_
        |___ \  / /  | |    / _` | '__/ _` | | | |_ |/ _ \| |  _|
         ___) |/ /_  | |___| (_| | | | (_| | | |__| | (_) | | |
        |____/|____|  \_____\__,_|_|  \__,_|  \_____|\___/|_|_|
         """)


def select_number_of_cards_for_game_text():
    delay_print("Here we go.....", 2)
    print()
    delay_print("Pick the number of cards you would like...", 0)
    delay_print("Choices are 4, 6 or 8", 1)


def computers_move_text():
    delay_print("Computer is thinking..", 2)
    delay_print("Computer is thinking....", 2)
    delay_print("Computer is thinking......\n", 2)
    delay_print("The computer has completed it's move..\n", 2)


def game_over_text():
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

