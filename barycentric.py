import numpy as np

def get_barycentric_coordinates(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> np.ndarray:
    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]
    x, y = point_coordinates[0], point_coordinates[1]
    l1 = ((x2 - x) * (y3 - y) - (x3 - x) * (y2 - y)) / ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    l2 = ((x3 - x) * (y1 - y) - (x1 - x) * (y3 - y)) / ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    l3 = 1 - l1 - l2
    return np.array([l1, l2, l3])

def get_cartesian_coordinates(triangle_coordinates: np.ndarray, barycentric_coordinates: np.ndarray) -> np.ndarray:
    return np.dot(triangle_coordinates, barycentric_coordinates)

def is_inside_triangle(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> bool:
    lambdas = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
    return np.all(lambdas >= 0)
