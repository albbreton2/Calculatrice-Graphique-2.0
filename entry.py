import customtkinter as ctk
import tkinter as tk

class Entry(ctk.CTkFrame):
    def __init__(self, master=None, width=400):
        super().__init__(master, width)
        self.master = master #MainApp
        self.entries = [] #Liste des entries
        self.entryCourant = None #entry courant
        self.create_widgets()
        

    def create_widgets(self):
        for i in range(18):
            self.entries.append(ctk.CTkEntry(self, width=400))
        for i in range(18):
            self.entries[i].grid(row=i,column=0,sticky='new')
        for i in range(18):
            self.entries[i].bind("<FocusIn>", self.on_focus)     

    def on_focus(self, event):
        self.entryCourant = event.widget
