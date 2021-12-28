#!/usr/bin/env python
"""Programm for calc."""


import operator

from .brain_games import ask_name, get_random, game, get_random_item


def main():
    """Headest prog.

    Args:
    name: string

    """
    name = ask_name()
    print('What is the result of the expression?')
    game(name, get_calc)


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
    num1 = get_random(1, 10)
    num2 = get_random(1, 10)
    op = get_random_item(ops.keys())

    true_answer = ops.get(op)(num1, num2)
    qustion = f'{num1} {op} {num2}'

    return str(true_answer), qustion


if __name__ == '__main__':
    main()
