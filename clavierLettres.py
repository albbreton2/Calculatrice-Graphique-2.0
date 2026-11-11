import customtkinter as ctk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from clavierAccueil import buttonClick
from MathConstante import MathConstante
from MathConstante import MathFonction

class ClavierLettres(ctk.CTkFrame):
    def __init__(self, master=None, on_key=None):
        super().__init__(master)
        self.master = master #Clavier
        self.on_key = on_key #fonction fournie par la page
        self.create_widgets()

    def create_widgets(self):
        ####################################
        ## section des lettres du clavier ##
        ####################################

        letters= ['q','w','e','r','t','y','u','i','o','p',
                  'a','s','d','f','g','h','j','k','l',
                  ' ▲ ','z','x','c','v','b','n','m'] #liste des lettres du clavier
        lettersButtons = [] #liste des boutons du clavier

        for letter in letters:
            lettersButtons.append(ctk.CTkButton(self, text=letter, command=lambda btn=letter: buttonClick(btn, self.on_key), height=20, width=60))
        lettersButtons.append(ctk.CTkButton(self, text='⌫', command=lambda: backspaceButton(self.on_key), height=20, width=60))

        col, row = 0, 0 #compteurs
        for i in range(len(lettersButtons)):
            if col == 10 and row == 0:  #pour que ce soit placé selon la bonne ligne et colonne
                col, row = 0, 1
            if col == 9 and row == 1:
                col, row = 0, 2
            lettersButtons[i].grid(row=row, column=col, pady=(5,5), padx=(5,5)) #
            col += 1
        lettersButtons[19].configure(command=lambda: capitalizeLetters(lettersButtons, self.on_key)) #Pour mettre en majuscule/minuscule

#supprime le dernier caractère entré
def backspaceButton(on_key):
    on_key("⌫")

#met en majuscules ou en minuscules
def capitalizeLetters(lettersBtn, on_key):
    ###############################################
    ##Pour mettre en majuscules ou en minuscules:##
    ###############################################
    for i in lettersBtn:
        if i.cget("text").isalpha(): #si c'est une lettre
            if i.cget("text").isupper(): #si l'attribut text du bouton est en majuscules
                lowerLetter = i.cget("text").lower() #mettre en minuscule
                i.configure(text = lowerLetter, command=lambda lettre=lowerLetter: buttonClick(lettre, on_key))
            else: #si l'attribut text du bouton est en minuscules
                upperLetter = i.cget("text").upper() #mettre en majuscules
                i.configure(text = upperLetter, command=lambda lettre=upperLetter: buttonClick(lettre, on_key))
