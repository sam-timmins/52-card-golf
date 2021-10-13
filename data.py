import gspread
from google.oauth2.service_account import Credentials
from utils import delay_print, clear_terminal

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


computer_jokes = {
    "queston1": {
        "question": "Why does the computer keep coughing?",
        "answer": "It has a virus"
    },

    "queston2": {
        "question": "How do you stop your laptop's charge running out?",
        "answer": "You hide its trainers."
    },

    "queston3": {
        "question": "How does a computer eat computer chips?",
        "answer": "With mega-bytes."
    },

    "queston4": {
        "question": "What do you get if you cross an elephant with a computer?",
        "answer": "Bits of plastic all over the floor."
    },

    "queston5": {
        "question": "Why was the computer late?",
        "answer": "It had a hard drive."
    },

    "queston6": {
        "question": "Why did the keyboards break up?",
        "answer": "They weren't each other's type."
    },

    "queston7": {
        "question": "How many computer programmers are needed to put in a light bulb?",
        "answer": "None, it's a hardware issue."
    },

    "queston8": {
        "question": "What do you call the woman who married the internet?",
        "answer": "The wife-i."
    },

    "queston9": {
        "question": "Have you seen the maths website?",
        "answer": "Yes, it added a lot to my day."
    },

    "queston10": {
        "question": "Where did the software developer go?",
        "answer": "I don’t know, he ransomware!"
    }
}


def game_rules():
    """
    Text for the rules of the game
    """
    rules_logo()
    delay_print("A game of skill and pure luck!! \n", 3)
    delay_print("The winner will have the lowest cumulative score", 1)
    delay_print("at the end of the game. \n", 3)
    delay_print("We use a standard 52-card pack. \n", 3)
    delay_print("You will be asked how many cards you would like to "
                "play with. \n", 3)
    delay_print("You can pick between 3 and 10 cards", 2)
    delay_print("There will always be one less round that the number "
                "of cards you select", 2)
    delay_print("3 cards selected will play 2 rounds", 1)
    delay_print("8 cards selected will play 7 rounds \n", 1)
    delay_print("The computer will randomly deal. \n", 3)
    delay_print("Your cards will be shown to you at the start. \n", 3)
    delay_print("They will be displayed as ['D9', 'S9', 'C2', 'H1'] \n", 3)
    delay_print("The first letter describes the suit... \n", 2)
    delay_print("H - Hearts, D - Diamonds, S - Spades and C - Clubs \n", 3)
    delay_print("The number then is the value... \n", 3)
    delay_print("Ace is 1, Jack is 11, Queen is 12 and King is 13 \n", 3)
    delay_print("The computer will pick the top card from the deck", 0)
    delay_print("and show it to you \n", 3)
    delay_print("You then get the option to 'swap' or 'pass' \n", 3)
    delay_print("If it is lower than one that you have you can 'swap'", 0)
    delay_print("it with one of yours \n", 3)
    delay_print("Choosing 'pass' ends your turn and gives the computer a "
                "go \n", 3)
    delay_print("Pick wisely, one card cannot be changed!! \n", 3)
    delay_print("", 3)


def select_number_of_cards_for_game_text():
    """
    Text for the number of cards
    """
    clear_terminal()
    logo()
    delay_print("Here we go.....", 2)
    print()
    delay_print("Pick the number of cards you would like...", 0)


def computers_move_text():
    """
    Text for the computer's move
    """
    delay_print("Computer is thinking..", 2)
    delay_print("Computer is thinking....", 2)
    delay_print("Computer is thinking......\n", 2)
    delay_print("The computer has completed it's move..\n", 2)


def game_over_text():
    """
    Text for game over
    """
    game_over_logo()
    delay_print("Totaling the scores...", 3)
    delay_print("Ready in...", 2)
    delay_print("3...", 1)
    delay_print("2...", 1)
    delay_print("1...", 1)
    print()


def logo():
    """
    Text for the game logo
    """
    print("""


         _____ ___     _____              _    _____       _  __
        | ____|__ \   / ____|            | |  / ____|     | |/ _|
        | |__    ) | | |     __ _ _ __ __| | | |  __  ___ | | |_
        |___ \  / /  | |    / _` | '__/ _` | | | |_ |/ _ \| |  _|
         ___) |/ /_  | |___| (_| | | | (_| | | |__| | (_) | | |
        |____/|____|  \_____\__,_|_|  \__,_|  \_____|\___/|_|_|



         """)


def game_over_logo():
    """
    Game over logo
    """
    print("""

    
           _____                         ____
          / ____|                       / __ \ 
         | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __
         | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
         | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |
          \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|


          
        """)


def rules_logo():
    """
    Logo for the read rules screen
    """
    print("""


                     _____       _
                    |  __ \     | |
                    | |__) |   _| | ___  ___
                    |  _  / | | | |/ _ \/ __|
                    | | \ \ |_| | |  __/\__ \ 
                    |_|  \_\__,_|_|\___||___/



    """)


def computers_move_logo():
    print("""
    

             __  __         __  __                            
            |  \/  |       |  \/  |                           
            | \  / |_   _  | \  / | _____   _____             
            | |\/| | | | | | |\/| |/ _ \ \ / / _ \            
            | |  | | |_| | | |  | | (_) \ V /  __/  _   _   _ 
            |_|  |_|\__, | |_|  |_|\___/ \_/ \___| (_) (_) (_)
                     __/ |                            
                    |___/ 


    """)
