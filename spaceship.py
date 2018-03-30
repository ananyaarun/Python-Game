import curses
import threading
import random
import time

stdscr = curses.initscr()


class spaceship:

    def __init__(self):
        self.posx = 2
        self.posy = 9
        self.__ss = '^'
        stdscr.addch(9, 2, '^')
        stdscr.refresh()

    def moveright(self):
        if self.posx < 9:
            stdscr.addch(9, self.posx + 1, '^')
            stdscr.refresh()
            stdscr.addch(9, self.posx, ' ')
            stdscr.refresh()
            self.posx = self.posx + 1

    def moveleft(self):
        if self.posx > 2:
            stdscr.addch(9, self.posx - 1, '^')
            stdscr.refresh()
            stdscr.addch(9, self.posx, ' ')
            stdscr.refresh()
            self.posx = self.posx - 1
