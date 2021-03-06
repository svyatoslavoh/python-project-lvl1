#!/usr/bin/env python
"""Programm for calc."""

import math


from .games import ask_name, get_random, game


def main():
    """Headest prog.

    Args:
    name: string

    """
    name = ask_name()
    print('Find the greatest common divisor of given numbers.')
    game(name, get_calc)


def get_calc():
    """Get const of game.

    Returns:
        true_answer: int true answer
        qustion: string whith rundom num

    """
    num1 = get_random(1, 10)
    num2 = get_random(1, 10)

    true_answer = str(math.gcd(num1, num2))
    qustion = f'{num1} {num2}'

    return true_answer, qustion


if __name__ == '__main__':
    main()
