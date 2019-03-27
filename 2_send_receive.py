from microbit import *
import radio

# TODO: CHANGE ME
CHANNEL = 42

radio.on()
radio.config(channel=CHANNEL)

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

    user_input = get_user_input()

    if user_input is not None:
        radio.send(user_input)

    opponent_input = radio.receive()
    if opponent_input is not None:
        display.show(opponent_input)

    sleep(200) # 0.2s


# Python cheat sheet
#
# Variables and types:
#
# my_int  = 3
# my_str  = 'some_str'
# my_list = [1, 2, 3, 'a']
#
# Lists:
#
# 'a' in ['a', 'b'] == True
#
# If statements:
#
# if condition:
#     do_something()
# elif condition2:
#     do_something_else()
# else:
#     print('no conditions matched!')
#
# Dictionaries:
#
# my_dict = {'a': 1, 'b': '2'}
# my_dict['a'] == 1
# my_dict['random'] ==> KeyError
#
# my_dict['c'] = 42
# my_dict['c'] == 42
#
# Loops:
#
# Runs while condition == True
# while condition:
#     do_something()
#
# Runs forever
# while True:
#     do_something()
#
# Micro:bit general functions:
#
# sleep(500) - Does nothing for 500ms
# display.show(Image.HAPPY) - Shows a smiley face on the screen
# display.show('a') - Shows the character 'a' on the screen
#
# Micro:bit buttons:
#
# button_a.was_pressed() - Returns whether the button was pressed since last time it was called
# button_b.was_pressed()
# button_a.get_presses() - Returns the number of presses since last call
#
# Micro:bit radio:
#
# radio.send('something') - Sends the string 'something' over your current channel
# msg = radio.receive() - Returns you any message that has been received. Doesn't block
#
# Available images:
# To see all images that are built in to micro:bit go here -> https://microbit-micropython.readthedocs.io/en/latest/image.html#attributes
