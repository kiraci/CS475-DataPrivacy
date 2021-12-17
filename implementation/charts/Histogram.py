import matplotlib.pyplot as plt
import numpy as np


class Histogram:
    def __init__(self, x, y, title, xlabel, ylabel, color):
        self.x = x
        self.y = y
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.color = color
        self.xpos = np.arange(len(self.x))

    def run(self):
        # Create bars and choose color
        plt.bar(self.xpos, self.y, color=self.color)

        # Add title and axis names
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        # Create names on the x-axis
        plt.xticks(self.xpos, self.x)

        # Show graph
        plt.show()
