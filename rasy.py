def Czlowiek():
    json = {
    "Plusy":[],
    "Minusy":[],
    "Specjalne":["atut"],
    "Predkosc":9
    }
    return json
def Krasnolud():
    json = {
    "Plusy":["b"],
    "Minusy":["c"],
    "Specjalne":[],
    "Predkosc":6
    }
    return json
def Elf():
    json = {
    "Plusy":["z"],
    "Minusy":["b"],
    "Specjalne":[],
    "Predkosc":9
    }
    return json
def Gnom():
    json = {
    "Plusy":["b"],
    "Minusy":["s"],
    "Specjalne":[],
    "Predkosc":6
    }
    return json
def Polelf():
    json = {
    "Plusy":[],
    "Minusy":[],
    "Specjalne":[],
    "Predkosc":9
    }
    return json
def Polokr():
    json = {
    "Plusy":["s"],
    "Minusy":["c","i"],
    "Specjalne":[],
    "Predkosc":12
    }
    return json
def Nizolek():
    json = {
    "Plusy":["z"],
    "Minusy":["s"],
    "Specjalne":[],
    "Predkosc":12
    }
    return json
def Rasa(Nazwa):
    switcher = {
        "Czlowiek": Czlowiek(),
        "Krasnolud": Krasnolud(),
        "Elf": Elf(),
        "Gnom": Gnom(),
        "Polelf": Polelf(),
        "Polork":Polokr(),
        "Nizolek": Nizolek(),
    }
    return switcher.get(Nazwa, "Zla nazwa rasy")
