from PauLie import *

if __name__ == '__main__':
    animationAntiCommutationGraph(["XYI", "IXY", "XZY"], storage={"filename":"data/example_a.html", "writer":"html"})
    animationAntiCommutationGraph(["XY", "XZ"], size = 4, storage={"filename": "data/example_b.html", "writer": "html"})
