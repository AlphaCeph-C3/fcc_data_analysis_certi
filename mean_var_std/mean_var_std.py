import numpy as np


def calculate(array):
    if len(array) != 9:
        raise ValueError("List must contain nine numbers.")
    # convert the list into numpy array and reshape it.
    formatted_array = np.array(array).reshape((3, 3))

    # function to calculate the statistic for a n-dimensional numpy-array along the axes
    # and the statistic of the whole array
    def calculate_stat(arr, func):
        result = []
        # ndim attribute gets the dimension of the array
        for i in range(arr.ndim):
            result.append(list(func(arr, axis=i)))
        # calculation for the whole array
        result.append(func(arr))
        return result

    # necessary statistic function to do the calculation
    stat_functions = {
        "mean": np.mean,
        "variance": np.var,
        "standard deviation": np.std,
        "max": np.max,
        "min": np.min,
        "sum": np.sum,
    }
    calculations = {}
    for key, value in stat_functions.items():
        calculations[key] = calculate_stat(formatted_array, value)
    return calculations


print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
