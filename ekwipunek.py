def mieczdl():
    json = {
    "Nazwa":"Dlugi Miecz",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":8,
    },
    "type":"Zolnierska",
    "krytyk":{
    "mnoznik":2,
    "wynik":19
    },
    "Zasieg":1.5
    }
    return json
def mieczk():
    json = {
    "Nazwa":"Krotki Miecz",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":6,
    },
    "type":"Zolnierska",
    "krytyk":{
    "mnoznik":2,
    "wynik":19
    },
    "Zasieg":1.5
    }
    return json
def buzdyganlekki():
    json = {
    "Nazwa":"Lekki Buzdygan",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":6,
    },
    "type":"Prosta",
    "krytyk":{
    "mnoznik":2,
    "wynik":20
    },
    "Zasieg":1.5
    }
    return json
def sztylet():
    json = {
    "Nazwa":"Sztylet",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":4,
    },
    "type":"Prosta",
    "krytyk":{
    "mnoznik":2,
    "wynik":19
    },
    "Zasieg":1.5
    }
    return json
def wloczniak():
    json = {
    "Nazwa":"Krotka Wlucznia",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":6,
    },
    "type":"Prosta",
    "krytyk":{
    "mnoznik":2,
    "wynik":20
    },
    "Zasieg":1.5
    }
    return json
def maczuga():
    json = {
    "Nazwa":"Maczuga",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":6,
    },
    "type":"Zolnierska",
    "krytyk":{
    "mnoznik":2,
    "wynik":20
    },
    "Zasieg":1.5
    }
    return json
def wlucznia():
    json = {
    "Nazwa":"Wlucznia",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":8,
    },
    "type":"Prosta",
    "krytyk":{
    "mnoznik":3,
    "wynik":20
    },
    "Zasieg":3
    }
    return json
def kuszal():
    json = {
    "Nazwa":"Lekka Kusza",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":8,
    },
    "type":"Prosta",
    "krytyk":{
    "mnoznik":2,
    "wynik":19
    },
    "Zasieg":24
    }
    return json
def toporek():
    json = {
    "Nazwa":"Toporek",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":6,
    },
    "type":"Zolnierska",
    "krytyk":{
    "mnoznik":3,
    "wynik":20
    },
    "Zasieg":1.5
    }
    return json
def mlotbojowy():
    json = {
    "Nazwa":"Mlot Bojowy",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":8,
    },
    "type":"Zolnierska",
    "krytyk":{
    "mnoznik":3,
    "wynik":20
    },
    "Zasieg":1.5
    }
    return json
def sejmitar():
    json = {
    "Nazwa":"Sejmitar",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":6,
    },
    "type":"Zolnierska",
    "krytyk":{
    "mnoznik":2,
    "wynik":18
    },
    "Zasieg":1.5
    }
    return json
def toporwojenny():
    json = {
    "Nazwa":"Topor Wojenny",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":8,
    },
    "type":"Zolnierska",
    "krytyk":{
    "mnoznik":3,
    "wynik":20
    },
    "Zasieg":1.5
    }
    return json
def glewia():
    json = {
    "Nazwa":"Glewia",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":10,
    },
    "type":"Zolnierska",
    "krytyk":{
    "mnoznik":2,
    "wynik":20
    },
    "Zasieg":1.5
    }
    return json
def korbaczc():
    json = {
    "Nazwa":"Ciezki Korbacz",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":10,
    },
    "type":"Zolnierska",
    "krytyk":{
    "mnoznik":2,
    "wynik":19
    },
    "Zasieg":1.5
    }
    return json
def kosa():
    json = {
    "Nazwa":"Kosa",
    "Obrazenia":{
    "Ilosc":2,
    "Kosc":4,
    },
    "type":"Zolnierska",
    "krytyk":{
    "mnoznik":4,
    "wynik":20
    },
    "Zasieg":1.5
    }
    return json
def mieczdwr():
    json = {
    "Nazwa":"Miecz Dworeczny",
    "Obrazenia":{
    "Ilosc":2,
    "Kosc":6,
    },
    "type":"Zolnierska",
    "krytyk":{
    "mnoznik":2,
    "wynik":19
    },
    "Zasieg":1.5
    }
    return json
