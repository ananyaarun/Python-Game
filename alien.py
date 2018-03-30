import curses
import threading
import random
import time
import confing

stdscr = curses.initscr()


class alien():

    def __init__(self):
        self.alienx = 5
        self.alieny = 2
        self.__al = '*'
        stdscr.addch(self.alieny, self.alienx, '*')
        stdscr.refresh()
        self.interval = 10
        confing.flag = 0
        thread = threading.Thread(target=self.draw, args=())
        thread.daemon = True
        thread.start()

    def draw(self):

        while True:

            xx = random.randint(2, 9)
            yy = random.randint(2, 3)
            stdscr.addch(yy, xx, '*')
            stdscr.refresh()
            stdscr.addch(self.alieny, self.alienx, ' ')
            stdscr.refresh()
            self.alieny = yy
            self.alienx = xx
            time.sleep(8)
            confing.flag = 1
            stdscr.addch(self.alieny, self.alienx, ' ')
            stdscr.refresh()
            time.sleep(2)
            confing.flag = 0
