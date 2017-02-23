#! /usr/bin/python3
from tkinter import *
from interface import *
from tkinter.filedialog import *


#fenetre
fen= Tk()
fen.title('Photoenix')

#config du menu
mon_menu=Menu(fen)
fen.config(menu=mon_menu)

#config du menu deroulant Fichier
menu_fichier=Menu(mon_menu,tearoff=0)
mon_menu.add_cascade(label="Fichier",menu=menu_fichier)
menu_fichier.add_command(label="Ouvrir",command=lambda:Ouvrir(can))
menu_fichier.add_command(label="Sauvegarder",command=Sauvegarder)
menu_fichier.add_command(label="Sauvegarder sous ..",command=Sauvegarder_sous)
menu_fichier.add_command(label="Quitter",command=lambda:Quitter(fen))

#config du menu deroulant Edition
menu_edition=Menu(mon_menu,tearoff=0)
mon_menu.add_cascade(label="Edition",menu=menu_edition)
menu_edition.add_command(label="Défaire",command=lambda:defaire(can))
menu_edition.add_command(label="Refaire",command=lambda:refaire(can))
menu_edition.add_command(label="Rétablir",command=lambda:retablir(can))



#config du menu deroulant Traitement
menu_traitement=Menu(mon_menu,tearoff=0)
mon_menu.add_cascade(label="Traitement",menu=menu_traitement)
menu_traitement.add_command(label="Vieille-Photo",command=lambda:vieille_photo(fen,can))
menu_traitement.add_command(label="Negatif",command=lambda:fonction(can,traitement_negatif))
menu_traitement.add_command(label="symetrie",command=lambda:fonction(can,traitement_symetrie))
menu_traitement.add_command(label="Flou",command=lambda:flou(can))
menu_traitement.add_command(label="Contraste",command=lambda:contraste(can))
menu_traitement.add_command(label="Superexposition",command=lambda:surexposition(fen,can))
menu_traitement.add_command(label="Bruit",command=lambda:bruit_gaussien(fen,can))
menu_traitement.add_command(label="Rayure",command=lambda:rayure(can))
menu_traitement.add_command(label="Rotation Gauche",command=lambda:fonction(can,traitement_rotation_gauche))
menu_traitement.add_command(label="Rotation Droite",command=lambda:fonction(can,traitement_rotation_droite))

menu_miroir=Menu(menu_traitement)
menu_traitement.add_cascade(label="miroir",menu=menu_miroir)
menu_miroir.add_command(label="vertical droite",command=lambda:fonction(can,traitement_miroir_vertical_droite))
menu_miroir.add_command(label="vertical gauche",command=lambda:fonction(can,traitement_miroir_vertical_gauche))
menu_miroir.add_command(label="horizontal haut",command=lambda:fonction(can,traitement_miroir_horizontal_haut))
menu_miroir.add_command(label="horizontal bas",command=lambda:fonction(can,traitement_miroir_horizontal_bas))


## Ligne des bouton #

ligne_bouton=Frame(fen)
ligne_bouton.grid(sticky=W)

photo_ouvrir = PhotoImage(file='Icones/ouvrir.pgm')
photo_sauvegarder = PhotoImage(file='Icones/sauvegarder.pgm')
photo_droite = PhotoImage(file='Icones/refaire.pgm')
photo_gauche = PhotoImage(file='Icones/defaire.pgm')


bouton_ouvrir=Button(ligne_bouton,text="ouvrir",image=photo_ouvrir,command=lambda:Ouvrir(can))
bouton_ouvrir.grid(row=0,column=0)
bouton_sauvegarder=Button(ligne_bouton,text="sauvegarder",image=photo_sauvegarder,command=Sauvegarder)
bouton_sauvegarder.grid(row=0,column=1)

bouton_refaire=Button(ligne_bouton,image=photo_gauche,command=lambda:defaire(can))
bouton_refaire.grid(row=0,column=2)
bouton_defaire=Button(ligne_bouton,image=photo_droite,command=lambda:refaire(can))
bouton_defaire.grid(row=0,column=3)

bouton_retablir=Button(ligne_bouton,text="rétablir",command=lambda:retablir(can))
bouton_retablir.grid(row=0,column=6)

## canvas de depart ##
image_canvas= PhotoImage(file='Icones/pheonix.gif')

can = Canvas(fen,
             height=300, width=300,background='grey',bd=0)
can.create_image(0,0,anchor=NW,image=image_canvas)
can.configure(height=image_canvas.height(),width=image_canvas.width())

can.grid(row=2)

## Action de la souris ##
can.bind("<Button-1>", lambda event:coordonner_x_y(position_souris,can,event))


position_souris=Label(fen,
               text="Position de la souris")
position_souris.grid(row=4)

fen.mainloop()
