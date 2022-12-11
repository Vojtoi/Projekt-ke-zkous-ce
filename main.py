#import třídy Pojistenci
from Pojistenci import Pojistenci
#vložení instance Pojistenci do proměnné
pojistenci = Pojistenci()

print("____________________\nEvidence pojištěných\n____________________")
#výběr operací a while cyklus pro pokračování zadávaní
pokracovat = True
while (pokracovat == True):
    operace = int(input("Vyberte si akci: \n1 - Přidat nového pojištěného\n2 - Vypsat všechny pojištěné\n3 - Vyhledat pojištěného\n4 - Konec\n"))

    if (operace == 1):
        pojistenci.pridat_noveho_pojisteneho()
        print("Pojištěný byl přidán.\n_____________________")
    elif (operace == 2):
        pojistenci.vypsat_vsechny_pojistence()
        print("______________________________")
    elif (operace == 3):
        pojistenci.vyhledat_pojistene()
        print("______________________________")
    elif (operace == 4):
        input("Stisknutím klávesy enter ukončíte aplikaci:")
        pokracovat = False
    else:
        print("Chybná volba")
