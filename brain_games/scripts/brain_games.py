#!/usr/bin/env python3
"""Main programm."""

import prompt


def main():
    """Make a hi intreface."""
    print('Welcome to the Brain Games!')
    welcome_user()


def welcome_user():
    """Ask for the name."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')


if __name__ == '__main__':
    main()
