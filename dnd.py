from mech import *
import json
import socket

class Tura:
    def checkSpecjalne(self):
        for spec in self.hero.bohater['specjalne']:
            if spec['Czas'] < 0:
                if spec['Nazwa'] == "silaByka":
                    self.hero.bohater['atrybuty']['s'] = self.hero.bohater['atrybuty']['s'] - 4
            else:
                spec['Czas'] -=1

    def __init__(self,siatka,log,buttons,hero):
        self.buttons = buttons
        self.siatka = siatka
        self.log = log
        self.log.win.keypad(1)
        self.hero = hero
        self.checkSpecjalne()
        self.log.write("Rozpoczyna sie tura " + self.hero.znaczek)

    def getMouse(self):
        event = self.log.win.getch()
        if event == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
            return mx,my

    def ruch(self):
        bytpomin = ["Pomin"]
        but = self.hero.getRuchy()
        self.buttons.setButtons(but['Ruch'] + bytpomin)
        self.buttons.drawButtons()
        check ="0"
        while True:
            mysz = self.getMouse()
            self.checklog(mysz[0],mysz[1])
            if self.checkbuttons(mysz[0],mysz[1]) != "0":
                check = self.checkbuttons(mysz[0],mysz[1])
                if check[:len("Pomin")] == "Pomin":
                    return 1
            if check != "0":
                position = self.checksiatka(mysz[0],mysz[1])
                if position != (-1,-1):
                    ruch = Ruch(self.siatka,self.log)
                    if check[:len("Ruch Standardowy")] == "Ruch Standardowy":
                        if not ruch.przesBohatera(position[0],position[1],self.hero):
                            self.log.write("Za daleko, nie moge sie tam dostac")
                        else:
                            return 1

    def standard(self):
        bytpomin = ["Pomin"]
        but = self.hero.getRuchy()
        butczar = []
        for czar in but['Czar']:
            if czar['Ilosc'] > 0:
                butczar.append(czar['Nazwa'])
        self.buttons.setButtons(but['Standardowa']+butczar + bytpomin)
        self.buttons.drawButtons()
        check = "0"
        while True:
            mysz = self.getMouse()
            self.checklog(mysz[0],mysz[1])
            if self.checkbuttons(mysz[0],mysz[1]) != "0":
                check = self.checkbuttons(mysz[0],mysz[1])
                if check[:len("Pomin")] == "Pomin":
                    return 1
            if check != "0":
                position = self.checksiatka(mysz[0],mysz[1])
                if position != (-1,-1):
                    standard = Standardowa(self.siatka,self.log)
                    czar = Czar(self.siatka,self.log)
                    if check[:len("Atak Standardowy")] == "Atak Standardowy":
                        if self.siatka.win[position[1]][position[0]].empty :
                            standard.atakStandardowy(self.hero,self.siatka.win[position[1]][position[0]].bohater)
                            return 1
                        else:
                            self.log.write("Nie ma przeciewnika na tym polu")
                    if check[:len("Magiczny Pocisk")] == "Magiczny Pocisk":
                        if  self.siatka.win[position[1]][position[0]].empty :
                            czar.magicznypocisk(self.siatka.win[position[1]][position[0]].bohater)
                            for czar in but['Czar']:
                                if czar['Nazwa'] == "Magiczny Pocisk":
                                    czar['Ilosc'] -=1
                            return 1
                        else:
                            self.log.write("Nie ma przeciewnika na tym polu")
                    if check[:len("Kula Ognia")] == "Kula Ognia":
                        czar.kulaognia(position[1],position[0])
                        for czar in but['Czar']:
                            if czar['Nazwa'] == "Kula Ognia":
                                czar['Ilosc'] -=1
                        return 1
                    if check[:len("L Lekkich Ran")] == "L Lekkich Ran":
                        if  self.siatka.win[position[1]][position[0]].empty :
                            czar.leczenielr(self.siatka.win[position[1]][position[0]].bohater)
                            for czar in but['Czar']:
                                if czar['Nazwa'] == "L Lekkich Ran":
                                    czar['Ilosc'] -=1
                            return 1
                        else:
                            self.log.write("Nie ma postaci na tym polu")
                    if check[:len("Siala Byka")] == "Siala Byka":
                        if  self.siatka.win[position[1]][position[0]].empty :
                            czar.silaByka(self.siatka.win[position[1]][position[0]].bohater)
                            for czar in but['Czar']:
                                if czar['Nazwa'] == "Siala Byka":
                                    czar['Ilosc'] -=1
                            return 1
                        else:
                            self.log.write("Nie ma postaci na tym polu")

    def checklog(self,mysz1,mysz2):
        self.log.checkpoint(mysz1,mysz2)
    def checkbuttons(self,mysz1,mysz2):
        return self.buttons.checkpoint(mysz1,mysz2)
    def checksiatka(self,mysz1,mysz2):
        return self.siatka.checkpoint(mysz1,mysz2)



