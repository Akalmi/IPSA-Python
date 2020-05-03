"""
    *In21-Converter Durees (Python)

    """
from time import*
print("######################################################################")
#Données exemples : 12h 14min 04sec 000millisec / 0h 02min 03sec 123millisec / 0h 00min 36sec 456millisec 789microsec

def Verifie_saisi(saisi):
    list_chiffres = "0123456789"
    return all([caractere in list_chiffres for caractere in saisi])

def ConverterDurees():
    b_heure = True
    b_minute = True
    b_seconde = True
    b_milliseconde = True
    b_microseconde = True
    while b_heure:
        heure = input("Veuillez choisir le nombre d'heures : ")
        if Verifie_saisi(heure):
            b_heure = False
            
    while b_minute:
        minute = input("Veuillez choisir le nombre de minutes : ")
        if Verifie_saisi(minute):
            b_minute = False
            
    while b_seconde:
        seconde = input("Veuillez choisir le nombre de seconde : ")
        if Verifie_saisi(seconde):
            b_seconde = False

    while b_milliseconde:
        milliseconde = input("Veuillez choisir le nombre de milli-seconde : ")
        if Verifie_saisi(milliseconde):
            b_milliseconde = False

    while b_microseconde:
        microseconde = input("Veuillez choisir le nombre de micro-seconde : ")
        if Verifie_saisi(microseconde):
            b_microseconde = False

    Resultat = (int(heure)*3600) + (int(minute)*60) + int(seconde) + (int(milliseconde)/1000) + (int(microseconde)/1000000)
    return print("La durée retenue est : ", heure, "h", minute,"min", seconde,"sec",milliseconde,"msec", microseconde, "microsec. Une fois convertie, cela nous donne ", Resultat, "secondes.")

#@uthor : Thomas Piacentile
