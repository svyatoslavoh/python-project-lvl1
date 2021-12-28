#!/usr/bin/env python
"""Programm for calc."""


import sympy

from .games import ask_name, get_random, game


def main():
    """Headest prog.

    Args:
    name: string

    """
    name = ask_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    game(name, get_prime)


def get_prime():
    """Get const of game.

    Returns:
        true_answer: int true answer
        qustion: string whith rundom num

    """
    num = get_random(1, 30)

    is_prime = sympy.isprime(num)
    true_answer = 'yes' if is_prime is True else 'no'
    qustion = f'{num}'

    return true_answer, qustion


if __name__ == '__main__':
    main()
