"""Rock paper scissors game for micro:bit

Written for the Embedded and Robotics Society at the
University of Edinburgh.
Original author: Cameron MacLeod (@notexaclyawe)
"""

# Program flow:
#   --- Repeat indefinitely ---
#   Take input from user and listen for selection from opponent
#   When user input send "r" "p" or "s"
#   When both input and opponent, display win or lose
#   ---
# Original intention was to have a discovery step before the game began
# but there isn't much point to that and would lead to annoying state
# bugs where one micro:bit is listening for the opponent to connect and
# the opponent is listening for the play

from microbit import *
import radio

# Channel the game will be played on. Needs to be the same on both
# micro:bits. Value between 0-83
CHANNEL = 42

# Dictionary from move to move that it beats. Used to check if a move
# has won
WIN_TABLE = {'r': 's',
             'p': 'r',
             's': 'p'}

radio.on()
radio.config(channel=CHANNEL)

def did_user_win(user_input, opponent_input):
    """Takes two inputs from 'r', 'p', 's' and returns an image
    representing the result in a game of rock, paper, scissors.
    """
    if user_input == opponent_input:
        return '-'
    if WIN_TABLE[user_input] == opponent_input:
        return Image.HAPPY
    else:
        return Image.SAD

def get_moves():
    """Gets user input and listens for opponent's move
    Return: An image representing whether the user won, lost or drew
    """
    opponent_input = None
    user_input = None

    while opponent_input is None or user_input is None:
        if opponent_input is None:
            # non-blocking, just checks a queue
            msg = radio.receive()
            # assert a message from our game was received
            if msg is not None and msg in ['r', 'p', 's']:
                opponent_input = msg

        if user_input is None:
            # obtain once since function has side effects
            a = button_a.was_pressed()
            b = button_b.was_pressed()
            if a and b:
                user_input = 's'
            elif a:
                user_input = 'r'
            elif b:
                user_input = 'p'

            if user_input is not None:
                # if we set the user input
                radio.send(user_input)

        sleep(200)

    return did_user_win(user_input, opponent_input)

while True:
    display.show('?')
    result_img = get_moves()
    display.show(result_img)
    sleep(2000)
