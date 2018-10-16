def Czlowiek():
    json = {
    "Plusy":[],
    "Minusy":[],
    "Specjalne":["atut"]
    }
    return json
def Krasnolud():
    json = {
    "Plusy":["b"],
    "Minusy":["c"],
    "Specjalne":[]
    }
    return json
def Elf():
    json = {
    "Plusy":["z"],
    "Minusy":["b"],
    "Specjalne":[]
    }
    return json
def Gnom():
    json = {
    "Plusy":["b"],
    "Minusy":["s"],
    "Specjalne":[]
    }
    return json
def Polelf():
    json = {
    "Plusy":[],
    "Minusy":[],
    "Specjalne":[]
    }
    return json
def Polokr():
    json = {
    "Plusy":["s"],
    "Minusy":["c","i"],
    "Specjalne":[]
    }
    return json
def Nizolek():
    json = {
    "Plusy":["z"],
    "Minusy":["s"],
    "Specjalne":[]
    }
    return json
def Rasa(Nazwa):
    switcher = {
        "Czlowiek": Czlowiek(),
        "Krasnolud": Krasnolud(),
        "Elf": Elf(),
        "Gnom": Gnom(),
        "Polelf": Polelf(),
        "Nizolek": Nizolek(),
    }
    return switcher.get(Nazwa, "Zla nazwa rasy")
