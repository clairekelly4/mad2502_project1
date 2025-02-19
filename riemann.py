import numpy as np
def left_endpoint(x_vals: np.ndarray, func: np.ufunc):
    dist = x_vals[:-1] - x_vals[1:]
    return np.sum(dist * func(x_vals[-1]))

def trapezoid (x_vals: np.ndarray, func: np.ufunc):
    dist = x_vals[:-1] - x_vals[1:]
    return np.sum((func(x_vals[:-1]) + func(x_vals[1:]))/2 * dist)

def simpson (x_vals: np.ndarray, func: np.ufunc):
    dist = x_vals[:-1] - x_vals[1:]
    return np.sum((1/6) * (func(x_vals[:-1]) + 4 * func((x_vals[:-1] + x_vals[1:])/2) + func(x_vals[1:])) * dist)