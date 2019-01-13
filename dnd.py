from mech import *

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
    def __init__(self,siatka,log,buttons):
        self.siatka = siatka
        self.log = log
        her1 = Bohater("Krasnolud","Barbarzynca",1,18,10,10,14,13,16,"Krutki Luk","Przeszywanica")
        her2 = Bohater("Krasnolud","Barbarzynca",1,18,10,10,14,13,16,"Topor Dworeczny","Plytowa")
        her3 = Bohater("Krasnolud","Barbarzynca",1,18,10,10,14,13,16,"Krutki Luk","Przeszywanica")
        her4 = Bohater("Krasnolud","Barbarzynca",1,18,10,10,14,13,16,"Topor Dworeczny","Plytowa")
        self.tw = Tworzenie(siatka,log)
        her1 = self.tw.stworzBohatera(0,0,her1,"1",1)
        her2 = self.tw.stworzBohatera(0,1,her2,"2",1)
        her3 = self.tw.stworzBohatera(7,9,her3,"3",2)
        her4 = self.tw.stworzBohatera(7,8,her4,"4",2)
        self.Heroes=[her1,her2,her3,her4]
        i=0
        while True:
            itury = i % len(self.Heroes)
            i+=1
            tura = Tura(siatka,log,buttons,self.Heroes[itury])
            tura.ruch()
            tura.standard()
            self.checklife()




stdscr = curses.initscr()
curses.curs_set(0)
curses.mousemask(1)
curses.cbreak()
curses.echo()
try:
    siatka = Siatka(8,10,3,3)
    but = Buttons(8,10,3,3)
    log=Logi(8,10,3,3)
    gra = Gra(siatka,log,but)

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
