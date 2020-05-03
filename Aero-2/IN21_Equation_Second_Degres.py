from math import*
from math import radians
from time import *
from datetime import date

# Vérification des données d'entrées
def Verifie_saisi(saisi):
    list_chiffres = "0123456789"
    return all([caractere in list_chiffres for caractere in saisi])

#Saisi des coefficients
def saisi_coefficient():
        print("*Saisi des coefficients : ")
        b_CoefficientA = True
        b_CoefficientB = True
        b_CoefficientC = True
        while b_CoefficientA :
             a = input("a = ")
             if Verifie_saisi(a) and a != '':
                     print("La valeur du coefficient A retenue est :",a)
                     b_CoefficientA = False

        while b_CoefficientB :
             b = input("b = ")
             if Verifie_saisi(b) and b != '':
                     print("La valeur du coefficient B retenue est :",b)
                     b_CoefficientB = False

        while b_CoefficientC :
             c = input("c = ")
             if Verifie_saisi(c) and b != '':
                     print("La valeur du coefficient C retenue est :",c)
                     b_CoefficientC = False

        return int(a), int(b), int(c)

def calcul_racines(CoefficientA, CoefficientB, Delta, Delta_abs):
        racine_2 = "Inexistante"
        #Delta négatif
        if Delta < 0:
                racine_1 = complex((-CoefficientB)/(2*CoefficientA), sqrt(Delta_abs)/(2*CoefficientA))
                racine_2 = complex((-CoefficientB)/(2*CoefficientA),-sqrt(Delta_abs)/(2*CoefficientA))
        #Delta positif
        elif Delta > 0:
                racine_1 = (-CoefficientB + sqrt(Delta_abs))/(2*CoefficientA)
                racine_2 = (-CoefficientB - sqrt(Delta_abs))/(2*CoefficientA)
        else:
                racine_1 = -CoefficientB/(2*CoefficientA)

        #Affichage des racines
        print("les racines de ce polynôme sont : ", racine_1, " et ", racine_2)
        print("\n")

        return racine_1, racine_2

# Main
def Main():
    print("  ---------------------------------------------- \n")
    print("| Equations du second degrés avec spécifications | \n")
    print("  ---------------------------------------------- \n")
    
    b_Verification = True
    b_Continuer = True
    while b_Continuer:
        CoefficientA, CoefficientB, CoefficientC = saisi_coefficient()
        Delta = ((pow(CoefficientB,2))-(4*CoefficientA*CoefficientC))
        Delta_abs = abs(Delta)
        print("Delta = ", Delta)
        racine_1, racine_2 = calcul_racines(CoefficientA, CoefficientB, Delta, Delta_abs)

        
        while b_Verification:
            sContinuer = input("Voulez-vous résoudre une autre équation ? (OUI / NON) : ")
            if sContinuer == "NON":
                print("La session est terminé !")
                b_Continuer = False
                b_Verification = False
            elif sContinuer == "OUI":
                print("\n\n")
                b_Continuer = True
                b_Verification = False
            else:
                b_Verification = True
            
        
        
