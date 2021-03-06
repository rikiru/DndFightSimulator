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
    def __init__(self,dane,x,y,zn,team,inicjatywa):
        self.x=x
        self.y=y
        self.bohater=dane
        self.znaczek = zn
        self.specjalne = []
        self.team = team
        self.bohater['inicjatywa'] += inicjatywa


    def zminejszHP(self,atak):
        self.bohater['HP'] = self.bohater['HP'] - atak
    def zwiekszHP(self,leczenie):
        self.bohater['HP'] = self.bohater['HP'] + leczenie
    def getRuchy(self):
        return self.bohater['actions']
    def toJSON(self):
        data = {}
        data['x'] = self.x
        data['y'] = self.y
        data['bohater'] =self.bohater
        data['specjalne'] = self.specjalne
        data['team'] = self.team
        data['znaczek'] = self.znaczek
        return data



class Tworzenie:
    def __init__(self,siatka,logi):
        self.siatka = siatka
        self.logi = logi
    def stworzBohatera(self,sy,sx,bohater,zn,team):
        inicjatywa = randrange(1,20)
        heros=Hero(bohater,sx,sy,zn,team,inicjatywa)
        self.siatka.create(sy,sx,zn,heros)
        return heros
    def wypiszBohatera(self,sy,sx,bohater,zn,team,inicjatywa):
        heros=Hero(bohater,sx,sy,zn,team,inicjatywa)
        self.siatka.create(sy,sx,zn,heros)
        return heros
    def delHero(self,y,x):
        self.siatka.destroy(y,x)


class Ruch:
    def __init__(self,siatka,logi):
        self.siatka = siatka
        self.logi = logi

    def przesBohatera(self,dy,dx,bohater):
        if odleglosc(bohater.x,bohater.y,dx,dy) <= bohater.bohater['predkosc'] :
            self.siatka.move(bohater.y,bohater.x,dy,dx,bohater.znaczek,bohater)
            bohater.y = dy
            bohater.x = dx
            self.logi.write("Bohater " + bohater.znaczek +" przeszedl na pole (" + str(dx) + "," + str(dy) + ")" )
            return True
        else:
            return False


class Standardowa:
    def __init__(self,siatka,logi):
        self.siatka = siatka
        self.logi = logi
    def atakStandardowy(self,bohatera,bohaterb):
        bron = Bron(bohatera.bohater['bron'])
        if  odleglosc(bohatera.x,bohatera.y,bohaterb.x,bohaterb.y) <= bron['Zasieg'] :
            self.logi.write(str(bohatera.znaczek) + " zaatakowal " + str(bohaterb.znaczek))
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
                    obrazenia = obrazenia * bron['krytyk']['mnoznik']
                    self.logi.write("KRYTYK")
                bohaterb.zminejszHP(obrazenia)
                self.logi.write(bohatera.znaczek + " zadal " + str(obrazenia) + " obrazen " + bohaterb.znaczek)

class Czar:
    def __init__(self,siatka,log):
        self.siatka = siatka
        self.logi=log
    def magicznypocisk(self,bohater):
        obrazenia = randrange(1,4) + 1
        bohater.zminejszHP(obrazenia)
        self.logi.write("Magiczny pocisk zadal " + str(obrazenia) + " obrazen " + bohater.znaczek)
    def leczenielr(self,bohater):
        lecz = randrange(1,6)
        bohater.zwiekszHP(lecz)
        self.logi.write("Lecznie przywrocilo " + str(lecz) + " PW")
    def kulaognia(self,x,y):
        self.logi.write("Rzucono Kule Ognia")
        zasieg = [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]
        for pole in zasieg:
            if pole[1]>=0 and pole[0]>=0 and pole[1]< self.siatka.h and pole[0]<self.siatka.l:
                if self.siatka.win[pole[0]][pole[1]].empty:
                    self.logi.write("Kula Ognia trafila " + self.siatka.win[pole[0]][pole[1]].bohater.znaczek)
                    obrazenia = randrange(1,6)
                    self.siatka.win[pole[0]][pole[1]].bohater.zminejszHP(obrazenia)
                    self.logi.write("Kula Ognia zadala " + str(obrazenia) +" obrazen " +self.siatka.win[pole[0]][pole[1]].bohater.znaczek)
    def silaByka(self,bohater):
        bohater.bohater['atrybuty']['s'] = bohater.bohater['atrybuty']['s'] + 4
        bohater.specjalne.append({"Nazwa":"silaByka","Czas":4})
        self.logi.write("Rzucono Sile Byka na bohatera " + bohater.znaczek)



#
# stdscr = curses.initscr()
# curses.curs_set(0)
# stdscr.keypad(1)
# curses.mousemask(1)
# curses.cbreak()
# curses.echo()
# try:
#     her1 = Bohater("Krasnolud","Barbarzynca",3,18,16,15,14,13,16,"Krutki Luk","Skozana")
#     her2 = Bohater("Krasnolud","Barbarzynca",3,18,16,15,14,13,16,"Topor Dworeczny","Plytowa")
#     siatka = Siatka(4,3,5,7)
#     log = Logi(4,3,5,7)
#     whateba = Tworzenie(siatka,log)
#     heros1 = whateba.stworzBohatera(1,1,her1,"3")
#     heros2 = whateba.stworzBohatera(0,0,her2,"4")
#     whateba = Ruch(siatka,log)
#     cza = Czar(siatka,log)
#     sleep(1)
#     print heros1.bohater,heros2.bohater,"cokolwiek"
#     # whateba.przesBohatera(3,2,heros1)
#     # stanadrd = Standardowa(siatka,log)
#     # stanadrd.atakStandardowy(heros1,heros2)
#     # cza.magicznypocisk(heros2),
#     # cza.leczenielr(heros2),
#     # cza.kulaognia(heros2.x,heros2.y)
#     # sleep(1)
#     # whateba.przesBohatera(3,1,heros2)
#     # stanadrd.atakStandardowy(heros2,heros1)
#     # cza.kulaognia(heros2.x,heros2.y)
#     cza.silaByka(heros1)
#     log.win.keypad(1)
#     event = log.win.getch()
#     if event == curses.KEY_MOUSE:
#         _, mx, my, _, _ = curses.getmouse()
#         log.write(" " + str(mx) + " " + str(my))
#     print heros1.bohater,heros2.bohater
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
