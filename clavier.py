import customtkinter as ctk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from MathConstante import MathConstante
from MathConstante import MathFonction
from clavierAccueil import ClavierAccueil
from clavierLettres import ClavierLettres
from clavierFonctions import ClavierFonctions


class Clavier(ctk.CTkFrame):
    def __init__(self, master=None, on_key=None):
        super().__init__(master)
        self.master = master
        self.on_key = on_key
        self.grid_columnconfigure(2, weight=1)
        self.create_widgets()
        self.showClavierAccueil()

    def showClavierAccueil(self):
        self.clearClavierFrame()
        self.clavierAccueil = ClavierAccueil(self, on_key=self.on_key)
        self.clavierAccueil.grid(row=1, column=0, columnspan=20, sticky='s')

    def showClavierLettres(self):
        self.clearClavierFrame()
        self.clavierLettres = ClavierLettres(self, on_key=self.on_key)
        self.clavierLettres.grid(row=1, column=0, columnspan=30, sticky='s')

    def showClavierFonctions(self):
        self.clearClavierFrame()
        self.clavierFonctions = ClavierFonctions(self, on_key=self.on_key)
        self.clavierFonctions.grid(row=1, column=0, columnspan=30, sticky='s')
    '''
    def showClavierAutre(self):
        self.clearClavierFrame()
        self.clavierAutre = ClavierAutre(self)
    '''
    def clearClavierFrame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_widgets()

    def create_widgets(self):
        boutonAccueil = ctk.CTkButton(self, text="123", command = self.showClavierAccueil, height=20, width=40)
        boutonAccueil.grid(row=0, column=0, pady=(5,5), padx=(5,5), sticky="w")

        boutonLettres = ctk.CTkButton(self, text="ABC", command = self.showClavierLettres, height=20, width=40)
        boutonLettres.grid(row=0, column=1, pady=(5,5), padx=(5,5), sticky="w")

        boutonFonctions = ctk.CTkButton(self, text="f(x)", command = self.showClavierFonctions, height=20, width=40)
        boutonFonctions.grid(row=0, column=2, pady=(5,5), padx=(5,5), sticky="w")
