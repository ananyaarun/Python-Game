if __name__ == "__main__":
    import curses
    import threading
    import random
    import time
    from curses import wrapper
    from alien import *
    from board import *
    from spaceship import *
    from missile import *

    start = time.time()

    stdscr = curses.initscr()

    def main(stdscr):
        b = Board()
        s = spaceship()
        a = alien()

        curses.curs_set(0)
        while True:
            c = stdscr.getch()
            if c == ord('d'):
                s.moveright()
            elif c == ord('a'):
                s.moveleft()
            elif c == ord(' '):
                m1 = misi(8, s.posx, a.alienx, a.alieny)
            elif c == ord('s'):
                m2 = misI(8, s.posx, a.alienx, a.alieny)
            elif c == ord('q'):
                break

    stdscr.addstr(11, 0, 'Score : 0')
    stdscr.refresh()

    wrapper(main)
