import numpy as np

class Distance:
    def Euclidean_distance(point_a, point_b):
        diff = point_a - point_b
        return np.sqrt(np.einsum("ij,ij->j", diff, diff))

    functions = {"euclidean": Euclidean_distance()}

    def get_function_list(self):
        return self.functions.keys

    def get_function_by_name(self, name: str):
        return self.functions[name]
