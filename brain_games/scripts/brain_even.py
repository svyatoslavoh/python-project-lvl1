#!/usr/bin/env python
"""Main programm."""


from .games import ask_name, get_random, game


def main():
    """Headest prog.

    Args:
    name: string

    """
    name = ask_name()
    game(name, get_even)


def get_even():
    """Get const of game.

    Args:
        num: rundom num
        answer: answer of user

    Returns:
        true_answer: int true answer
        num: int with rundom num

    """
    num = get_random(1, 10)
    true_answer = 'yes' if num % 2 == 0 else 'no'

    return true_answer, num


if __name__ == '__main__':
    main()
