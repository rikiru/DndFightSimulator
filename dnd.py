from mech import *
import json
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024




class Tura:
    def __init__(self,siatka,log,buttons,hero):
        self.buttons = buttons
        self.siatka = siatka
        self.log = log
        self.log.win.keypad(1)
        self.hero = hero
    def getMouse(self):
        event = self.log.win.getch()
        if event == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
            return mx,my
    def ruch(self):
        but = self.hero.getRuchy()
        self.buttons.setButtons(but['Ruch'])
        self.buttons.drawButtons()
        check = "0"
        while check == "0":
            mysz = self.getMouse()
            check = self.buttons.checkpoint(mysz[0],mysz[1])
            self.checklog(mysz[0],mysz[1])
            self.log.write(check)
            position = [-1,-1]
        while position == [-1,-1]:
            mysz = self.getMouse()
            position = self.siatka.checkpoint(mysz[0],mysz[1])
            self.checklog(mysz[0],mysz[1])
            self.log.write(str(position))
        ruch = Ruch(self.siatka,self.log)
        if check[:len("Ruch Standardowy")] == "Ruch Standardowy":
            ruch.przesBohatera(position[0],position[1],self.hero)

    def standard(self):
        but = self.hero.getRuchy()
        self.buttons.setButtons(but['Standardowa'])
        self.buttons.drawButtons()
        check = "0"
        while check == "0":
            mysz = self.getMouse()
            check = self.buttons.checkpoint(mysz[0],mysz[1])
            self.checklog(mysz[0],mysz[1])
            self.log.write(check)
        position = [-1,-1]
        while position == [-1,-1]:
            mysz = self.getMouse()
            position = self.siatka.checkpoint(mysz[0],mysz[1])
            self.checklog(mysz[0],mysz[1])
            self.log.write(str(position))
            standard = Standardowa(self.siatka,self.log)
        if check[:len("Atak Standardowy")] == "Atak Standardowy":
            standard.atakStandardowy(self.hero,self.siatka.win[position[1]][position[0]].bohater)

    def checklog(self,mysz1,mysz2):
        log=self.log.checkpoint(mysz1,mysz2)



class Gra:
    def checklife(self):
        for her in self.Heroes:
            if her.bohater['HP'] <=0 :
                self.tw.delHero(her.y,her.x)
                self.Heroes.remove(her)
    def __init__(self):
        self.Heroes=[]
        config = open("config.json").read()
        config = json.loads(config)
        siatka = Siatka(config['map']['xlength'],config['map']['ylength'],config['map']['xsize'],config['map']['ysize'])
        but = Buttons(config['map']['xlength'],config['map']['ylength'],config['map']['xsize'],config['map']['ysize'])
        log=Logi(config['map']['xlength'],config['map']['ylength'],config['map']['xsize'],config['map']['ysize'])
        self.tw = Tworzenie(siatka,log)
        for heroes in config['team1']:
            her = Bohater(heroes['race'],heroes['class'],heroes['lvl'],heroes['s'],heroes['z'],heroes['b'],heroes['i'],heroes['m'],heroes['c'],heroes['weapon'],heroes['armor'])
            self.Heroes.append(self.tw.stworzBohatera(heroes['locatios']['x'],heroes['locatios']['y'],her,heroes['char'],1))
        for heroes in config['team2']:
            her = Bohater(heroes['race'],heroes['class'],heroes['lvl'],heroes['s'],heroes['z'],heroes['b'],heroes['i'],heroes['m'],heroes['c'],heroes['weapon'],heroes['armor'])
            hero = self.tw.stworzBohatera(heroes['locatios']['x'],heroes['locatios']['y'],her,heroes['char'],2)
            self.Heroes.append(hero)
        i=0
        while True:
            clog = len(log.tekst)
            itury = i % len(self.Heroes)
            i+=1
            tura = Tura(siatka,log,but,self.Heroes[itury])
            tura.ruch()
            tura.standard()
            self.checklife()

