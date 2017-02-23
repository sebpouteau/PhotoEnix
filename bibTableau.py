#!/usr/bin/env python3
# Fonctions fournies aux etudiants
import random

# Creation et initialisation de tableaux d'entiers


# La fonction creerTableau cree un tableau de taille elements
# utilisation: creerTableau(10) ou creerTableau(10,-1) 
def creerTableau(nombreElements,valeurInitiale=0 ):
    return [valeurInitiale]*nombreElements

# La fonction creerTableaualeatoire cree un tableau de n elements 
# tires aleatoirement dans l'intervalle [borneInf,borneSup]
# utilisation: creerTableauAleatoire(10) ou creerTableauAleatoire(10,-50,-10)
def creerTableauAleatoire(nombreElements,borneInf=-50, borneSup=50): 
    t = creerTableau(nombreElements)
    for i in range (nombreElements):
        t[i] = random.randint(borneInf,borneSup)
    return t

# La fonction creerTableauMonotone cree un tableau de n elements 
# tires aleatoirement dans l'intervalle [borneInf,borneSup]
# si variation est positif (resp negatif), le tableau est croissant (resp decroissant)
# utilisation: creerTableauMonotone(10) ou creerTableauMonotone(10,-1)

def creerTableauMonotone(nombreElements, variation = 1,borneInf=-1000, borneSup=1000):
     t = creerTableauAleatoire(nombreElements,borneInf,borneSup)
     var = variation < 0
     return sorted(t,reverse = var)

# Modifications de tableaux

# La fonction ajouterNcases ajoute n cases au tableau fourni en parametre.
# Ces cases sont initialisees a None
def ajouterNcases(t,n):
    t += [None]*n

# La fonction supprimerNcases supprime les n dernieres cases du tableau fourni en parametre.
def supprimerNcases(t,n):
    if n <= len(t):
        t[len(t)-n:]=[]
    else:
        t[:]=[]
        
    

