import curses
from cur import *
from hero import Bohater,Modyfikator
from ekwipunek import Bron,Zbroja
from random import randrange

def odleglosc(ax,ay,bx,by):
    odleglosc = -1
    if ax == bx or ay == by :
        odleglosc = abs(ay - by) + abs(ax - bx)
        odleglosc = odleglosc * 1.5
    else:
        odx = abs(ax - bx)
        ody = abs(ay - by)
        skos = min(odx,ody)
        odx=odx-skos
        ody=ody-skos
        odleglosc = 0
        for i in range(1,skos+1):
            if i%2 ==0:
                odleglosc = odleglosc + 3
            else:
                odleglosc = odleglosc + 1.5
        odleglosc = odleglosc + (1.5*(odx+ody))
    return odleglosc


class Hero:
    def __init__(self,dane,x,y,zn):
        self.x=x
        self.y=y
        self.bohater=dane
        self.znaczek = zn
        self.specjalne = []

    def zminejszHP(self,atak):
        self.bohater['HP'] = self.bohater['HP'] - atak
    def zwiekszHP(self,leczenie):
        self.bohater['HP'] = self.bohater['HP'] + leczenie


class Tworzenie:
    def __init__(self,siatka,logi):
        self.siatka = siatka
        self.logi = logi
    def stworzBohatera(self,sy,sx,bohater,zn):
        heros=Hero(bohater,sx,sy,zn)
        self.siatka.create(sy,sx,zn,heros)
        self.logi.write("stworzono")
        return heros


class Ruch:
    def __init__(self,siatka,logi):
        self.siatka = siatka
        self.logi = logi

    def przesBohatera(self,dy,dx,bohater):
        self.siatka.move(bohater.y,bohater.x,dy,dx,bohater.znaczek,bohater)
        bohater.y = dy
        bohater.x = dx


class Standardowa:
    def __init__(self,siatka,logi):
        self.siatka = siatka
        self.logi = logi
    def atakStandardowy(self,bohatera,bohaterb):
        bron = Bron(bohatera.bohater['bron'])
        print odleglosc(bohatera.x,bohatera.y,bohaterb.x,bohaterb.y)
        print bron['Zasieg']
        if  odleglosc(bohatera.x,bohatera.y,bohaterb.x,bohaterb.y) <= bron['Zasieg'] :
            self.logi.write("boatera zaatakowal bohaterb")
            kosc = randrange(1,20)
            self.logi.write(str(kosc) + " + " + str(Modyfikator(bohatera.bohater['atrybuty'][bron['Bouns']]))+ " = " + str(kosc+ Modyfikator(bohatera.bohater['atrybuty'][bron['Bouns']])) + "| kontra " + str(bohaterb.bohater['KP']))
            if kosc + Modyfikator(bohatera.bohater['atrybuty'][bron['Bouns']]) >= bohaterb.bohater['KP']:
                obrazenia = 0
                for j in range(0,bohatera.bohater['iloscAtakow']):
                    for i in range(0,bron['Obrazenia']['Ilosc']):
                        obrazenia = obrazenia + randrange(1,bron['Obrazenia']['Kosc'])
                if bron['Bouns'] == 's':
                    obrazenia = obrazenia + Modyfikator(bohatera.bohater['atrybuty']['s'])
                if bron['krytyk']['wynik'] <= kosc:
                    print kosc
                    obrazenia = obrazenia * bron['krytyk']['mnoznik']
                    self.logi.write("KRYTYK")
                bohaterb.zminejszHP(obrazenia)
                self.logi.write("boatera zadal " + str(obrazenia) + " bohaterb")

class Czar:
    def __init__(self,siatka,log):
        self.siatka = siatka
        self.logi=log
    def magicznypocisk(self,bohater):
        obrazenia = randrange(1,4) + 1
        bohater.zminejszHP(obrazenia)
        self.logi.write("magicznypocisk zadal " + str(obrazenia))
    def leczenielr(self,bohater):
        lecz = randrange(1,6)
        bohater.zwiekszHP(lecz)
        self.logi.write("lecznie przywrocilo " + str(lecz))
    def kulaognia(self,x,y):
        self.logi.write("rzucono kule ognia")
        print x,y
        zasieg = [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]
        for pole in zasieg:
            if pole[1]>=0 and pole[0]>=0 and pole[1]< self.siatka.h and pole[0]<self.siatka.l:
                if self.siatka.win[pole[0]][pole[1]].empty:
                    self.logi.write("kula trafila" + self.siatka.win[pole[0]][pole[1]].bohater.znaczek)
                    obrazenia = randrange(1,6)
                    self.siatka.win[pole[0]][pole[1]].bohater.zminejszHP(obrazenia)
                    self.logi.write("kula ogania zadala " + str(obrazenia) +" " +self.siatka.win[pole[0]][pole[1]].bohater.znaczek)
    def silaByka(self,bohater):
        bohater.bohater['atrybuty']['s'] = bohater.bohater['atrybuty']['s'] + 4
        bohater.specjalne.append({"Nazwa":"silaByka","Czas":4})
        self.logi.write("silaByka")




stdscr = curses.initscr()

curses.cbreak()
curses.echo()
try:
    her1 = Bohater("Krasnolud","Barbarzynca",3,18,16,15,14,13,16,"Krutki Luk","Skozana")
    her2 = Bohater("Krasnolud","Barbarzynca",3,18,16,15,14,13,16,"Topor Dworeczny","Plytowa")
    siatka = Siatka(4,3,5,7)
    log = Logi(4,3,5,7)
    whateba = Tworzenie(siatka,log)
    heros1 = whateba.stworzBohatera(1,1,her1,"3")
    heros2 = whateba.stworzBohatera(0,0,her2,"4")
    whateba = Ruch(siatka,log)
    cza = Czar(siatka,log)
    sleep(1)
    print heros1.bohater,heros2.bohater,"cokolwiek"
    # whateba.przesBohatera(3,2,heros1)
    # stanadrd = Standardowa(siatka,log)
    # stanadrd.atakStandardowy(heros1,heros2)
    # cza.magicznypocisk(heros2),
    # cza.leczenielr(heros2),
    # cza.kulaognia(heros2.x,heros2.y)
    # sleep(1)
    # whateba.przesBohatera(3,1,heros2)
    # stanadrd.atakStandardowy(heros2,heros1)
    # cza.kulaognia(heros2.x,heros2.y)
    cza.silaByka(heros1)
    curses.getmouse()
    print heros1.bohater,heros2.bohater

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
