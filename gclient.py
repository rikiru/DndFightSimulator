from dnd import *

stdscr = curses.initscr()
curses.curs_set(0)
curses.mousemask(1)
curses.cbreak()
curses.echo()
try:
    curses.start_color()
    gra = GraClient()
    curses.endwin()
    exit(0)
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
