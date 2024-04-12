from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import config
import delone_triangulation
from ErrorWindow import ErrorWindow
from DiagramWindow import DiagramWindow

import numpy as np

class GraphWindow(Tk):
    def __init__(self):
        super().__init__()
        self.button_build = Button(self, text="Построить эпюру", command=self.err)
        self.button_build.pack(fill=X)

        self.x = np.array([i[0] for i in config.data])
        self.y = np.array([i[1] for i in config.data])
        self.z = np.array([i[2] for i in config.data])

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        scatter = self.ax.scatter(self.x, self.y, s=60, c=self.z, cmap='jet', picker=len(config.data))
        legend1 = self.ax.legend(*scatter.legend_elements(), title="R")
        self.ax.add_artist(legend1)

        self.flag = 0

        self.start = [0, 0, 0]
        self.end = [0, 0, 0]

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas.callbacks.connect('pick_event', self.on_pick)

    def on_pick(self, event):
        artist = event.artist
        xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
        #x, y = artist.get_xdata(), artist.get_ydata()
        ind = event.ind
        print('Artist picked:', event.artist)
        print('{} vertices picked'.format(len(ind)))
        print('Pick between vertices {} and {}'.format(min(ind), max(ind) + 1))
        print('x, y of mouse: {:.2f},{:.2f}'.format(xmouse, ymouse))
        #print('Data point:', x[ind[0]], y[ind[0]])
        print()
        if self.flag == 0:
            self.start = config.data[min(ind)]
            self.flag = 1
        elif self.flag == 1:
            self.end = config.data[min(ind)]
            self.flag = 3
            x1 = np.linspace(self.start[0], self.end[0], 20)
            y1 = np.linspace(self.start[1], self.end[1], 20)
            points = []
            values = []
            for i in config.data:
                points.append(i[:2])
                values.append(i[2])
            print(points)
            p = []
            for i in range(20):
                p.append([x1[i], y1[i]])
            p_points = delone_triangulation.delone_triangulation(points, np.array(values), p, 2)

            self.x = np.array(list(self.x) + list(x1)[1:19])
            self.y = np.array(list(self.y) + list(y1)[1:19])
            self.z = np.array(list(self.z) + p_points[1:19])
            self.ax.plot(x1, y1)
            self.ax.scatter(self.x, self.y, s=60, c=self.z,  cmap='jet')
            ep = lambda i=list(x1), j=p_points: self.epure(i, j)
            self.button_build.config(command=ep)

            self.canvas.draw()

    def err(self):
        error = ErrorWindow(self, config.errorTextInterpolate)

    def epure(self, x, z):
        d = DiagramWindow(x, z)
        d.iconbitmap("data/test_axe.ico")
        d.mainloop()
