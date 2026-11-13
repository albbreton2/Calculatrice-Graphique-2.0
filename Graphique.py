import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import customtkinter as ctk


class Graphique(ctk.CTkFrame):
    def __init__(self, master, avec_barre=True):
        super().__init__(master)
        self.fig = Figure(figsize=(6, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.barre = None
        if avec_barre:
            cadre_barre = ctk.CTkFrame(self)
            cadre_barre.pack(side="bottom", fill="x")
            self.barre = NavigationToolbar2Tk(self.canvas, cadre_barre, pack_toolbar=False)
            self.barre.grid(row=0, column=0, sticky="w")
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        self.fenetre = (-10, 10, -10, 10)
        self.artistes_geo = []   
        self.on_clic = None     
        self.canvas.mpl_connect("button_press_event", self._clic)
        self._axes()

    def _axes(self):
        xmin, xmax, ymin, ymax = self.fenetre
        self.ax.set_xlim(xmin, xmax)
        self.ax.set_ylim(ymin, ymax)
        self.ax.grid(True, alpha=0.3)
        self.canvas.draw()
        if self.barre:
            self.barre.update()

    def tracer(self, xs, ys, couleur="tab:blue"):
        self.ax.plot(xs, ys, color=couleur)
        self.canvas.draw()

    def tracer_implicite(self, xs, ys, eq, couleur="tab:blue"):
        self.ax.contour(xs,ys,eq,[0])
        self.canvas.draw()

    def effacer(self):
        self.ax.clear()
        self.artistes_geo = []
        self._axes()

    
    def _clic(self, event):
        if event.inaxes != self.ax or event.button != 1:
            return
        
        if self.barre is not None and self.barre.mode != "":
            return
        if self.on_clic:
            self.on_clic(event.xdata, event.ydata)

    def indice_point_proche(self, points, x, y, rayon=10):
        """Retourne l'indice du point à moins de `rayon` pixels de (x, y), sinon None."""
        cx, cy = self.ax.transData.transform((x, y))
        for k, (px, py) in enumerate(points):
            ppx, ppy = self.ax.transData.transform((px, py))
            if (ppx - cx) ** 2 + (ppy - cy) ** 2 <= rayon ** 2:
                return k
        return None

    def dessiner_geometrie(self, points, selection, segments):
        for a in self.artistes_geo:
            a.remove()
        self.artistes_geo = []

        for i, j in segments:
            (x1, y1), (x2, y2) = points[i], points[j]
            ligne, = self.ax.plot([x1, x2], [y1, y2], color="tab:green", linewidth=2)
            longueur = math.hypot(x2 - x1, y2 - y1)
            texte = self.ax.annotate(f"{longueur:.2f}", ((x1 + x2) / 2, (y1 + y2) / 2),
                                     textcoords="offset points", xytext=(0, 6),
                                     ha="center", color="tab:green")
            self.artistes_geo += [ligne, texte]

        for k, (x, y) in enumerate(points):
            couleur = "tab:orange" if k in selection else "tab:red"
            point, = self.ax.plot(x, y, "o", color=couleur, markersize=8)
            nom = self.ax.annotate(chr(65 + k % 26), (x, y),
                                   textcoords="offset points", xytext=(7, 7))
            self.artistes_geo += [point, nom]

        self.canvas.draw()

#brouillon méthode à créer = axes, tracer, effacer, peut-être zoom, exporter le graphique/ enregistrer, geometrie pour segments