class Gra:
    def invertinicjatywa(self,heroes):
        heroes.bohater['inicjatywa'] = -heroes.bohater['inicjatywa']
    def resetHeroes(self):
        for her in self.Heroes:
            self.invertinicjatywa(her)
    def chosehero(self):
        mininicjatywa = 0
        i = 0
        itury = -1
        for her in self.Heroes:
            if her.bohater['inicjatywa']>mininicjatywa:
                mininicjatywa = her.bohater['inicjatywa']
                itury = i
            i+=1
        if mininicjatywa == 0:
            self.resetHeroes()
        else:
            self.invertinicjatywa(self.Heroes[itury])
        return itury
    def checkteams(self):
        t1=0
        t2=0
        for her in self.Heroes:
            if her.team ==1:
                t1 += 1
            if  her.team ==2:
                t2 +=1
        if t1 == 0:
            return True,"Wygrala druzyna 2"
        elif t2 == 0:
            return True,"Wygrala druzyna 1"
        else:
            return False,"Jeszcze nikt nie wygral"
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
            her = Bohater(heroes['race'],heroes['class'],heroes['lvl'],heroes['s'],heroes['z'],heroes['b'],heroes['i'],heroes['m'],heroes['c'],heroes['weapon'],heroes['armor'],heroes['actions'])
            self.Heroes.append(self.tw.stworzBohatera(heroes['locatios']['x'],heroes['locatios']['y'],her,heroes['char'],1))
        for heroes in config['team2']:
            her = Bohater(heroes['race'],heroes['class'],heroes['lvl'],heroes['s'],heroes['z'],heroes['b'],heroes['i'],heroes['m'],heroes['c'],heroes['weapon'],heroes['armor'],heroes['actions'])
            hero = self.tw.stworzBohatera(heroes['locatios']['x'],heroes['locatios']['y'],her,heroes['char'],2)
            self.Heroes.append(hero)
        i=0
        while True:
            clog = len(log.tekst)
            itury = self.chosehero()
            if itury == -1:
                itury = self.chosehero()
            i+=1
            tura = Tura(siatka,log,but,self.Heroes[itury])
            tura.ruch()
            tura.standard()
            self.checklife()
            czykoniec,tekstkoncowy = self.checkteams()
            if czykoniec:
                break
        print tekstkoncowy + " po " + str(i) + " akcjach"

class GraSerwer:
    def invertinicjatywa(self,heroes):
        heroes.bohater['inicjatywa'] = -heroes.bohater['inicjatywa']
    def resetHeroes(self):
        for her in self.Heroes:
            self.invertinicjatywa(her)
    def chosehero(self):
        mininicjatywa = 0
        i = 0
        itury = -1
        for her in self.Heroes:
            if her.bohater['inicjatywa']>mininicjatywa:
                mininicjatywa = her.bohater['inicjatywa']
                itury = i
            i+=1
        if mininicjatywa == 0:
            self.resetHeroes()
        else:
            self.invertinicjatywa(self.Heroes[itury])
        return itury
    def checkteams(self):
        t1=0
        t2=0
        for her in self.Heroes:
            if her.team ==1:
                t1 += 1
            if  her.team ==2:
                t2 +=1
        if t1 == 0:
            return True,"Wygrala druzyna 2"
        elif t2 == 0:
            return True,"Wygrala druzyna 1"
        else:
            return False,"Jeszcze nikt nie wygral"
    def checklife(self):
        for her in self.Heroes:
            if her.bohater['HP'] <=0 :
                self.tw.delHero(her.y,her.x)
                self.Heroes.remove(her)
    def __init__(self):
        TCP_IP = '127.0.0.1'
        TCP_PORT = 5005
        BUFFER_SIZE = 4096
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
            her = Bohater(heroes['race'],heroes['class'],heroes['lvl'],heroes['s'],heroes['z'],heroes['b'],heroes['i'],heroes['m'],heroes['c'],heroes['weapon'],heroes['armor'],heroes['actions'])
            self.Heroes.append(self.tw.stworzBohatera(heroes['locatios']['x'],heroes['locatios']['y'],her,heroes['char'],1))
        for heroes in config['team2']:
            her = Bohater(heroes['race'],heroes['class'],heroes['lvl'],heroes['s'],heroes['z'],heroes['b'],heroes['i'],heroes['m'],heroes['c'],heroes['weapon'],heroes['armor'],heroes['actions'])
            hero = self.tw.stworzBohatera(heroes['locatios']['x'],heroes['locatios']['y'],her,heroes['char'],2)
            self.Heroes.append(hero)
        dataHero={}
        dataHero['heroes'] = []
        for hero in self.Heroes:
            dataHero['heroes'].append(hero.toJSON())
        conn.send(json.dumps(dataHero))
        i=0
        while True:
            czykoniec,tekstkoncowy = self.checkteams()
            if czykoniec:
                break
            itury = self.chosehero()
            if itury == -1:
                itury = self.chosehero()
            i+=1
            if(self.Heroes[itury].team == 1):
                daneruch={}
                clog = len(log.tekst)
                tura = Tura(siatka,log,but,self.Heroes[itury])
                tura.ruch()
                tura.standard()
                self.checklife()
                cnlog = len(log.tekst)
                dataLog = log.tekst[clog:cnlog]
                dataHero=[]
                for hero in self.Heroes:
                    dataHero.append(hero.toJSON())
                dane = {}
                dane['log'] = dataLog
                dane['hero'] = dataHero
                dane = json.dumps(dane)
                conn.send(dane)
            else:
                data = conn.recv(BUFFER_SIZE)
                dane = json.loads(data)
                for tekst in dane['log']:
                    log.write(tekst)
                for hero in self.Heroes:
                    self.tw.delHero(hero.y,hero.x)
                self.Heroes = []
                for hero in dane['hero']:
                    heros = self.tw.wypiszBohatera(hero['y'],hero['x'],hero['bohater'],hero['znaczek'],hero['team'],hero['bohater']['inicjatywa'])
                    self.Heroes.append(heros)
        print tekstkoncowy + " po " + str(i) + " akcjach"



