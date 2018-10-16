# -*- coding: utf-8 -*-
from classes import Klasa
from ekwipunek import Bron,Zbroja
from rasy import Rasa
from random import randrange
from math import ceil

def RO(lvl,main):
    if main:
        return 2+lvl/2
    else:
        return 0+lvl/3
def Modyfikator(wartosc):
    return (wartosc-10)/2
def HP(kosc,lvl):
    if lvl == 1:
        return kosc
    else:
        points = kosc
        for i in range(lvl-1):
            points = points + randrange(1,kosc)
        return points

def BA(lvl,umiejetnosci):
    if umiejetnosci == 0 :
        return lvl/2
    if umiejetnosci == 1:
        return lvl*2/3
    if umiejetnosci  == 2:
        return lvl

def iloscAtakow(ba):
    return int(ceil(ba/5.0))

def Bohater(rasa,klasa,lvl,s,z,b,i,m,c,bron,zbroja):
        bklasa = Klasa(klasa)
        bzbroja = Zbroja(zbroja)
        brasa = Rasa(rasa)
        bazowyAtak = BA(lvl,bklasa["premiaDoAtaku"])
        kp  = 10 + bzbroja['Bonus']
        if Modyfikator(z) < bzbroja['Maxzr']:
            kp = kp + Modyfikator(z)
        else:
            kp = kp + bzbroja['Maxzr']

        json ={
        "atrybuty":{
        "s":s,
        "z":z,
        "b":b,
        "i":i,
        "m":m,
        "c":c
        },
        "wytrwalosc" :  RO(lvl,bklasa["Wytrwalosc"]) + Modyfikator(b),
        "refleks" : RO(lvl,bklasa["Refleks"]) + Modyfikator(z),
        "wola" : RO(lvl,bklasa["Wola"]) + Modyfikator(m),
        "bazowyAtak" : bazowyAtak,
        "zwarcie": Modyfikator(s) + bazowyAtak,
        "iloscAtakow" : iloscAtakow(bazowyAtak),
        "bron" : bron,
        "inicjatywa" : Modyfikator(z),
        "HP" : HP(bklasa["kw"],lvl),
        "KP" : kp
        }
        for i in brasa['Plusy']:
            json['atrybuty'][i] +=2
        for i in brasa['Minusy']:
            json['atrybuty'][i] -=2
        return json
        # self.atrybuty=Atrybuty(s,z,b,i,m,c)
        # self.wytrwalosc = RO(lvl,bklasa["Wytrwalosc"]) + Modyfikator(b)
        # self.refleks = RO(lvl,bklasa["Refleks"]) + Modyfikator(z)
        # self.wola = RO(lvl,bklasa["Wola"]) + Modyfikator(m)
        # self.bazowyAtak = BA(lvl,bklasa["premiaDoAtaku"])
        # self.atak = bbron['Nazwa'] + " " + str(bbron['Obrazenia']['Ilosc']) + "k" + str(bbron['Obrazenia']['Kosc'])
        # self.iloscAtakow = iloscAtakow(self.bazowyAtak)
        # self.hp = HP(bklasa["kw"],lvl)
        # self.zwarcie = self.bazowyAtak + Modyfikator(s)
        # self.inicjatywa = Modyfikator(z)
        # self.kp  = 10 + bzbroja['Bonus']
        # if Modyfikator(z) < bzbroja['Maxzr']:
        #     self.kp = self.kp + Modyfikator(z)
        # else:
        #     self.kp = self.kp + bzbroja['Maxzr']
    #
    # def __str__(self):
    #         return  "Atrybuty = " + str(self.atrybuty.s) +" "+str(self.atrybuty.z) +" "+ str(self.atrybuty.b) +" "+str(self.atrybuty.i) +" "+str(self.atrybuty.m) +" "+ str(self.atrybuty.c)  +  "  Rzuty Obronne ="  +" "+ str(self.wytrwalosc) +" "+str(self.refleks) +" "+ str(self.wola)+" Bazowy Atak : " + str(self.bazowyAtak) + " Ilosc Atakow : " + str(self.iloscAtakow) + " HP : " +str(self.hp)+ " KP : " +str(self.kp) + " Atak : " + self.atak
