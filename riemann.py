import numpy as np
def left_endpoint(x_vals: np.ndarray, func: np.ufunc):
    cumulative_sum = 0 #initializes the variable that will hold the sum of the areas of the rectangles
    for i in range(len(x_vals)-1): #loops through each interval
        cumulative_sum += func(x_vals[i]) * (x_vals[i + 1] - x_vals[i]) #calculates the area of each rectangle, using left endpoints, and adds it to cumulative sum
    return cumulative_sum

def trapezoid (x_vals: np.ndarray, func: np.ufunc):
    cumulative_sum = 0 #initializes the variable that will hold the sum of the areas of the rectangles
    for i in range(len(x_vals)-1): #loops through each interval
        cumulative_sum += (func(x_vals[i]) + func(x_vals[i + 1]))/2 * (x_vals[i + 1] - x_vals[i]) #calculates the area of each rectangle, using right endpoints, and adds it to cumulative sum
    return cumulative_sum

def simpson (x_vals: np.ndarray, func: np.ufunc):
    cumulative_sum = 0  #initializes the variable that will hold the sum of the areas of the trapezoids
    for i in range(len(x_vals)-1): #loops through each interval
        cumulative_sum += (1/6) * (func(x_vals[i]) + 4 * func((x_vals[i] + x_vals[i + 1])/2) + func(x_vals[i + 1])) * (x_vals[i + 1] - x_vals[i]) #calculates the area of each trapezoid and adds it to cumulative sum
    return cumulative_sum
