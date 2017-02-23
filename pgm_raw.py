# -*- coding:utf-8 -*-

from tableaux import *

def creer_entete_fichier_pgm_binaire(l,h,nom):
    f = open(nom,'w', encoding="latin-1")
    f.write('P5' + '\n')
    f.write(str(l) + ' ' + str(h) + '\n')
    f.write('255 \n')
    f.close()

def ecrire_fichier_pgm_binaire(t, l, h, nom):
    creer_entete_fichier_pgm_binaire(l,h,nom)
    f = open(nom,'ab')
    for i in range(h):
        for j in range(l):
            f.write (bytes([t[i][j]])) #conversion int -> byte
    f.close()

def lire_en_tete_fichier_pgm (nom):
    f = open (nom, 'r', encoding="latin-1")
  #lecture du mode :  P5 (pgm binaire)
    mode = f.readline()
  #lecture des dimensions (il faut sauter les éventuelles lignes de commentaire)
    dim = f.readline()
    while dim[0] == '#':
        dim = f.readline()
    t_dim = dim.split()
    largeur = int(t_dim[0])
    hauteur = int(t_dim[1])
  # lecture de la valeur maximale d'un niveau de gris (255)
    val_max = f.readline()
    f.close()
    return hauteur, largeur

def lire_fichier_pgm_binaire (nom):
    hauteur, largeur = lire_en_tete_fichier_pgm (nom)
    # création du tableau image
    t_image = creer_tableau(hauteur, largeur, 0)
    f = open (nom, 'rb') # lecture de données binaires
    f.seek(-largeur*hauteur,2) # on se place après l'en-tete
    for i in range(hauteur):
        for j in range(largeur):
            o = f.read(1)
            t_image[i][j] = ord(o) # conversion byte -> int
    f.close()
    return t_image, largeur, hauteur
