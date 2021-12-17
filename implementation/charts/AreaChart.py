import matplotlib.pyplot as plt

class AreaChart:
    def __init__(self, x, y, colortofill, colortoline, alpha=0.2):
        self.x = x
        self.y = y
        self.colortofill = colortofill
        self.colortoline = colortoline
        self.alpha = alpha

    def run(self):
        plt.fill_between(self.x, self.y, color=self.colortofill, alpha=self.alpha)
        plt.plot(self.x, self.y, color=self.colortoline, alpha=self.alpha)

        # Show graph
        plt.show()
