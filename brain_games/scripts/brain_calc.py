#!/usr/bin/env python
"""Programm for calc."""


import operator
import random


from .brain_games import ask_name, ask_question, get_random


def main():
    """Headest prog.

    Args:
    name: string

    """
    name = ask_name()
    print('What is the result of the expression?')
    game(name)


def get_calc():
    """Get const of game.

    Returns:
        true_answer: int true answer
        qustion: string whith rundom num

    """
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    num1 = get_random()
    num2 = get_random()
    op = random.choice(
        list(ops.keys())
    )

    true_answer = ops.get(op)(num1, num2)
    qustion = f'{num1} {op} {num2}'

    return true_answer, qustion


def game(name):
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


def check_answer(true_answer, answer):
    """Cheking users unswers.

    Args:
        true_answer: true answer
        answer: answer of user

    """
    check = 1 if float(true_answer) == float(answer) else 0

    return check


if __name__ == '__main__':
    main()
