#!/usr/bin/python3
from tkinter import*
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from pgm_raw  import *
from tableaux import *
from bibTableau import *
from traitement import *
import os

#variable global
tableau_image=None
image=None
coord_x=None
coord_y=None
nom_fichier=None
tableau_annulation=None
indice_annulation=None

## Fonction fichier ##

def Ouvrir (can):
    global image, tableau_image, nom_fichier,indice_annulation,tableau_annulation
    #verifie qu'un fichier est selectionné
    presence_fichier=askopenfilename(title='Ouvrir',filetypes=(('Image PGM','*.pgm'),('Autre','*.*')))
    if presence_fichier!='' and presence_fichier!=():
            indice_annulation=0
            nom_fichier=presence_fichier
            image=PhotoImage(file=nom_fichier)
            can.create_image(0,0,anchor=NW,image=image)
            can.configure(height=image.height(),width=image.width())
            can.grid()
            tableau_image,largeur,hauteur =lire_fichier_pgm_binaire(nom_fichier)
            tableau_annulation=creerTableau(1,None)
            tableau_annulation[indice_annulation]=recopier_tableau(tableau_image)
            
            
def Sauvegarder():
    global tableau_image,image,nom_fichier
    if presence_image(tableau_image)!=False:
        ecrire_fichier_pgm_binaire(tableau_image,image.width(),image.height(),nom_fichier)
    
def Sauvegarder_sous():
    global tableau_image,image
    if presence_image(tableau_image)!=False:
        image_modif=asksaveasfilename(title='Sauvegarder sous..', defaultextension=".pgm")
        if len(image_modif)>0:
            ecrire_fichier_pgm_binaire(tableau_image, image.width(),image.height(), image_modif)

def Quitter(fen):
    fen.destroy()
    if os.path.isfile('en_cour.pgm'):
        os.remove('en_cour.pgm')


## Fonction de modification et test ##

def coordonner_x_y(position_souris,can,event):
    global tableau_image,coor_x,coord_y
    if presence_image(tableau_image)!=False:
        coord_x=event.x
        coord_y=event.y
        z="x : %d ; y : %d ; niveau de gris : %d" %(coord_x, coord_y,tableau_image[coord_y][coord_x])
        position_souris.config(text=z)
        
def presence_image(tableau):
    if tableau==None:
        showwarning('ERREUR',"Pas d'image")
        return False
    
def afficher_modif(can,tableau_image):
    global image
    ecrire_fichier_pgm_binaire(tableau_image,len(tableau_image[0]), len(tableau_image), 'tmp.pgm')
    image= PhotoImage(file='tmp.pgm')
    can.create_image(0,0,anchor=NW,image=image)
    can.configure(height=image.height(),width=image.width())
    can.grid()
    #supprimer le fichier temporaire 
    if os.path.isfile('tmp.pgm'):
        os.remove('tmp.pgm')

def retablir(can):
    global image,nom_fichier,tableau_image
    if presence_image(tableau_image)!=False:
        can.delete(ALL)
        image= PhotoImage(file=nom_fichier)
        can.create_image(0,0,anchor=NW,image=image)
        can.configure(height=image.height(),width=image.width())
        can.grid()
        tableau_image,largeur,hauteur =lire_fichier_pgm_binaire(nom_fichier)

def sauvegarde_enchainement_traitement(tableau_image):
    global tableau_annulation,indice_annulation
    if indice_annulation==len(tableau_annulation)-1:
        ajouterNcases(tableau_annulation,1)
    indice_annulation+=1
    tableau_annulation[indice_annulation]=recopier_tableau(tableau_image)
    

def defaire(can):
    global indice_annulation,tableau_annulation,tableau_image
    if presence_image(tableau_image)!=False:
        if indice_annulation>0:
            indice_annulation-=1
            afficher_modif(can,tableau_annulation[indice_annulation])
            tableau_image=recopier_tableau(tableau_annulation[indice_annulation])
        else:
            showwarning('Erreur',"Impossible d'annuler \n Image d'origine")
            return
        
def refaire(can):
    global indice_annulation,tableau_annulation,tableau_image
    if presence_image(tableau_image)!=False:
        if indice_annulation<=len(tableau_annulation)-2:
            indice_annulation+=1
            afficher_modif(can,tableau_annulation[indice_annulation])
            tableau_image=recopier_tableau(tableau_annulation[indice_annulation])
        else:
            showwarning('Erreur',"Impossible de refaire \n Plus d'action possible")
            return
    
## Fonction traitement ##

#fonction valable pour plusieurs traitements 
def fonction(can,traitement):
    global tableau_image,image
    if presence_image(tableau_image)!=False:
        tableau_image=traitement(tableau_image)
        afficher_modif(can,tableau_image)
        sauvegarde_enchainement_traitement(tableau_image)
        
#fonction autres
def vieille_photo(fen,can):
    global tableau_image
    if presence_image(tableau_image)!=False:
        tableau_image=traitement_flou(tableau_image,1)
        tableau_image=traitement_contraste(tableau_image,0,220)
        tableau_image=traitement_bruit_gaussien(10,tableau_image)
        rayure(can)
        afficher_modif(can,tableau_image)
    

    
    
def bruit_gaussien(fen,can):
    global tableau_image,image
    if presence_image(tableau_image)!=False:
        #demande une valeur
        valeur=askinteger("Bruit","Entrez une valeur (0 ≤ X ≤ 255)",initialvalue=0,minvalue=0,maxvalue=255)
        if valeur!=None:
            tableau_image=traitement_bruit_gaussien(valeur,tableau_image)
            afficher_modif(can,tableau_image)
            sauvegarde_enchainement_traitement(tableau_image)

def flou(can):
    global tableau_image
    if presence_image(tableau_image)!=False:
        nb_flou=askinteger("Bruit","Entrez une valeur (0 ≤ X ≤ 10)",initialvalue=0,minvalue=0,maxvalue=10)
        if nb_flou!=None:
            tableau_image=traitement_flou(tableau_image,nb_flou)
            afficher_modif(can,tableau_image)
            sauvegarde_enchainement_traitement(tableau_image)
        
def contraste(can):
    global tableau_image
    if presence_image(tableau_image)!=False:
        minimum, maximum = minimum_maximum(tableau_image)
        if minimum!=0 and maximum!=255:
            tableau_image=traitement_contraste(tableau_image,minimum,maximum)
            afficher_modif(can,tableau_image)
            sauvegarde_enchainement_traitement(tableau_image)
        else:
            #message errueur si le contraste est maximum 
            showwarning('Max contraste',"Le contraste est déjà maximum")
            return
        
def surexposition(fen,can):
    global tableau_image,image
    if presence_image(tableau_image)!=False:
        valeur=askinteger("surexposition","Entrez une valeur (0 ≤ X ≤ 255)" ,initialvalue=150,minvalue=0,maxvalue=255)
        if valeur!=None:
            tableau_image=traitement_contraste(tableau_image,0,valeur)
            afficher_modif(can,tableau_image)
            sauvegarde_enchainement_traitement(tableau_image)
            
def rayure(can):
    global tableau_image,image
    if presence_image(tableau_image)!=False:
        #creation tableau de l'image rayure 
        tableau_rayure,largeur,hauteur =lire_fichier_pgm_binaire('Icones/rayure.pgm')
        tableau_rayure=mise_echelle_image(tableau_rayure,len(tableau_image),len(tableau_image[0]))
        tableau_image=traitement_rayure(tableau_image,tableau_rayure)
        sauvegarde_enchainement_traitement(tableau_image)
        afficher_modif(can,tableau_image)
        






