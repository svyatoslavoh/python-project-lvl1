#!/usr/bin/env python
"""Main programm."""

import random

import prompt


def main():
    """Headest prog.

    Args:
    name: string

    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game(name)


def game(name):
    """Game func.

    Args:
        name: name of the user

    """
    trying = 0
    while trying < 3:
        rannum = random.randint(1, 100)
        print(f'Question: {rannum}')
        answer = prompt.string('Your answer:')
        check, true_answer = check_answer(rannum, answer)

        if check == 0:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{true_answer}".')
            print(f'Let as try again, {name}!')

            return

        print('Correct!')
        trying += 1

    print(f'Congratulations, {name}!')


def check_answer(num, answer):
    """Cheking users unswers.

    Args:
        num: rundom num
        answer: answer of user

    Returns:
        check: one or ziro
        true_answer: true answer

    """
    true_answer = 'yes' if num % 2 == 0 else 'no'
    check = 1 if true_answer == answer else 0

    return check, true_answer


if __name__ == '__main__':
    main()
