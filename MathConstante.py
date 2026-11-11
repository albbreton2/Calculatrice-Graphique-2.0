import numpy as np

#pour les constantes du genre infini, pi, e, etc
# ex: pi = MathConstante("pi")
#input de print(pi) -> π
#ce que pi.operation fait -> np.pi()
#input de pi.operation() -> 3.141592653589793
class MathConstante:
    def __init__(self, nom):
        self.nom = nom
        self.symboles = {
            "pi" : "π",
            "inf" : "∞",
            "sqrt" : "√",
            "cbrt" : "∛",
            "floor" : "⌊ ⌋",
            "ceil" : "⌈ ⌉",
            "exp" : "eˣ",
            "log" : "ln",
            "log10" : "log₁₀",
            "log2" : "log₂",
            "absolute" : "| |",
            "**" : "ˣ",
            "**2" : "a²",
            "degrees" : "deg",
            "radians" : "rad"
            }

    def __str__(self):
        if self.nom in self.symboles:
            return self.symboles[self.nom]
        else:
            return self.nom
    def operation(self):
        result = getattr(np, self.nom)
        return result

#hérite de MathConstante, sert pour les fonctions sinusoïdales, exponentielles, logarithmes, etc
#ex: sin = MathFonction("sin")
#input de print(sin) -> sin
#input de sin.operation(x) si x = 1 -> 0.8414709848078965
class MathFonction(MathConstante):
    def __init__(self, nom):
        MathConstante.__init__(self, nom)
    def operation(self, x):
        sinusInverse = {'csc':'sin', 'sec':'cos', 'cot': 'tan'}
        arcInverse = {'arccsc':'arcsin', 'arcsec':'arccos', 'arccot':'arctan'}
        if self.nom in sinusInverse.keys():
            result = getattr(np, sinusInverse[self.nom])
            return 1/result(x)
        elif self.nom in arcInverse.keys():
            result = getattr(np, arcInverse[self.nom])
            return result(1/x)
        else:
            result = getattr(np, self.nom)
            return result(x)
