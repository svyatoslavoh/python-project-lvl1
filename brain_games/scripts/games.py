#!/usr/bin/env python3
"""Game modules."""

import prompt
import random


def ask_name():
    """Ask for the name.

    Returns:
        name: name of user

    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

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


def get_random(start, stop):
    """Generate random num.

    Returns:
        random: random num
    """
    return random.randint(start, stop)


def get_random_item(item):
    """Get random item.

    Returns:
        random: random item
    """
    return random.choice(list(item))


def check_answer(true_answer, answer):
    """Cheking users unswers.

    Args:
        true_answer: true answer
        answer: answer of user

    """
    check = 1 if true_answer == answer else 0

    return check


def game(name, get_params):
    """Game func.

    Args:
        name: name of the user

    """
    trying = 0
    while trying < 3:
        true_answer, qustion = get_params()
        answer = ask_question(qustion)
        check = check_answer(true_answer, answer)

        if check == 0:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{true_answer}".')
            print(f'Let as try again, {name}!')

            return

        print('Correct!')
        trying += 1

    print(f'Congratulations, {name}!')
