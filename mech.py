from cur import *
import curses

stdscr = curses.initscr()

curses.cbreak()
curses.echo()
try:
    siatka = Siatka(4,3,5,7)
    log = Logi(4,3,5,7)
    sleep(1)
    siatka.create(0,0 ,'1' )
    sleep(1)
    # siatka.create(2,1 , '2')
    # sleep(1)
    # siatka.move(2,1,0,0,'2')
    # sleep(1)
    # siatka.move(2,1,0,1,'2')
    # sleep(1)
    # siatka.destroy(0,0 )
    # sleep(1)
    # siatka.move(0,1,0,0,'2')
    log.write("whateba")
    sleep(1)
    log.write("whateba")
    sleep(1)
    log.write("whateban")
    sleep(1)
    log.write("whateba")
    sleep(1)
    log.write("whateba")
    sleep(1)
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
