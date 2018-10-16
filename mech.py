from cur import *
from hero import Bohater

class tworzenie:
    def __init__(self,siatka,logi):
        self.siatka = siatka
        self.logi = logi
    def stworzBohatera(self,sy,sx,bohater):
        self.siatka.create(sy,sx,"7",bohater)
        self.logi.write(str(bohater))

class ruch:
    def __init__(self,siatka,logi):
        self.siatka = siatka
        self.logi = logi
    def przesBohatera(self,sy,sx,dy,dx,bohater):
        self.siatka.move(sy,sx,dy,dx,"7",bohater)

class standardowa:
    def __init__(self,siatka,logi):
        self.siatka = siatka
        self.logi = logi
    def atakStandardowy(self,ya,xa,yb,xb):


class calorundowa:
    def __init__(self,siatka,logi):
        self.siatka = siatka
        self.logi = logi

stdscr = curses.initscr()

curses.cbreak()
curses.echo()
try:
    hero = Bohater("Krasnolud","Barbarzynca",3,18,16,15,14,13,16,"Topor Dworeczny","Plytowa")
    siatka = Siatka(4,3,5,7)
    log = Logi(4,3,5,7)
    whateba = tworzenie(siatka,log)
    whateba.stworzBohatera(1,1,hero)
    whateba = ruch(siatka,log)
    sleep(1)
    whateba.przesBohatera(1,1,0,1,hero)
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


# def stworzBohatera(siatka,logi,sy,sx,bohater):
#     json = {
#     "akcja" : "tworzenie",
#     "wykonaj" :[siatka.create(sy, sx,"7",bohater),logi.write(str(bohater))]
#     }
#     return json
# stdscr = curses.initscr()
#
# curses.cbreak()
# curses.echo()
# try:
#     hero = Bohater("Krasnolud","Barbarzynca",3,18,16,15,14,13,16,"Topor Dworeczny","Plytowa")
#     siatka = Siatka(4,3,5,7)
#     log = Logi(4,3,5,7)
#     whateba = stworzBohatera(siatka,log,0,0,hero)
#
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
#
