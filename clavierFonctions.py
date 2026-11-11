import customtkinter as ctk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from clavierAccueil import buttonClick
from MathConstante import MathConstante
from MathConstante import MathFonction

class ClavierFonctions(ctk.CTkFrame):
    def __init__(self, master=None, on_key=None):
        super().__init__(master)
        self.master = master #Clavier
        self.on_key = on_key #fonction fournie par la page
        self.create_widgets()

    def create_widgets(self):
        listeFonctions = [
            MathFonction("sin"), MathFonction("cos"),MathFonction("tan"),
            MathFonction("log"), MathFonction("log10"), MathFonction("log2"),

            MathFonction("csc"), MathFonction("sec"), MathFonction("cot"),
            '{',                '}',                  MathFonction("ceil"),

            MathFonction("arcsin"), MathFonction("arccos"), MathFonction("arctan"),
            '[',                    ']',                    MathFonction("floor"),

            MathFonction("arccsc"), MathFonction("arcsec"), MathFonction("arccot"),
            MathFonction("degrees"), MathFonction("radians")
            ]
        boutonsFonctions = []
        for symbole in listeFonctions:
            boutonsFonctions.append(ctk.CTkButton(self, text=str(symbole), command=lambda btn=symbole: buttonClick(btn, self.on_key), height=20, width=80))

        count, padx3 = 0, 5
        for i in range(4):
            for j in range(0,6):
                if j == 2 or j == 3:
                    padx3 = 15
                else:
                    padx3 = 5
                if count<len(listeFonctions):
                    boutonsFonctions[count].grid(row=i, column=j, pady=(5,5), padx=(padx3,5))
                    count += 1