class GraSerwer:
    def checklife(self):
        for her in self.Heroes:
            if her.bohater['HP'] <=0 :
                self.tw.delHero(her.y,her.x)
                self.Heroes.remove(her)
    def __init__(self):
        self.Heroes=[]
        config = open("config.json").read()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP, TCP_PORT))
        s.listen(1)
        conn, addr = s.accept()
        conn.send(config)
        config = json.loads(config)
        siatka = Siatka(config['map']['xlength'],config['map']['ylength'],config['map']['xsize'],config['map']['ysize'])
        but = Buttons(config['map']['xlength'],config['map']['ylength'],config['map']['xsize'],config['map']['ysize'])
        log=Logi(config['map']['xlength'],config['map']['ylength'],config['map']['xsize'],config['map']['ysize'])
        self.tw = Tworzenie(siatka,log)
        for heroes in config['team1']:
            her = Bohater(heroes['race'],heroes['class'],heroes['lvl'],heroes['s'],heroes['z'],heroes['b'],heroes['i'],heroes['m'],heroes['c'],heroes['weapon'],heroes['armor'])
            self.Heroes.append(self.tw.stworzBohatera(heroes['locatios']['x'],heroes['locatios']['y'],her,heroes['char'],1))
        for heroes in config['team2']:
            her = Bohater(heroes['race'],heroes['class'],heroes['lvl'],heroes['s'],heroes['z'],heroes['b'],heroes['i'],heroes['m'],heroes['c'],heroes['weapon'],heroes['armor'])
            hero = self.tw.stworzBohatera(heroes['locatios']['x'],heroes['locatios']['y'],her,heroes['char'],2)
            self.Heroes.append(hero)
        dataHero={}
        dataHero['heroes'] = []
        for hero in self.Heroes:
            dataHero['heroes'].append(hero.toJSON())
        conn.send(json.dumps(dataHero))
        i=0
        while True:
            itury = i % len(self.Heroes)
            i+=1
            if(self.Heroes[itury].team == 1):
                daneruch={}
                clog = len(log.tekst)
                tura = Tura(siatka,log,but,self.Heroes[itury])
                daneruch['xs'] =self.Heroes[itury].x
                daneruch['ys'] =self.Heroes[itury].y
                tura.ruch()
                daneruch['xd'] =self.Heroes[itury].x
                daneruch['yd'] =self.Heroes[itury].y
                tura.standard()
                self.checklife()
                cnlog = len(log.tekst)
                dataLog = log.tekst[clog:cnlog-1]
                dataHero=[]
                for hero in self.Heroes:
                    dataHero.append(hero.toJSON())
                dane = {}
                dane['log'] = dataLog
                dane['ruch'] = daneruch
                dane['hero'] = dataHero
                dane = json.dumps(dane)
                conn.send(dane)
            else:
                data = conn.recv(BUFFER_SIZE)
                dane = json.loads(data)
                siatka.move(dane['ruch']['ys'],dane['ruch']['xs'],dane['ruch']['yd'],dane['ruch']['xd'],self.Heroes[itury].znaczek,self.Heroes[itury])
                for tekst in dane['log']:
                    log.write(tekst)
                for hero in self.Heroes:
                    self.tw.delHero(hero.y,hero.x)
                self.Heroes = []
                for hero in dane['hero']:
                    heros = self.tw.wypiszBohatera(hero['y'],hero['x'],hero['bohater'],hero['znaczek'],hero['team'],['inicjatywa'])
                    self.Heroes.append(heros)


class GraClient:
    def checklife(self):
        for her in self.Heroes:
            if her.bohater['HP'] <=0 :
                self.tw.delHero(her.y,her.x)
                self.Heroes.remove(her)
    def __init__(self):
        self.Heroes=[]
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        config =  s.recv(BUFFER_SIZE)
        config = json.loads(config)
        siatka = Siatka(config['map']['xlength'],config['map']['ylength'],config['map']['xsize'],config['map']['ysize'])
        but = Buttons(config['map']['xlength'],config['map']['ylength'],config['map']['xsize'],config['map']['ysize'])
        log=Logi(config['map']['xlength'],config['map']['ylength'],config['map']['xsize'],config['map']['ysize'])
        self.tw = Tworzenie(siatka,log)
        heroes =  s.recv(BUFFER_SIZE)
        heroes = json.loads(heroes)
        for hero in heroes['heroes']:
            heros = self.tw.wypiszBohatera(hero['y'],hero['x'],hero['bohater'],hero['znaczek'],hero['team'],['inicjatywa'])
            self.Heroes.append(heros)
        i=0
        while True:
            itury = i % len(self.Heroes)
            i+=1
            if(self.Heroes[itury].team == 2):
                daneruch={}
                clog = len(log.tekst)
                tura = Tura(siatka,log,but,self.Heroes[itury])
                daneruch['xs'] =self.Heroes[itury].x
                daneruch['ys'] =self.Heroes[itury].y
                tura.ruch()
                daneruch['xd'] =self.Heroes[itury].x
                daneruch['yd'] =self.Heroes[itury].y
                tura.standard()
                self.checklife()
                cnlog = len(log.tekst)
                dataLog = log.tekst[clog:cnlog-1]
                dataHero=[]
                for hero in self.Heroes:
                    dataHero.append(hero.toJSON())
                dane = {}
                dane['log'] = dataLog
                dane['ruch'] = daneruch
                dane['hero'] = dataHero
                dane = json.dumps(dane)
                print dane
                s.send(dane)
            else:
                data = s.recv(BUFFER_SIZE)
                dane = json.loads(data)
                siatka.move(dane['ruch']['ys'],dane['ruch']['xs'],dane['ruch']['yd'],dane['ruch']['xd'],self.Heroes[itury].znaczek,self.Heroes[itury])
                for tekst in dane['log']:
                    log.write(tekst)
                for hero in self.Heroes:
                    self.tw.delHero(hero.y,hero.x)
                self.Heroes = []
                for hero in dane['hero']:
                    heros = self.tw.wypiszBohatera(hero['y'],hero['x'],hero['bohater'],hero['znaczek'],hero['team'],['inicjatywa'])
                    self.Heroes.append(heros)






# stdscr = curses.initscr()
# curses.curs_set(0)
# curses.mousemask(1)
# curses.cbreak()
# curses.echo()
# try:
#     gra = Gra()
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
