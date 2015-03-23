#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    http://patorjk.com/software/taag
     _____         ______
    |  __ \       |  ____|
    | |__) |_   _ | |__  _   _  ___  ___
    |  ___/| | | ||  __|| | | |/ __|/ __|
    | |    | |_| || |   | |_| |\__ \\__ \
    |_|     \__, ||_|    \__,_||___/|___/
          __/ |
         |___/
"""
"""
Taskwarrior:
ID Project Pri(ritet) Started Due Recur Age Tags Description
Bold http://stackoverflow.com/questions/8924173
"""

if __name__ == '__main__':
    with open('main.py', 'r') as main_file:
        main_list = main_file.read().split("\n")
        print('\033[1m' + 'Filename  ' + 'Line ' \
            + ' Type  ' + 'Description' + '\033[0m'
        )
        for indx, line in enumerate(main_list):
            if line.strip().startswith("# TODO"):
                print("main.py   {}   {}".format(
                    indx,
                    line.strip()[2:])
                )
