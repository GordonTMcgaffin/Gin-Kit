import numpy as np


def label_point(distance_func: function, points: list, labels: list, point: list, n_neighbors: int):
    distances = []
    for label, point_j in zip(labels, points):
        distances.append([label, distance_func(point, point_j)])

    distances = sorted(distances, key=lambda x: x[1])
    k_nearest_neighbors = distance_func[:n_neighbors]
    return np.mean([pair[0] for pair in k_nearest_neighbors])
