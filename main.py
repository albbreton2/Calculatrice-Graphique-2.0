import customtkinter as ctk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from clavier import Clavier
from entry import Entry
from visuel import Visuel


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculatrice graphique")
        self.geometry("1280x800")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.axe1 = np.linspace(-10, 10, 100)
        self.axe2 = self.axe1 ** 2

        self.page = None
        self.create_menu()
        self.show_calculatrice()

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def afficheEntries(self):
        self.entries = Entry(master=self, width=400)
        self.entries.grid(row=0, column=0, sticky="nw")

    def afficheClavier(self):
        clavier = Clavier(master=self)
        clavier.grid(row=2, column=0, columnspan=2, sticky="sew")

    def changeEntry(self, symbole):
        if self.entries.entryCourant is not None:
            current = str(self.entries.entryCourant.get())
            pos = self.entries.entryCourant.index("insert")
            self.entries.entryCourant.delete(0, tk.END)

            entryText = ""
            if current == "":
                entryText += str(symbole)
            elif pos == len(current):
                entryText = current + str(symbole)
            else:
                for i in range(len(current)):
                    if i == pos:
                        entryText += str(symbole)
                        entryText += current[i]
                    else:
                        entryText += current[i]

            self.entries.entryCourant.insert(0, entryText)

    def backspaceEntry(self):
        if self.entries.entryCourant is not None:
            current = str(self.entries.entryCourant.get())
            pos = self.entries.entryCourant.index("insert")
            self.entries.entryCourant.delete(0, tk.END)

            entryText = ""
            for i in range(len(current)):
                if i != pos - 1:
                    entryText += current[i]

            self.entries.entryCourant.insert(0, entryText)

    def _afficher(self, page):
        if self.page is not None:
            self.page.destroy()

        self.page = page
        self.page.grid(row=0, column=0, sticky="nsew")

    #def show_accueil(self):
        #self._afficher(Accueil(self, axe1=self.axe1, axe2=self.axe2))

    def show_calculatrice(self):
        self._afficher(Visuel(self))

    def create_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Quitter", command=self.on_closing)

        view_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Affichage", menu=view_menu)
        view_menu.add_command(label="Calculatrice", command=self.show_calculatrice)
        #view_menu.add_command(label="Accueil (exercice)", command=self.show_accueil)

    def on_closing(self):
        self.quit()
        self.destroy()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()