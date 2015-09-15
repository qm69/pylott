#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from termcolor import colored, cprint


def print_head(title, last_base, actual):
    print(colored('\n  ' + title, 'blue', 'on_white'))
    print(colored('   last: ', 'green') +
          colored(last_base, 'red') +
          colored(', actual: ', 'green') +
          colored(actual, 'red'))


def print_save(draw, save):
    print(colored('  saved: ', 'green') +
          colored(draw, 'red') +
          colored(', id: ', 'green') +
          # colored(str(save)[-6:], 'red')
          colored(save, 'red'))


def print_red(some_text):
    cprint('  ' + some_text, 'red')
