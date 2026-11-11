import customtkinter as ctk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from MathConstante import MathConstante
from MathConstante import MathFonction

class ClavierAccueil(ctk.CTkFrame):
    def __init__(self, master=None, on_key=None):
        super().__init__(master)
        self.master = master #Clavier
        self.on_key = on_key #fonction fournie par la page
        self.create_widgets()

    def create_widgets(self):
        listeOperateurs = ['x', 'y', MathConstante("pi"), MathConstante("e"),
                           '²', MathFonction("**"), MathFonction("sqrt"), MathFonction("absolute"),
                           '(', ')', '<', '>',
                           MathFonction("cbrt"), ',' ,'≤' ,'≥']
        listeBoutons1 = []

        for symbole in listeOperateurs:
            listeBoutons1.append(ctk.CTkButton(self, text=str(symbole), command=lambda btn=symbole: buttonClick(btn, self.on_key), height=20, width=80))

        count, padx3 = 0, 5
        for i in range(4):
            for j in range(0,4):
                if j == 4:
                    padx3 = 15
                else:
                    padx3 = 5
                if count<len(listeOperateurs):
                    listeBoutons1[count].grid(row=i, column=j, pady=(5,5), padx=(padx3,5))
                    count += 1

        chiffres = [7,8,9,'÷',4,5,6,'×',1,2,3,'-',0,'.','=','+']
        chiffresBoutons = []

        for chiffre in chiffres:
            chiffresBoutons.append(ctk.CTkButton(self, text=str(chiffre), command=lambda btn=chiffre: buttonClick(btn, self.on_key), height=20, width=80))

        count, padx4 = 0, 5
        for i in range(4):
            for j in range(4,8):
                if j == 4:
                    padx4 = 15
                else:
                    padx4 = 5
                if count<len(chiffres):
                    chiffresBoutons[count].grid(row=i, column=j, pady=(5,5), padx=(padx4,5))
                    count += 1

#quand on clique sur la touche, ça envoie la touche à la page (on_key)
def buttonClick(symbole, on_key):
    on_key(str(symbole))
