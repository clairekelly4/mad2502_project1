import numpy as np

def get_barycentric_coordinates(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> np.ndarray:
    x1, x2, x3 = triangle_coordinates[0] # sets the three numbers in first row of array to x1, x2, and x3 for calculations
    y1, y2, y3 = triangle_coordinates[1] # sets the three numbers in second row of array to y1, y2, and y3 for calculations
    x, y = point_coordinates[0], point_coordinates[1] # assigns the x point coordinate to x and y point coordinate to y
    l1 = ((x2 - x) * (y3 - y) - (x3 - x) * (y2 - y)) / ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) # calculates lambda 1
    l2 = ((x3 - x) * (y1 - y) - (x1 - x) * (y3 - y)) / ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) # calculates lambda 2
    l3 = 1 - l1 - l2 # calculates lamba 3
    return np.array([l1, l2, l3])

def get_cartesian_coordinates(triangle_coordinates: np.ndarray, barycentric_coordinates: np.ndarray) -> np.ndarray:
    return np.dot(triangle_coordinates, barycentric_coordinates) # uses the numpy dot product function to calculate cartesian coordinates

def is_inside_triangle(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> bool:
    lambdas = get_barycentric_coordinates(triangle_coordinates, point_coordinates) # calls on get_barycentric_coordinates function to return lambda values
    return np.all(lambdas >= 0) # checks each lambda value to ensure it is non-negative and will return true value if all are non-negative and false otherwise
