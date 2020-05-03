from math import*

# Vérification des données d'entrées
def Verifie_saisi(saisi):
    list_chiffres = "0123456789"
    return all([caractere in list_chiffres for caractere in saisi])

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
def Solve_Equation(CoefficientA, CoefficientB, CoefficientC):
    print("  ---------------------------------------------- \n")
    print("| Equations du second degrés avec spécifications | \n")
    print("  ---------------------------------------------- \n")
    
    Delta = ((pow(CoefficientB,2))-(4*CoefficientA*CoefficientC))
    Delta_abs = abs(Delta)
    print("Delta = ", Delta)
    acine_1, racine_2 = calcul_racines(CoefficientA, CoefficientB, Delta, Delta_abs)
        
            
        
        
