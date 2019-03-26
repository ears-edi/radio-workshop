# Rock, Paper, Scissors - Micro:bit Radio Workshop

This repository contains the code for a radio workshop developed for the [University of Edinburgh Embedded and Robotics Society](http://ears-edi.com/). The workshop takes participants through building the game on the BBC micro:bit using its radio functionality, along the way explaining some concepts about radio communication in general. It was originally written for undergraduate students, but could be easily adapted for other audiences.

## Structure of the repo

The repository contains a series of python files starting from `initial_skeleton.py` through to `full.py`. These files contain the code at each stage of the workshop and are named after the step that they implement. This enables participants who fell behind during the workshop to catch up.

## Workshop set up

This workshop requires every participant to have a micro:bit and to pair up. During the workshop the pairs will work together to build the game and they will both be writing the same code. Each pair will need to be assigned a channel number from 0 to 83 so that the games can all operate on their own independent channels.

## Steps of the workshop

### Obtaining user input

This step asks the participants to fill in a `get_user_input` function. This function reads the state of the buttons and decides if the user wants to input rock, paper or scissors.

### Send and receive

Here the participants will send whatever the user has input to their radio channel and will also listen for incoming transmissions from their partner. This step aims to teach some foundational concepts such as receiving buffers and broadcast by default.

### Adding in rounds

A game consists of rounds where both players enter their decision and then the winner is decided. Before now the game had no concept of rounds, but this step adds that in and makes sure players only input their moves once per round.

### Checking win condition

In this step participants finish off the game by checking to see if either of the players won or if they drew. An appropriate image is then displayed on each micro:bit.

## Slides

The slides are available [here](https://docs.google.com/presentation/d/11BJfE25QNorKtRiN2Ap9PeLz7a0m58pVKTwm90xOupg/edit?usp=sharing).
