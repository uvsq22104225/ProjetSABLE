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


import tkinter as tk


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

def canevas():
    """ Initilise le terrain de la manière suivante:
    * met à 0 la liste appelée terrain à 2D qui contient pour chaque case la 
    valeur 1 si il y a un mur, et 0 sinon
    * initialise la liste grille à 2D qui contient l'identifiant
    du carré dessiné sur le canevas pour chaque case 
    """
    racine = tk.Tk() # Création de la fenêtre racine
    bouton = tk.Button(text="ouverture de la fenetre", 
                        font = ("Helvetica", "20")
                        )
    bouton.grid(column=0, row=1)
    canvas = tk.Canvas(racine, bg="red", height=HEIGHT, width=WIDTH)
    canvas.grid(column=0, row=0)
    # on récupère l'identifiant du cercle:
    cercle = canvas.create_oval((100, 100), (300, 300), fill="blue", width=5, outline="cyan") 
    racine.mainloop() # Lancement de la boucle principale