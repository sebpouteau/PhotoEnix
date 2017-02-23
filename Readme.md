#  Projet PhotoEnix python3.3
(Licence 1 - Informatique)

Réalisé par: Sébastien Pouteau


## Compilation
    - pyhton3.3 main.py

## Explication sur les fonctions :

- fonction bruit gaussien faite avec Nicolas Palard

### fonction Ouvrir:

présence_fichier sert a vérifier que l'on a sélectionné un fichier. Se qui permet d'éviter les erreurs si l'on fait annulé lors de l'ouverture.

l'ajout du test presence!=() évite l'erreur suivante:
Ouvrir => ouverture d'une image => Ouvrir => Annuler



### fonction présence_image:

test si une image est ouverte donc si un tableau existe? Se qui limite les erreurs lors de l'exécution des traitement

### fonction mise_echelle_image:

si l'image est plus petite elle recopie juste les valeurs du tableau image dans un tableau plus petit?
si l'image est plus grande, elle recopie tout le tableau image, une ou plusieurs fois, jusqu'à remplir totalement le tableau final.

utilisation de la variable "rapport" de se replacer au début du tableau lorsqu'on atteint la fin du tableau image. Elle évite donc les erreurs si le tableau final fais plus de deux fois la taille du tableau image.


### fonction flou:

ce flou prend la moyenne du voisinage du pixel sélectionné.
si un pixel appartenant au voisinage n'appartient pas au tableau alors il remplace cette valeur par la moyenne des pixels voisins déjà calculé.

### fonction défaire et refaire:

Utilisation d'un tableau sauvegarde contenant dans chacune de ses cases la version du tableau image au cour des traitements,permettant de pouvoir défaire et refaire un ou plusieurs traitement.


### fonction ajouté:

- fonction défaire
- fonction refaire
- fonction rétablir

- traitement rotation à droite
- traitement rotation à gauche
- traitements miroirs
