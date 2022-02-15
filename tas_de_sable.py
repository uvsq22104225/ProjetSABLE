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

racine = tk.Tk() # Création de la fenêtre racine
bouton = tk.Button(text="Ouverture de la fenetre", 
                        font = ("Helvetica", "20")
                        )
bouton.grid(column=0, row=1)
canvas = tk.Canvas(racine, bg="Black", height=HEIGHT, width=WIDTH)
canvas.grid(column=0, row=0)
# on récupère l'identifiant du cercle:
Ligne = canvas.create_line(166,0,166,500, fill="white", width=5) 
racine.mainloop() # Lancement de la boucle principale 