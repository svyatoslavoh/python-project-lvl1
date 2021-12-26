#!/usr/bin/env python
"""Main programm."""


from .brain_games import ask_name, ask_question, get_random


def main():
    """Headest prog.

    Args:
    name: string

    """
    name = ask_name()
    game(name)


def game(name):
    """Game func.

    Args:
        name: name of the user

    """
    trying = 0
    while trying < 3:
        true_answer, qustion = get_even()
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

    Returns:
        check: one or ziro

    """
    check = 1 if true_answer == answer else 0

    return check


def get_even():
    """Get const of game.

    Args:
        num: rundom num
        answer: answer of user

    Returns:
        true_answer: int true answer
        num: int with rundom num

    """
    num = get_random()
    true_answer = 'yes' if num % 2 == 0 else 'no'

    return true_answer, num


if __name__ == '__main__':
    main()
