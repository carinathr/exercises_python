def vokon_zählen(x):
    vokale = ["a", "e", "i", "o", "u"]
    vokale_anzahl = 0
    konsonanten_anzahl = 0

    x = x.lower()
    x_list = list(x)
    for i in x_list:
        if i.isalpha():
            if i in vokale:
                vokale_anzahl += 1
            else:
                konsonanten_anzahl += 1
    print(f"Es gibt {vokale_anzahl} Vokale und {konsonanten_anzahl} Konsonanten")
                
vokon_zählen("Hallo Berlin")
