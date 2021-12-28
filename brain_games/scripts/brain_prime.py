#!/usr/bin/env python
"""Programm for calc."""


from .games import ask_name, get_random, game


def main():
    """Headest prog.

    Args:
    name: string

    """
    name = ask_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game(name, get_prime)


def get_prime():
    """Get const of game.

    Returns:
        true_answer: int true answer
        qustion: string whith rundom num

    """
    num = get_random(1, 30)

    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1

    true_answer = 'yes' if k <= 0 else 'no'

    return true_answer, num


if __name__ == '__main__':
    main()
