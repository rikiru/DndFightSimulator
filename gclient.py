from dnd import *

stdscr = curses.initscr()
curses.curs_set(0)
curses.mousemask(1)
curses.cbreak()
curses.echo()
try:
    gra = GraClient()
except Exception as e:
    print e
    curses.endwin()
    exit(0)
g= "z"
while g!="g":
    g=sys.stdin.read(1)
    if g == "q":
        curses.endwin()
        exit(0)
