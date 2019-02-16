import curses
import sys
from math import ceil
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
    def create(self,y, x,char,bohater):
        self.win[x][y].bohater = bohater
        self.win[x][y].empty  = True
        self.win[x][y].win.addstr(self.winh/2,self.winl/2,char,curses.color_pair(bohater.team))
        self.win[x][y].win.refresh()
    def move(self,ys, xs,yd,xd,char,bohater):
        if not self.win[xd][yd].empty:
            self.destroy(ys, xs)
            self.win[xd][yd].win.addstr(self.winh/2,self.winl/2,char,curses.color_pair(bohater.team))
            self.win[xd][yd].bohater = bohater
            self.win[xd][yd].empty  = True
            self.win[xs][ys].win.refresh()
            self.win[xd][yd].win.refresh()
    def destroy(self,y, x):
        self.win[x][y].bohater = 0
        self.win[x][y].win.addstr(self.winh/2,self.winl/2,' ')
        self.win[x][y].empty  = False
        self.win[x][y].win.refresh()
    def __init__(self,h,l,winh,winl):
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.win = [[Pole(x,y,winh,winl) for x in range(h)] for y in range(l)]
        self.l =l
        self.h =h
        self.winh = winh
        self.winl = winl
    def checkpoint(self,x,y):
        for i in range(self.l):
                for j in range(self.h):
                    bwy,bwx = self.win[i][j].win.getbegyx()
                    bly,blx = self.win[i][j].win.getmaxyx()
                    if x>bwx and bwx + blx>x and y>bwy and bwy + bly>y:
                        return self.win[i][j].x,self.win[i][j].y
        return -1,-1


class Logi:
    def write(self, string):
        dlugosc = len(string)
        if dlugosc > self.winl -2:
            ilosc = dlugosc/ (self.winl -2)
            ilosc += 1
            for i in range(ilosc):
                self.tekst.append(string[0+((self.winl -2)*i):(self.winl -2)+((self.winl -2)*i)])
        else:
            ilosc = 1
            self.tekst.append(string)
        self.strona = (len(self.tekst)-1)/(self.winh-5)
        self.wypiszstrone();
    def __init__(self,h,l,winh,winl):
        self.tekst =[]
        self.strona = 0
        self.winh = winh*h
        self.winl = curses.COLS -1 - winl * l
        self.win=curses.newwin(self.winh, self.winl, 0, winl * l)
        self.win.box(0,0)
        self.win.refresh()
        self.winleft = curses.newwin(3,(self.winl/2),self.winh-4,winl *l+1)
        self.winleft.addstr(1,1,"<-")
        self.winleft.box(0,0)
        self.winleft.refresh()
        self.winright = curses.newwin(3,(self.winl/2)-1,self.winh-4,winl *l + (self.winl/2) +1 )
        self.winright.addstr(1,1,"->")
        self.winright.box(0,0)
        self.winright.refresh()
    def checkpoint(self,x,y):
        bwy,bwx = self.winleft.getbegyx()
        bly,blx = self.winleft.getmaxyx()
        if x>bwx and bwx + blx>x and y>bwy and bwy + bly>y:
            self.strona = self.strona -1
            if self.strona == -1 :
                self.strona = 0
            self.wypiszstrone()
            return 1
        bwy,bwx = self.winright.getbegyx()
        bly,blx = self.winright.getmaxyx()
        if x>bwx and bwx + blx>x and y>bwy and bwy + bly>y:
            self.strona = self.strona + 1
            if  len(self.tekst) < self.strona*(self.winh -5) :
                self.strona = self.strona -1
            self.wypiszstrone()
            return 2
        return -1
    def wypiszstrone(self):
        self.wyzeruj()
        i=1
        for tekst in self.tekst[self.strona*(self.winh -5):(self.winh - 5)+(self.strona*(self.winh-5))]:
            self.win.addstr(i,1,tekst)
            i=i+1
            self.win.refresh()
    def wyzeruj(self):
        for i in range(1,self.winh-4):
            for j in range(1,self.winl -1):
                self.win.addch(i,j,' ')

class Buttonwin():
    def __init__(self,h,l,winh,winl,inside):
        self.winh = winh
        self.winl = winl
        self.h=h
        self.l = l
        self.win = curses.newwin(winh,winl,h,l)
        self.inside = inside
        self.win.addstr(1,1,inside)
        self.win.box(0,0)
        self.win.refresh()

class Buttons:
    def __init__(self,h,l,winh,winl):
        self.l =l
        self.h =h
        self.sh = winh
        self.winh = 2+(4*3)
        self.winl = curses.COLS - 1
        self.win=curses.newwin(self.winh, self.winl, h*winh, 0)
        self.win.box(0,0)
        self.win.refresh()
        self.winleft = curses.newwin(3,(self.winl/2),self.winh+winh*h-4,1)
        self.winleft.addstr(1,1,"<-")
        self.winleft.box(0,0)
        self.winleft.refresh()
        self.winright = curses.newwin(3,(self.winl/2)-1,self.winh+winh*h-4,(self.winl/2)+1)
        self.winright.addstr(1,1,"->")
        self.winright.box(0,0)
        self.winright.refresh()
        self.page = 0;
        self.buttonwin = []
    def changecolor(self,button):
        for butt in self.buttonwin:
            if butt != button:
                butt.win.addstr(1,1,butt.inside)
                butt.win.refresh()
        button.win.addstr(1,1,button.inside,curses.color_pair(3))
        button.win.refresh()
    def setButtons(self,buttons):
        self.button=buttons
    def refreshButtons(self):
        i=0

        lenn = len(self.button)
        beg = self.page*9
        end = 9+(9*self.page)
        if end > lenn:
            end =lenn
        if beg < 0 or end <= 0:
            beg = 0
            end = 9
            self.page = 0
        for but in self.button[beg:end]:
            self.buttonwin.append(Buttonwin(self.h*self.sh + 1 + ((i/3)*3),1+((i%3)*((self.winl/3)-1)),3, ((self.winl/3)-1),str(but)))
            i=i+1
    def drawButtons(self):
        for but in self.buttonwin:
            but.win.clear()
            but.win.refresh()
        self.buttonwin = []
        self.refreshButtons()
    def checkpoint(self,x,y):
        wy,wx = self.win.getbegyx()
        ly,lx = self.win.getmaxyx()
        if x>wx and wx + lx>x and y>wy and wy + ly>y:
            for button in self.buttonwin:
                bwy,bwx = button.win.getbegyx()
                bly,blx = button.win.getmaxyx()
                if x>bwx and bwx + blx>x and y>bwy and bwy + bly>y:
                    self.changecolor(button)
                    return button.win.instr(1, 1)
        bwy,bwx = self.winleft.getbegyx()
        bly,blx = self.winleft.getmaxyx()
        if x>bwx and bwx + blx>x and y>bwy and bwy + bly>y:
            self.page = self.page-1
            self.drawButtons()
        bwy,bwx = self.winright.getbegyx()
        bly,blx = self.winright.getmaxyx()
        if x>bwx and bwx + blx>x and y>bwy and bwy + bly>y:
            self.page = self.page +1
            self.drawButtons()
        return "0"
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
