#!/usr/bin/env python
"""Programm for calc."""


import prompt

import operator

import random


def main():
    """Headest prog.

    Args:
    name: string

    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    game(name)


def get_calc():
    """Game func calc.

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
    num1 = random.randint(0, 10)
    num2 = random.randint(1, 10)
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
        print(f'Question: {qustion}')
        answer = prompt.string('Your answer:')
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
    return 1 if float(true_answer) == float(answer) else 0


if __name__ == '__main__':
    main()
