import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox

def tracer_graphique(fonctions, x_min=-10, x_max=10):
    #x = np.linspace(x_min, x_max, 500)
    x = np.linspace(-100,100,1000) #pour que ça ait l'air infini

    plt.figure(figsize=(10, 6))

    result=[]

    fonctionsPossibles={
        "÷": "/",
        "×": "*",
        "π": "np.pi",
        "∞": "np.inf",
        "√": "np.sqrt",
        "∛": "np.cbrt",
        "eˣ": "np.exp(x)",
        "ln": "np.log",
        "log₁₀": "np.log10",
        "log₂": "np.log2",
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
        fonction = check_sinus(fonction) #empêcher que des "np.arcnp.cos(x)" n'apparaissent

        #pour vérifier si jamais x!=x mais plutôt x² ou x+1, par exemple
        fonction = checkAbsolute(fonction)
        fonction = checkPlancherPlafond(fonction, ["⌊","⌋"])
        fonction = checkPlancherPlafond(fonction, ["⌈","⌉"])

        for i in fonctionsPossibles.keys():
            if i in fonction: #si c'est dans la fonction, remplacer par la version évaluable
                fonction = fonction.replace(i, fonctionsPossibles[i])

        if "y" and "x" and "=" in fonction: #vérifier s'il y a y et = pour savoir si c'est implicite
            y = np.linspace(-10,10,1000)
            xv, yv = np.meshgrid(x,y)
            #met tout du même côté de l'équation
            fonction=fonction[:fonction.find("=")]+"-"+fonction[fonction.find("=")+1:]
            #remplace
            fonction=fonction.replace("y","yv")
            fonction=fonction.replace("x","xv")
            eq = eval(fonction)
            #x devient (x,y) et y devient eq basically
            result.append(((xv,yv),eq))

        peutEtreEvalue = False #Si la fonction peut-être évaluée, c'est vrai, sinon, c'est faux
        try:
            y = eval(fonction)
            if np.isscalar(y): #si c'est un scalaire ça va être une ligne horizontale
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
            for i in range(len(fonction)): #vérifie si les 3 lettres avant la clef sont "arc"
                if i<(len(fonction)-2) and fonction[i]+fonction[i+1]+fonction[i+2]==sinus:
                    if fonction[i-3]+fonction[i-2]+fonction[i-1] != "arc" and fonction[i-3]+fonction[i-2]+fonction[i-1] != "np.":
                        fonction = fonction[:i]+fonctionsSinus[sinus]+fonction[i+3:]
    return fonction

def checkAbsolute(fonction):
    fonctionSplit = fonction.split('|') #crée une liste de tous ce qui n'est pas "|"
    result = ""
    for i in range(len(fonctionSplit)): #pour chaque élément de la liste
        if i%2==0: #si c'est impair (donc c'est avant le x)
            if i == len(fonctionSplit)-1: #on veut pas que ça termine en "np.absolute("
                result+=fonctionSplit[i]+""
            else: #sinon rajouter car une autre parenthèse va être ajoutée anyways
                result+=fonctionSplit[i]+"np.absolute("
        else:
            result+=fonctionSplit[i]+")" #ajout de la parenthèse après le x
    return result

def checkPlancherPlafond(fonction,symboles):
    fonctionStr = ""

    #vérification des symboles
    if symboles[0] == "⌊":
        fonctionStr = "np.floor("
    elif symboles[0] == "⌈":
        fonctionStr = "np.ceil("

    #
    if symboles[0] and symboles[1] in fonction:
        fonctionSplit = fonction.split(symboles[0]) #crée une liste de tous ce qui est pas symbole
        result = ""
        for i in range (len(fonctionSplit)):
            if i%2==0:
                result+=fonctionSplit[i]+fonctionStr
            else:
                result+=fonctionSplit[i]
        fonctionSplit = result.split(symboles[1])
        result = ""
        for i in range(len(fonctionSplit)):
            if i%2==0:
                result+=fonctionSplit[i]
            else:
                result+=fonctionSplit[i]+")"
        return result
    else:
        return fonction