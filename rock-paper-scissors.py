#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rock beats scissors
Scissors beats paper
Paper beats rock
"""

import sys
import random


def computer_choice():
    choices = ['r', 's', 'p']
    comp_choice = random.choice(choices)
    print "Computer choice is: " + comp_choice.upper()
    return comp_choice


def compare_choices(me, comp):
    me_color = '\033[94m'
    comp_color = '\033[92m'
    both_bold = '\033[1m'
    reset_color = '\x1B[m'

    if me == comp:
        print "No winner.\nBoth of you choosed: " + both_bold + "[" + me + "]" + reset_color
    elif me == 'r':
        if comp == 'p':
            print "Computer wins! His choice is " + comp_color + "[" + comp + "]" + reset_color + " and yours is " + me_color + "[" + me + "]" + reset_color
        else:
            print "You win! Your choice is " + me_color + "[" + me + "]" + reset_color + " and comp's " + comp_color + "[" + comp + "]" + reset_color

    elif me == 's':
        if comp == 'r':
            print "Computer wins! His choice is " + comp_color + "[" + comp + "]" + reset_color + " and yours is " + me_color + "[" + me + "]" + reset_color
        else:
            print "You win! Your choice is " + me_color + "[" + me + "]" + reset_color + " and comp's " + comp_color + "[" + comp + "]" + reset_color

    elif me == 'p':
        if comp == 'r':
            print "You win! Your choice is " + me_color + "[" + me + "]" + reset_color + " and comp's " + comp_color + "[" + comp + "]" + reset_color
        else:
            print "Computer wins! His choice is " + comp_color + "[" + comp + "]" + reset_color + " and yours is " + me_color + "[" + me + "]" + reset_color


def play_game(choice):
    print "Your choice was: " + choice.upper()
    comp_choice = computer_choice()
    compare_choices(choice, comp_choice)


if __name__ == '__main__':
    buy = '\033[93m'
    while True:
        stay = raw_input("New game or exit?[n/x]")
        if stay == 'x':
            print(buy + "Buy!" + '\x1B[m')
            sys.exit()
        elif stay == 'n':
            choice = raw_input("Please choose from Rock [r], Scissors [s], Paper [p]")
            play_game(choice)
        else:
            print("Wrong input choose [n] or [x].")
            continue
