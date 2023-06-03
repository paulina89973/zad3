class Kosmetyk:
    def __init__(self, nazwa, marka, cena, pojemnosc, kolor, typ, kraj_pochodzenia, dostepny):
        self.nazwa = nazwa
        self.marka = marka
        self.cena = cena
        self.pojemnosc = pojemnosc
        self.kolor = kolor
        self.typ = typ
        self.kraj_pochodzenia = kraj_pochodzenia
        self.dostepny = dostepny

    def __str__(self):
        return f"Kosmetyk: {self.nazwa} ({self.marka})\n" \
               f"Cena: {self.cena} zł\n" \
               f"Pojemność: {self.pojemnosc} ml\n" \
               f"Kolor: {self.kolor}\n" \
               f"Typ: {self.typ}\n" \
               f"Kraj pochodzenia: {self.kraj_pochodzenia}\n" \
               f"Dostępny: {'Tak' if self.dostepny else 'Nie'}"

    def wyswietl_informacje(self):
        print(self)

    def sprawdz_dostepnosc(self):
        if self.dostepny:
            print(f"{self.nazwa} jest dostępny.")
        else:
            print(f"{self.nazwa} nie jest dostępny.")

    def zmien_dostepnosc(self, dostepnosc):
        self.dostepny = dostepnosc
        print(f"Zmieniono dostępność {self.nazwa} na {'Tak' if dostepnosc else 'Nie'}.")


# Przykładowe użycie klasy kosmetyki
kosmetyk = Kosmetyk("Podkład", "Maybelline", 39.99, 30, "Naturalny", "Fluid", "Francja", True)
kosmetyk.wyswietl_informacje()
kosmetyk.sprawdz_dostepnosc()
kosmetyk.zmien_dostepnosc(False)
kosmetyk.wyswietl_informacje()