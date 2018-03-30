import curses
import threading
import random
import time

stdscr = curses.initscr()


class Board:

    def __init__(self):
        stdscr.addch(0, 0, ' ')
        stdscr.refresh()
        for i in range(2, 10, 1):
            stdscr.addstr(0, i, str(i - 1))
            stdscr.refresh()
        for i in range(2, 10, 1):
            j = 10 - i
            stdscr.addch(i, 0, str(j))
            stdscr.refresh()
        for i in range(2, 10, 1):
            stdscr.addch(1, i, '-')
            stdscr.refresh()
        for i in range(2, 10, 1):
            stdscr.addch(i, 1, '|')
            stdscr.refresh()
        for i in range(2, 10, 1):
            stdscr.addch(10, i, '-')
            stdscr.refresh()
        for i in range(2, 10, 1):
            stdscr.addch(i, 11, '|')
            stdscr.refresh()
