import curses
import threading
import random
import time
import config

stdscr = curses.initscr()

score = 0


class missiles:
    def __init__(self, posy):
        self.posy = 8


class misi(missiles):
    def __init__(self, posy, posx, alienx, alieny):
        missiles.__init__(self, posy)
        self.mix = posx
        self.miy = posy
        self.alienx = alienx
        self.alieny = alieny

        self.__mi = 'i'
        self.interval = 1
        thread = threading.Thread(target=self.createmi, args=())
        thread.daemon = True
        thread.start()

    def createmi(self):
        global score

        while True and self.miy >= 1:
            if self.miy == 1:
                stdscr.addch(self.miy + 1, self.mix, ' ')
                stdscr.refresh()
                break
            stdscr.addch(self.miy, self.mix, 'i')
            stdscr.refresh()
            if self.alienx == self.mix and self.alieny == self.miy and\
               config.flag == 0:
                score = score + 1
                confing.flag = 1
                sco = "Score : " + str(score)
                stdscr.addstr(11, 0, sco)
                stdscr.refresh()
                stdscr.addch(self.alieny, self.alienx, ' ')
                stdscr.refresh()
                stdscr.addch(self.miy + 1, self.mix, ' ')
                stdscr.refresh()
                break
            if self.miy + 1 != 9:
                stdscr.addch(self.miy + 1, self.mix, ' ')
                stdscr.refresh()
            self.miy = self.miy - 1
            time.sleep(self.interval)


class misI(missiles):
    def __init__(self, posy, posx, alienx, alieny):
        missiles.__init__(self, posy)
        self.mIx = posx
        self.mIy = posy
        self.alienx = alienx
        self.alieny = alieny

        self.__mi = 'I'
        self.interval = 1
        thread = threading.Thread(target=self.createmi, args=())
        thread.daemon = True
        thread.start()

    def createmi(self):

        while True and self.mIy >= 0:
            if self.mIy == 0:
                stdscr.addch(self.mIy + 2, self.mIx, ' ')
                stdscr.refresh()
                break
            stdscr.addch(self.mIy, self.mIx, 'I')
            stdscr.refresh()
            if self.alienx == self.mIx and self.alieny == self.mIy and\
                    config.flag == 0:
                stdscr.addch(self.alieny, self.alienx, '#')
                stdscr.refresh()
                stdscr.addch(self.mIy + 2, self.mIx, ' ')
                stdscr.refresh()
                time.sleep(5)
            if self.mIy + 1 != 9:
                stdscr.addch(self.mIy + 2, self.mIx, ' ')
                stdscr.refresh()
            self.mIy = self.mIy - 2
            time.sleep(self.interval)
