#import knihoven sqlite3 pro práci s databází a pandas pro formátování výstupu z databáze
import sqlite3
import pandas as pd
#připojení databáze
con = sqlite3.connect("databaze.db")
cur = con.cursor()

class Pojistenci:

    def pridat_noveho_pojisteneho(self):
        info = input("Zadejte jméno:"), input("Zadejte příjmení:"), int(input("Zadejte telefonní číslo:")), int(input("Zadejte věk:"))
        cur.execute("INSERT INTO pojistenci VALUES(null, ?, ?, ?, ?);", info)
        con.commit()

    def vypsat_vsechny_pojistence(self):
        print(pd.read_sql_query("SELECT jmeno, prijmeni, tel_cislo, vek FROM pojistenci", con))



    def vyhledat_pojistene(self):
        hledani_jmeno = input("Zadejte hledané jméno:")
        hledani_prijmeni = input("Zadejte hledané příjmení:")
        print(pd.read_sql_query(f"SELECT jmeno, prijmeni, tel_cislo, vek FROM pojistenci WHERE jmeno = '{hledani_jmeno}' AND prijmeni='{hledani_prijmeni}'", con))

