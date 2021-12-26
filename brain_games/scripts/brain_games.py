#!/usr/bin/env python3
"""Main programm."""

import prompt
import random


def main():
    """Make a hi intreface."""
    ask_name()


def ask_name():
    """Ask for the name.

    Returns:
        name: name of user

    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    return name


def ask_question(qustion):
    """Ask for the name.

    Args:
        qustion: string qustion
    Returns:
        answer: answer of user

    """
    print(f'Question: {qustion}')
    answer = prompt.string('Your answer:')

    return answer


def get_random():
    """Ask for the name.

    Returns:
        random: random num
    """
    return random.randint(1, 100)


if __name__ == '__main__':
    main()
