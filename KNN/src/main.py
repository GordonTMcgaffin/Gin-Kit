import numpy as np
import random
from distance_functions import Distance


class KNN:

    number_classes = 0
    number_neighbors = 0
    points = []
    labels = []

    def __init__(self, points: list, labels: list, number_classes: int) -> None:
        self.points = points

        if labels == None and number_classes == None:
            raise Exception("Data labels or number of class labels must be provided")

        if labels != None:
            self.labels = labels
        else:
            # No labels are provided so we randomly assign labels to the data
            self.assign_random_data(number_classes)

        if number_classes != None:
            self.number_classes = number_classes
        else:
            # No number of labels was received so we get it from the labels
            self.number_classes = np.max(self.labels)
        pass

    def fit(self, iterations: int, number_neighbors: int, distance_function) -> list:
        if type(distance_function) == str:
            function = Distance.get_function_by_name(distance_function)
            if function != None:
                return self.label_data_points(function, iterations, number_neighbors)
            else:
                raise Exception(
                    f"Could not find distance function: {distance_function} \nDistance functions include:"
                    f" {Distance.get_function_list()}"
                )
        else:
            return self.label_data_points(distance_function, iterations, number_neighbors)

    def label_data_points(self, distance_func: function, iterations: int, number_neighbors: int):
        for i in range(iterations):
            new_labels = []
            for point in self.points:
                new_labels.append(self.label_point(distance_func=distance_func, point=point))
            self.labels = new_labels

    def label_point(self, distance_func: function, point: list, number_neighbors: int):
        distances = []
        for label, point_j in zip(self.labels, self.points):
            if point_j != point:
                distances.append([label, distance_func(point, point_j)])

        distances = sorted(distances, key=lambda x: x[1])
        k_nearest_neighbors = distance_func[: self.number_neighbors]
        return np.mean([pair[0] for pair in k_nearest_neighbors])

    def assign_random_data(self, number_classes: int) -> list:
        for i in range(len(self.points)):
            self.labels.append(random.randint(0, number_classes))
