# -*- coding:utf-8 -*-

# création d'un vecteur de taille l initialisé à val
def creer_tableau_1D(l, val):
    t = [val]*l  
    return t

# création d'une matrice [h,l] initialisée à val
# le premier indice correspond à la hauteur
def creer_tableau (h, l, val):
    t = creer_tableau_1D(h, None) 
    for i in range(0, h):
        t[i] = creer_tableau_1D(l, val)
    return t

# affichage sommaire
def afficher_tableau(t):
    print()
    for i in range(len(t)):
        print(t[i])


#tests
if __name__ == "__main__":
    m = creer_tableau(10, 5, 0)
    afficher_tableau(m)
    
# parcours ligne par ligne
    cpt = 0
    h = len(m)
    l = len(m[0])
    for i in range(h):
        for j in range(l):
            m[i][j] = cpt
        cpt += 1

# parcours colonne par colonne
    # cpt = 0
    # h = len(m)
    # l = len(m[0])
    # for j in range(l):
    #     for i in range(h):
    #         m[i][j] = cpt
    #     cpt += 1
            
    afficher_tableau(m)

def copier_tableau(t1,t2):
    for i in range(len(t1)):
        for j in range(len(t1)):
            t2[i][j]=t1[i][j]
