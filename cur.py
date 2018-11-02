import curses
import sys
from time import sleep
class Pole :
    def __init__(self,x,y,winh,winl):
        self.x = x
        self.y = y
        self.winh = winh
        self.winl = winl
        self.empty = False
        self.bohater = 0
        self.win = curses.newwin(winh, winl, 0+(winh*x), 0+(winl*y))
        self.win.box(0,0)
        self.win.refresh()

class Siatka:
    def move(self,ys, xs,yd,xd,char,bohater):
        if not self.win[xd][yd].empty:
            self.win[xs][ys].win.addch(self.winh/2,self.winl/2,' ')
            self.win[xs][ys].bohater = 0
            self.win[xs][ys].empty  = False
            self.win[xd][yd].win.addch(self.winh/2,self.winl/2,char)
            self.win[xd][yd].bohater = bohater
            self.win[xd][yd].empty  = True
            self.win[xs][ys].win.refresh()
            self.win[xd][yd].win.refresh()
    def create(self,y, x,char,bohater):
        self.win[x][y].bohater = bohater
        self.win[x][y].empty  = True
        self.win[x][y].win.addch(self.winh/2,self.winl/2,char)
        self.win[x][y].win.refresh()
    def destroy(self,y, x):
        self.win[x][y].bohater = 0
        self.win[x][y].win.addch(self.winh/2,self.winl/2,' ')
        self.win[x][y].empty  = False
        self.win[x][y].win.refresh()
    def __init__(self,h,l,winh,winl):
        self.win = [[Pole(x,y,winh,winl) for x in range(h)] for y in range(l)]
        self.l =l
        self.h =h
        self.winh = winh
        self.winl = winl

class Logi:
    def write(self, string):
        self.win.addstr(self.count+1,1,string)
        self.win.refresh()
        self.count += 1
    def __init__(self,h,l,winh,winl):
        self.count = 0
        self.winh = winh*h
        self.winl = curses.COLS -1 - winl * l
        self.win=curses.newwin(self.winh, self.winl, 0, winl * l)
        self.win.box(0,0)
        self.win.refresh()


# stdscr = curses.initscr()
#
# curses.cbreak()
# curses.echo()
# try:
#     siatka = Siatka(4,3,5,7)
#     log = Logi(4,3,5,7)
#     sleep(1)
#     siatka.create(0,0 ,'1' )
#     sleep(1)
#     # siatka.create(2,1 , '2')
#     # sleep(1)
#     # siatka.move(2,1,0,0,'2')
#     # sleep(1)
#     # siatka.move(2,1,0,1,'2')
#     # sleep(1)
#     # siatka.destroy(0,0 )
#     # sleep(1)
#     # siatka.move(0,1,0,0,'2')
#     log.write("whateba")
#     sleep(1)
#     log.write("whateba")
#     sleep(1)
#     log.write("whateban")
#     sleep(1)
#     log.write("whateba")
#     sleep(1)
#     log.write("whateba")
#     sleep(1)
# except Exception as e:
#     print e
#     curses.endwin()
#     exit(0)
# g= "z"
# while g!="g":
#     g=sys.stdin.read(1)
#     if g == "q":
#         curses.endwin()
#         exit(0)
