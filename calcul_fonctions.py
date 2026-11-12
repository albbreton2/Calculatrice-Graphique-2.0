import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox

def tracer_graphique(fonctions, x_min=-10, x_max=10):
    x = np.linspace(x_min, x_max, 500)
    #x = np.linspace(-100,100,1000) #pour que ça ait l'air infini

    plt.figure(figsize=(10, 6))

    result=[]

    fonctionsPossibles={
        "÷": "/",
        "×": "*",
        "π": "np.pi",
        "∞": "np.inf",
        "√": "np.sqrt",
        "∛": "np.cbrt",
        "⌊x⌋": "np.floor(x)",
        "⌈x⌉": "np.ceil(x)",
        "eˣ": "np.exp(x)",
        "ln": "np.log",
        "log₁₀": "np.log10",
        "log₂": "np.log2",
        "|x|": "np.absolute(x)",
        "arcsin": "np.arcsin",
        "arccos": "np.arccos",
        "arctan": "np.arctan",
        "arccsc": "1/np.arcsin",
        "arcsec": "1/np.arccos",
        "arccot": "1/np.arctan",
        "²": '**2',
        "ˣ": "**(x)",
        "deg": "np.degrees",
        "rad": "np.radians",
        "≤": "<=",
        "≥": ">="
        }
    
    for fonction in fonctions:
        fonction = check_sinus(fonction)
        for i in fonctionsPossibles.keys():
            if i in fonction: #si c'est dans la fonction, remplacer par la version évaluable
                fonction = fonction.replace(i, fonctionsPossibles[i])

        peutEtreEvalue = False #Si la fonction peut-être évaluée, c'est vrai, sinon, c'est faux
    
        try:
            y = eval(fonction)
            if np.isscalar(y):
                y = np.full_like(x, y)
            peutEtreEvalue = True
        except (ValueError, TypeError, SyntaxError, NameError, ZeroDivisionError):
            peutEtreEvalue = False
            messagebox.showerror("Erreur", "La fonction est invalide") 
            print("Erreur dans la fonction :", fonction)

        if peutEtreEvalue: #S'affiche seulement si c'est évaluable, sinon rien ne s'affiche pour éviter une erreur
            result.append((x,y))
    return result

def check_sinus(fonction):
    fonctionsSinus = {
        "sin": 'np.sin',
        "cos": 'np.cos',
        "tan": "np.tan",
        "csc": "1/np.sin",
        "sec": "1/np.cos",
        "cot": "1/np.tan"
    }
    for sinus in fonctionsSinus.keys():
        if sinus in fonction:
            for i in range(len(fonction)):
                if i<(len(fonction)-2) and fonction[i]+fonction[i+1]+fonction[i+2]==sinus:
                    if fonction[i-3]+fonction[i-2]+fonction[i-1] != "arc" and fonction[i-3]+fonction[i-2]+fonction[i-1] != "np.":
                        fonction = fonction[:i]+fonctionsSinus[sinus]+fonction[i+3:]
    return fonction

def checkAbsolute(fonction):
    nombre = int(fonction.count("|")/2) #nombre de fois qu'il y a "| |" (s'il y en a un nombre impair faut throw error)
    positions = [] #chaque position de valeurs absolues
    first = fonction.index("|") #premier index
    last = fonction.rindex("|") #dernier index
    positions.extend([first,last]) #ajoute à l'array

    for i in range (nombre-1): #prendre les positions de toutes les instances
        first = first+1+fonction[first+1:last].index("|")
        last = first+fonction[first:last-1].rindex("|")
        print(first, last)
        positions.extend([first, last])
    
    positions.sort() #classe en ordre
    ### À CONTINUER ###