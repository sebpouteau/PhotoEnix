#! /usr/bin/python3
from tkinter import*
from tkinter.filedialog import *
from pgm_raw import *
from tableaux import *
from bibTableau import *
from random import *


## Fonction utile ##
def inverse_deux_cellules(t,cellule1,cellule2):
    var=t[cellule1]
    t[cellule1] = t[cellule2]
    t[cellule2]=var

def recopier_tableau(tableau):
    tableau_copie=creer_tableau(len(tableau),len(tableau[0]),None)
    for i in range(len(tableau)):
        for j in range(len(tableau[0])):
            tableau_copie[i][j]=tableau[i][j]
    return tableau_copie
            
def minimum_maximum(tableau):
    minimum=tableau[0][0]
    maximum=tableau[0][0]
    for i in range(len(tableau)):
        for j in range(len(tableau[0])):
            if minimum > tableau[i][j]:
                minimum = tableau[i][j]
            if maximum < tableau[i][j]:
                maximum=tableau[i][j]
    if maximum>255:
        maximum=255
    if minimum<0:
        minimum=0
    return minimum, maximum

def mise_echelle_image(tableau,hauteur,largeur):
    tableau_echelle=creer_tableau(hauteur,largeur,None)
    for i in range(len(tableau_echelle)):
        for j in range(len(tableau_echelle[0])):
            rapport_i = i//len(tableau)+1
            rapport_j = j//len(tableau[0])+1
            if i<len(tableau) and j<len(tableau[0]):
                tableau_echelle[i][j]=tableau[i][j]
            elif i>=len(tableau) and j>=len(tableau[0]):
                tableau_echelle[i][j]=tableau[i-rapport_i*len(tableau)][j-rapport_j*len(tableau[0])]
            elif i>=len(tableau):
                tableau_echelle[i][j]=tableau[i-rapport_i*len(tableau)][j]
            else:
                tableau_echelle[i][j]=tableau[i][j-rapport_j*len(tableau[0])]
    return tableau_echelle


##Fonction traitement image ##

def traitement_negatif(tableau):
    for i in range(len(tableau)):
        for j in range(len(tableau[0])):
            tableau[i][j]=255-tableau[i][j]
    return tableau

def traitement_bruit_gaussien(ecart_type,tableau):
    for i in range(len(tableau)):
        for j in range(len(tableau[0])):
            ng=int(gauss(0,ecart_type))
            tableau[i][j]=tableau[i][j]+ng
            if tableau[i][j]>255:
                tableau[i][j]=255
            elif tableau[i][j]<0:
                tableau[i][j]=0
    return tableau
               
def traitement_symetrie(tableau):
    taille=len(tableau[0])
    milieu= taille//2
    if taille%2==0:
        for i in range (len(tableau)):
            for j in range(taille//2):
                inverse_deux_cellules(tableau[i],milieu-j,milieu+j)
    else:
        for i in range (len(tableau)):
            for j in range(taille//2-1):
                inverse_deux_cellules(tableau[i],milieu-j,milieu+j+1)
    
    return tableau

def traitement_flou(tableau,nb_flou):
    tableau_modif=recopier_tableau(tableau)
    for i in range(0,len(tableau)):
        for j in range(0,len(tableau[0])):
            s=0
            div=0
            for k in range(-nb_flou,nb_flou+1):
                for l in range(-nb_flou,nb_flou+1):
                    if i+k>=0 and j+l>=0 and i+k<len(tableau) and j+l<len(tableau[0]):
                        s+=tableau[i+k][j+l]
                    else:
                        if div==0:
                            s=tableau[i][j]
                        else:
                            s+=s//div                                              
                    div+=1
            s//=div
            tableau_modif[i][j]=s
    return tableau_modif
                     
def traitement_contraste(tableau,minimum,maximum):
    if minimum!=maximum:
        for i in range(len(tableau)):
            for j in range(len(tableau[0])):
                tableau[i][j]=((tableau[i][j]-minimum)*255)//(maximum-minimum)
                if tableau[i][j]>255:
                    tableau[i][j]=255
                elif tableau[i][j]<0:
                    tableau[i][j]=0
    return  tableau

def traitement_rayure(tableau,tableau_rayure):
    for i in range(len(tableau)):
        for j in range(len(tableau[0])):
            if tableau_rayure[i][j]>80:
                tableau[i][j]=(tableau[i][j]+tableau_rayure[i][j])//2
    return tableau

#traitement des rotations

def traitement_rotation_droite(tableau):
    tableau_modif=creer_tableau(len(tableau[0]), len(tableau), None)
    for i in range(len(tableau)):
        for j in range(len(tableau[0])):
            tableau_modif[j][len(tableau)-1-i]=tableau[i][j]
    return tableau_modif

def traitement_rotation_gauche(tableau):
    tableau_modif=creer_tableau(len(tableau[0]), len(tableau), None)
    for i in range(len(tableau)):
        for j in range(len(tableau[0])):
            tableau_modif[j][i]=tableau[i][len(tableau[0])-1-j]        
    return tableau_modif

def traitement_miroir_vertical_droite(tableau):
    taille=len(tableau[0])
    for i in range(len(tableau)):
        for j in range(taille//2):
            tableau[i][taille-1-j]=tableau[i][j]
    return tableau
                           
def traitement_miroir_vertical_gauche(tableau):
    taille=len(tableau[0])
    for i in range(len(tableau)):
        for j in range(taille//2):
            tableau[i][j]=tableau[i][taille-1-j]
    return tableau

def traitement_miroir_horizontal_haut(tableau):
    taille=len(tableau)
    for i in range(taille//2):
        for j in range(len(tableau[0])):
            tableau[taille-i-1][j]=tableau[i][j]
    return tableau

def traitement_miroir_horizontal_bas(tableau):
    taille=len(tableau)
    for i in range(taille//2):
        for j in range(len(tableau[0])):
            tableau[i][j]=tableau[len(tableau)-i-1][j]
    return tableau



if __name__ == '__main__':
    t=[[0,255,0,255,0,255],[0,255,0,255,0,255],[0,255,0,255,0,255]];print('\n tableau origine');afficher_tableau(t);s=creerTableau(len(t))
    c=[[50,51,50],[52,50,51]]
    print('\n test sur negatif');s=traitement_negatif(t);afficher_tableau(s)
    print('\n test sur bruit avec ecart type de 10');s=traitement_bruit_gaussien(10,t);afficher_tableau(s)
    print('\n test sur la mise à l echelle ');s=mise_echelle_image(t,9,7);afficher_tableau(s)
    print('\n test sur le contraste ');minimum,maximum=minimum_maximum(c);s=traitement_contraste(c,minimum,maximum);afficher_tableau(s)

