import plotly.express as px
import numpy as np

colours_list = [
    "aliceblue",
    "antiquewhite",
    "aqua",
    "aquamarine",
    "azure",
    "beige",
    "bisque",
    "black",
    "blanchedalmond",
    "blue",
    "blueviolet",
    "brown",
    "burlywood",
    "cadetblue",
    "chartreuse",
    "chocolate",
    "coral",
    "cornflowerblue",
    "cornsilk",
    "crimson",
    "cyan",
    "darkblue",
    "darkcyan",
    "darkgoldenrod",
    "darkgray",
]


def int_to_colour(int_colors: list) -> list:
    return [colours_list[colour] for colour in int_colors]


def plot_points_coloured(points: np.Array, colors: list, reduce: bool):
    if len(points.shape()) == 2:
        print("Plotting 2D")
    elif len(points.shape()) == 3:
        print("Plotting 3D")
    elif reduce:
        print("Reducing dimesnsions for plotting")
    else:
        print("Invalid dimesnsions for plotting. Reduce flag not set")
    pass
