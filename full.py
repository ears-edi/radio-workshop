from microbit import *
import radio

# TODO: CHANGE ME
CHANNEL = 42

radio.on()
radio.config(channel=CHANNEL)

# Dictionary from move to move that it beats. Used to check if a move
# has won
WIN_TABLE = {'r': 's',
             'p': 'r',
             's': 'p'}

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

def get_user_input():
    """Function that checks if the user has input a move and returns it.

    Return: 'r' if the user pressed button A
            'p' if the user pressed button B
            's' if the user pressed buttons A and B
            None if the user hasn't pressed any buttons.
    """
    # obtain once since function has side effects
    a = button_a.was_pressed()
    b = button_b.was_pressed()

    if a and b:
        return 's'
    elif a:
        return 'r'
    elif b:
        return 'p'

    # neither a or b was true
    return None


# this will run forever
while True:
    # variables to hold moves for this turn
    # will contain a string that is 'r', 'p' or 's'
    user_input     = None
    opponent_input = None

    display.show('?')

    while user_input is None or opponent_input is None:
        if user_input is None:
            user_input = get_user_input()
            if user_input is not None:
                display.show(user_input)
                radio.send(user_input)

        if opponent_input is None:
            opponent_input = radio.receive()

        sleep(200) # 0.2s

    result = did_user_win(user_input, opponent_input)
    display.show(result)

    sleep(2000)