def topordwr():
    json = {
    "Nazwa":"Topor Dworeczny",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":12,
    },
    "type":"Zolnierska",
    "krytyk":{
    "mnoznik":3,
    "wynik":20
    },
    "Zasieg":1.5
    }
    return json
def lukk():
    json = {
    "Nazwa":"Krutki Luk",
    "Obrazenia":{
    "Ilosc":1,
    "Kosc":6,
    },
    "type":"Zolnierska",
    "krytyk":{
    "mnoznik":3,
    "wynik":20
    },
    "Zasieg":1.5
    }
    return json
def Bron(nazwa):
    switcher = {
    "Dlugi Miecz" : mieczdl(),
    "Krotki Miecz" : mieczk(),
    "Lekki Buzdygan" : buzdyganlekki(),
    "Sztylet" : sztylet(),
    "Krotka Wlucznia" : wloczniak(),
    "Maczuga" : maczuga(),
    "Wlucznia" : wlucznia(),
    "Toporek" : toporek(),
    "Mlot Bojowy" : mlotbojowy(),
    "Sejmitar" : sejmitar(),
    "Topor Wojenny" : toporwojenny(),
    "Ciezki Korbacz" : korbaczc(),
    "Kosa" : kosa(),
    "Miecz Dworeczny" : mieczdwr(),
    "Topor Dworeczny" : topordwr(),
    "Krutki Luk" : lukk(),
    }
    return switcher.get(nazwa, "Zla nazwa broni")

def przeszywanica():
    json = {
    "Nazwa":"Przeszywanica",
    "Maxzr" : 8,
    "Bonus" : 1,
    "Niepowodzenie": 5,
    "typ":"Lekka"
    }
    return json
def skoznia():
    json = {
    "Nazwa":"Skoznia",
    "Maxzr" : 6,
    "Bonus" : 2,
    "Niepowodzenie": 10
    }
    return json
def kolcza():
    json = {
    "Nazwa":"Koszula Kolcza",
    "Maxzr" : 4,
    "Bonus" : 4,
    "Niepowodzenie": 20,
    "typ":"Lekka"
    }
    return json
def skozana():
    json = {
    "Nazwa":"Skozana",
    "Maxzr" : 3,
    "Bonus" : 4,
    "Niepowodzenie": 20,
    "typ":"Srednia"
    }
    return json
def luskowa():
    json = {
    "Nazwa":"Luskowa",
    "Maxzr" : 3,
    "Bonus" : 4,
    "Niepowodzenie": 25,
    "typ":"Srednia"
    }
    return json
def kolczuga():
    json = {
    "Nazwa":"Kolczuga",
    "Maxzr" : 2,
    "Bonus" : 5,
    "Niepowodzenie": 30,
    "typ":"Srednia"
    }
    return json
def plytkowa():
    json = {
    "Nazwa":"Plytkowa",
    "Maxzr" : 0,
    "Bonus" : 6,
    "Niepowodzenie": 40,
    "typ":"Ciezka"
    }
    return json
def kryta():
    json = {
    "Nazwa":"Kryta",
    "Maxzr" : 1,
    "Bonus" : 6,
    "Niepowodzenie": 35,
    "typ":"Ciezka"
    }
    return json
def plytowa():
    json = {
    "Nazwa":"Plytowa",
    "Maxzr" : 1,
    "Bonus" : 8,
    "Niepowodzenie": 35,
    "typ":"Ciezka"
    }
    return json
def Zbroja(nazwa):
    switcher = {
    "Przeszywanica" : przeszywanica(),
    "Skoznia" : skoznia(),
    "Koszula Kolcza" : kolcza(),
    "Skozana" : skozana(),
    "Luskowa" : luskowa(),
    "Kolczuga" : kolczuga(),
    "Plytkowa" : plytkowa(),
    "Kryta" : kryta(),
    "Plytowa" : plytowa(),
    }
    return switcher.get(nazwa, "Zla nazwa Zbroja")
