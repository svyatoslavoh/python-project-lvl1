#!/usr/bin/env python
import prompt

def main():
    print('Welcome to the Brain Games!')
    welcome_user()

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')


if __name__ == '__main__':
    main()