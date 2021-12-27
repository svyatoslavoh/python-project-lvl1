#!/usr/bin/env python
"""Programm for calc."""

from .brain_games import ask_name, get_random, game, get_random_item


def main():
    """Headest prog.

    Args:
    name: string

    """
    name = ask_name()
    print('Find the greatest common divisor of given numbers.')
    game(name, get_progression, check_answer)


def get_progression():
    """Get const of game.

    Returns:
        true_answer: int true answer
        qustion: string whith rundom num

    """
    step = get_random(2, 9)
    start = get_random(1, 20)
    list_progressiv = list(range(start, 100, step)[:10])

    op = get_random_item(enumerate(list_progressiv))
    list_progressiv[op[0]] = '..'
    qustion = " ".join(map(str, list_progressiv))
    true_answer = op[1]

    return true_answer, qustion


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
