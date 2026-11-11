import numpy as np
import matplotlib.pyplot as plt

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
        "√x": "np.sqrt(x)",
        "∛x": "np.cbrt(x)",
        "⌊x⌋": "np.floor(x)",
        "⌈x⌉": "np.ceil(x)",
        "eˣ": "np.exp(x)",
        "ln": "np.log",
        "log₁₀": "np.log10",
        "log₂": "np.log2",
        "|x|": "np.absolute(x)",
        "sin(x)": 'np.sin(x)',
        "cos(x)": 'np.cos(x)',
        "tan(x)": "np.tan(x)",
        "csc(x)": "(1/np.sin(x))",
        "sec(x)": "(1/np.cos(x))",
        "cot(x)": "(1/np.tan(x))",
        "arcsin(x)": "np.arcsin(x)",
        "arccos(x)": "np.arccos(x)",
        "arctan(x)": "np.arctan(x)",
        "arccsc(x)": "(1/np.arcsin(x))",
        "arcsec(x)": "(1/np.arccos(x))",
        "arccot(x)": "(1/np.arctan(x))",
        "²": '**2',
        "ˣ": "**(x)",
        "deg": "np.degrees",
        "rad": "np.radians",
        "≤": "<=",
        "≥": ">="
        }
    
    for fonction in fonctions:
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
            print("Erreur dans la fonction :", fonction)

        if peutEtreEvalue: #S'affiche seulement si c'est évaluable, sinon rien ne s'affiche pour éviter une erreur
            result.append((x,y))
    return result