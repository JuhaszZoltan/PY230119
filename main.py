from module import Versenyzo, beerkezo_nok_szama, keres, ferfi_ido_avg, gyoztes

versenyzok:list[Versenyzo] = []

for sor in open('ub2017egyeni.txt').readlines()[1:]:
    versenyzok.append(Versenyzo(sor))

print(f'3. feladat: Egyéni indulók: {len(versenyzok)} fő')

bnsz:int = beerkezo_nok_szama(versenyzok)
print(f'4. feladat: Célba érkező női sportolók: {bnsz} fő')

nev:str = input('5. feladat: Kérem a sportoló nevét: ')
keres(versenyzok, nev)

ai:float = ferfi_ido_avg(versenyzok)
print(f'7. feladat: Átlagos idő: {ai} óra')

print('8. feladat: A verseny győztesei:')
print(f'\tNők: {gyoztes(versenyzok, "Noi")}')
print(f'\tFérfiak: {gyoztes(versenyzok, "Ferfi")}')