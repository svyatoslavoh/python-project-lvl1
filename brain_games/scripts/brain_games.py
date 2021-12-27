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


def get_random(start, stop):
    """Get random num.

    Returns:
        random: random num
    """
    return random.randint(start, stop)


def get_random_item(item):
    """Ask for the name.

    Returns:
        random: random item
    """
    return random.choice(list(item))


def game(name, get_calc, check_answer):
    """Game func.

    Args:
        name: name of the user

    """
    trying = 0
    while trying < 3:
        true_answer, qustion = get_calc()
        answer = ask_question(qustion)
        check = check_answer(true_answer, answer)

        if check == 0:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{true_answer}".')
            print(f'Let as try again, {name}!')

            return

        print('Correct!')
        trying += 1

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
