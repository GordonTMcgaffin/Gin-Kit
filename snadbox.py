import numpy as np

if __name__ == "__main__":
    print("Hi")
    distances = [(1, 2), (1, 4), (5, 3), (6, 2)]
    print(sorted(distances, key=lambda x: x[1]))
