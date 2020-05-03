"""
    *In21-Converter Radian / Degres (Python)

    """
from math import*

#1. Convertir les angles suivant de degrés décimaux en radians
def Verifie_saisi(saisi):
    list_chiffres = "0123456789"
    return all([caractere in list_chiffres for caractere in saisi])

def ConverterDR():
    
    b_Angle_Degres = True
    while b_Angle_Degres:
             Angle_Degres = input("Veuillez entrer un angle en degrès : ")
             if Verifie_saisi(Angle_Degres) and Angle_Degres != '':
                 print("La valeur de l'angle retenue est :",Angle_Degres,"°")
                 b_Angle_Degres = False

    return print("L'angle  de ", int(Angle_Degres), "° vaut : ", radians(int(Angle_Degres)), "radian(s)")

def ConverterRD():
    
    b_Angle_Radian = True
    while b_Angle_Radian:
             Angle_Radian = input("Veuillez entrer un angle en radian : ")
             if Verifie_saisi(Angle_Radian) and Angle_Radian != '':
                 print("La valeur de l'angle retenue est :",Angle_Radian,"rad")
                 b_Angle_Radian = False

    return print("L'angle  de ", int(Angle_Radian), "° vaut : ", degrees(int(Angle_Radian)), "degrees(s)")


#@uthor : Thomas Piacentile"