class GraClient:
    def invertinicjatywa(self,heroes):
        print type(heroes.bohater['inicjatywa']),heroes.bohater['inicjatywa']
        heroes.bohater['inicjatywa'] = -heroes.bohater['inicjatywa']
    def resetHeroes(self):
        for her in self.Heroes:
            self.invertinicjatywa(her)
    def chosehero(self):
        mininicjatywa = 0
        i = 0
        itury = -1
        for her in self.Heroes:
            if her.bohater['inicjatywa']>mininicjatywa:
                mininicjatywa = her.bohater['inicjatywa']
                itury = i
            i+=1
        if mininicjatywa == 0:
            self.resetHeroes()
        else:
            self.invertinicjatywa(self.Heroes[itury])
        return itury
    def checkteams(self):
        t1=0
        t2=0
        for her in self.Heroes:
            if her.team ==1:
                t1 += 1
            if  her.team ==2:
                t2 +=1
        if t1 == 0:
            return True,"Wygrala druzyna 2"
        elif t2 == 0:
            return True,"Wygrala druzyna 1"
        else:
            return False,"Jeszcze nikt nie wygral"
    def checklife(self):
        for her in self.Heroes:
            if her.bohater['HP'] <=0 :
                self.tw.delHero(her.y,her.x)
                self.Heroes.remove(her)
    def __init__(self):
        TCP_IP = '127.0.0.1'
        TCP_PORT = 5005
        BUFFER_SIZE = 4096
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
            print hero
            heros = self.tw.wypiszBohatera(hero['y'],hero['x'],hero['bohater'],hero['znaczek'],hero['team'],hero['bohater']['inicjatywa'])
            self.Heroes.append(heros)
        i=0
        while True:
            czykoniec,tekstkoncowy = self.checkteams()
            if czykoniec:
                break
            itury = self.chosehero()
            if itury == -1:
                itury = self.chosehero()
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
                dataLog = log.tekst[clog:cnlog]
                dataHero=[]
                for hero in self.Heroes:
                    dataHero.append(hero.toJSON())
                dane = {}
                dane['log'] = dataLog
                dane['hero'] = dataHero
                dane = json.dumps(dane)
                s.send(dane)
            else:
                data = s.recv(BUFFER_SIZE)
                dane = json.loads(data)
                for tekst in dane['log']:
                    log.write(tekst)
                for hero in self.Heroes:
                    self.tw.delHero(hero.y,hero.x)
                self.Heroes = []
                for hero in dane['hero']:
                    heros = self.tw.wypiszBohatera(hero['y'],hero['x'],hero['bohater'],hero['znaczek'],hero['team'],hero['bohater']['inicjatywa'])
                    self.Heroes.append(heros)
        print tekstkoncowy + " po " + str(i) + " akcjach"





# stdscr = curses.initscr()
# curses.curs_set(0)
# curses.mousemask(1)
# curses.cbreak()
# curses.echo()
# try:
#     curses.start_color()
#     gra = Gra()
#     curses.endwin()
#     exit(0)
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
