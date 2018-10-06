# -*- coding: utf-8 -*-
def getKlasy():
    return ["Barbarzyńca","Bard","Czarodziej","Druid","Kapłan","Łotrzyk","Mnich","Palladyn","Tropiciel","Wojownik","Zaklinacz"]

def RO(lvl,main):
    if main:
        return 2+lvl/2
    else:
        return 0+lvl/3
def Modyfikator(wartosc):
    return (wartosc-10)/2
def hp(kosc,lvl):
    if lvl == 1:
        return kosc
    else:
        points = kosc
        for i in range(kosc-1):
            points = points + random.randint(1,kosc)

class Atrybuty:
    def __init__(self,s,z,b,i,m,c):
        self.s=s
        self.z=z
        self.b=b
        self.i=i
        self.m=m
        self.c=c

class Wartosci:
    def __init__(self,klasa,lvl,b,z,m):
        if klasa == "Barbarzyńca":
            self.hp = (12,lvl)
            self.wytrwalosc=RO(lvl,True)
            self.refleks=RO(lvl,False)
            self.wola=RO(lvl,False)
        if klasa == "Bard":
            self.wytrwalosc=RO(lvl,False)
            self.refleks=RO(lvl,True)
            self.wola=RO(lvl,True)
        if klasa == "Czarodziej":
            self.wytrwalosc=RO(lvl,False)
            self.refleks=RO(lvl,False)
            self.wola=RO(lvl,True)
        if klasa == "Druid":
            self.wytrwalosc=RO(lvl,True)
            self.refleks=RO(lvl,False)
            self.wola=RO(lvl,True)
        if klasa == "Kapłan":
            self.wytrwalosc=RO(lvl,True)
            self.refleks=RO(lvl,False)
            self.wola=RO(lvl,True)
        if klasa == "Łotrzyk":
            self.wytrwalosc=RO(lvl,True)
            self.refleks=RO(lvl,False)
            self.wola=RO(lvl,False)
        if klasa == "Mnich":
            self.wytrwalosc=RO(lvl,True)
            self.refleks=RO(lvl,True)
            self.wola=RO(lvl,True)
        if klasa == "Palladyn":
            self.wytrwalosc=RO(lvl,True)
            self.refleks=RO(lvl,False)
            self.wola=RO(lvl,False)
        if klasa == "Tropiciel":
            self.wytrwalosc=RO(lvl,True)
            self.refleks=RO(lvl,True)
            self.wola=RO(lvl,False)
        if klasa == "Wojownik":
            self.wytrwalosc=RO(lvl,True)
            self.refleks=RO(lvl,False)
            self.wola=RO(lvl,False)
        if klasa == "Zaklinacz":
            self.wytrwalosc=RO(lvl,False)
            self.refleks=RO(lvl,False)
            self.wola=RO(lvl,True)
        self.wytrwalosc=self.wytrwalosc+Modyfikator(b)
        self.refleks=self.refleks+Modyfikator(z)
        self.wola=self.wola+Modyfikator(m)

class Bohater:
    def __init__(self,klasa,lvl,s,z,b,i,m,c):
        self.atrybuty=Atrybuty(s,z,b,i,m,c)
        self.wartosci=Wartosci(klasa,lvl,b,z,m)
    def __str__(self):
        return  "Atrybuty = " + str(self.atrybuty.s) +" "+str(self.atrybuty.z) +" "+ str(self.atrybuty.b) +" "+str(self.atrybuty.i) +" "+str(self.atrybuty.m) +" "+ str(self.atrybuty.c)  +  "  Rzuty Obronne ="  +" "+ str(self.wartosci.wytrwalosc) +" "+str(self.wartosci.refleks) +" "+ str(self.wartosci.wola)

hero = Bohater("Barbarzyńca",3,18,16,15,14,13,16)
