import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class AnimationGrafic:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.artics = []
        self.ani = object

    def append(self, values, destac):
        colors = []
        for i in range(len(values)):
            colors.append("tab:green")
            if i == destac: 
                colors[i] = "tab:red"

        container = self.ax.bar(range(len(values)), values, color=colors)
        self.artics.append(container)

    def render(self, interval=400):
        self.ani = animation.ArtistAnimation(fig=self.fig, artists=self.artics, interval=interval)

    def show(self):
        plt.show()

    def save(self, name="save.gif"):
        self.ani.save(filename=f"./{name}", writer="pillow")
