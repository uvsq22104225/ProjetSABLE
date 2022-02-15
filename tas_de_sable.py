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


import tkinter as Tk


#########################################
#       DEFINITION DES CONSTANTES       #
#########################################



#########################################
#  DEFINITION DES VARIABLES GLOBALES    #
#########################################


#########################################
#       DEFINITION DES FONCTIONS        #
#########################################


import tkinter as tk

HEIGHT = 500
WIDTH = 500

def bouge_cercle():
    canvas.move(cercle, 50, 50) # méthode qui déplace l'objet cercle

racine = tk.Tk() # Création de la fenêtre racine
bouton = tk.Button(text="déplace cercle", 
                    command=bouge_cercle, font = ("Helvetica", "30")
                  )
bouton.grid(column=0, row=1)
canvas = tk.Canvas(racine, bg="red", height=HEIGHT, width=WIDTH)
canvas.grid(column=0, row=0)
# on récupère l'identifiant du cercle:
cercle = canvas.create_oval((100, 100), (300, 300), fill="blue", width=5, outline="cyan") 
racine.mainloop() # Lancement de la boucle principale