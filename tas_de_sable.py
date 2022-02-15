#########################################
# groupe BI TD03 GROUPE 1
# Sophie Hatey
# Hugo Coral
# Jibril Bedoei
# https://github.com/uvsq22104225/ProjetSABLE
#########################################

#########################################
#          IMPORT DES LIBRAIRIES        #
#########################################


from cmath import inf
import tkinter as tk
import random as rand


#########################################
#       DEFINITION DES CONSTANTES       #
#########################################

HEIGHT = 500
WIDTH = 500

#########################################
#  DEFINITION DES VARIABLES GLOBALES    #
#########################################



#########################################
#       DEFINITION DES FONCTIONS        #
#########################################

racine = tk.Tk() # Création de la fenêtre racine
bouton = tk.Button(text="Ouverture de la fenetre", 
                        font = ("Helvetica", "20")
                        )
bouton.grid(column=0, row=1)
canvas = tk.Canvas(racine, bg="Black", height=HEIGHT, width=WIDTH)
canvas.grid(column=0, row=0)
def lignes(n):
    x=HEIGHT/n/2
    y=WIDTH/n/2
    for i in range(n):
        ligne= canvas.create_line(HEIGHT/n*i,0,WIDTH/n*i,500, fill="white")
        text= canvas.create_text(x,y,text="a",fill ="white")
        ligne1= canvas.create_line(0,HEIGHT/n*i,500,WIDTH/n*i, fill="white")
lignes(5)

racine.mainloop() # Lancement de la boucle principale 