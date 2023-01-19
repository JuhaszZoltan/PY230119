class Versenyzo:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.rajtszam:str = v[1]
        self.kategoria:str = v[2]
        self.versenyido_string:str = v[3]
        self.versenyido = VersenyIdo(v[3])
        self.tav_szazalek:int = int(v[4])
        self.ido_oraban:float = ora(self.versenyido)


class VersenyIdo:
    def __init__(self, vis:str):
        v:list[str] = vis.strip().split(':')
        self.hh:int = int(v[0])
        self.mm:int = int(v[1])
        self.ss:int = int(v[2])


def ora(vi:VersenyIdo) -> float:
    return (vi.hh*3600 + vi.mm*60 + vi.ss) / 3600


def beerkezo_nok_szama(versenyzok:list[Versenyzo]) -> int:
    tt_nok_szama:int = 0
    for versenyzo in versenyzok:
        if versenyzo.kategoria == "Noi" and versenyzo.tav_szazalek == 100:
            tt_nok_szama += 1
    return tt_nok_szama


def keres(versenyzok:list[Versenyzo], keresett_nev:str) -> None:
    i:int = 0
    while i < len(versenyzok) and versenyzok[i].nev != keresett_nev:
        i += 1
    print("\tIndult egyéniben a sportoló?", end=' ')
    if i < len(versenyzok):
        print('Igen')
        print('\tTeljesítette a teljes távot?', end=' ')
        if versenyzok[i].tav_szazalek == 100:
            print('Igen')
        else: print('Nem')
    else: print('Nem')


def ferfi_ido_avg(versenyzok:list[Versenyzo]) -> float:
    tfsz:int = 0
    osum:float = 0
    for v in versenyzok:
        if v.kategoria == "Ferfi" and v.tav_szazalek == 100:
            tfsz += 1
            osum += v.ido_oraban
    return osum / tfsz


def gyoztes(versenyzok:list[Versenyzo], kategoria_nev:str) -> str:
    befutok:list[Versenyzo] = []
    for v in versenyzok:
        if v.kategoria == kategoria_nev and v.tav_szazalek == 100:
            befutok.append(v)
    
    mini:int = 0
    for i in range(1, len(befutok)):
        if befutok[i].ido_oraban < befutok[mini].ido_oraban:
            mini = i

    return f'{befutok[mini].nev} ({befutok[mini].rajtszam}.) - {befutok[mini].versenyido_string}'