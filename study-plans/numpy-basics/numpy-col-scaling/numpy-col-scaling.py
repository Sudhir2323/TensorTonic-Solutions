import numpy as np

def scale_cols(data: list, weights: list) -> np.ndarray:
    """
    Returns a float64 matrix with each column multiplied by its weight.
    """
    arr,weights=np.array(data,dtype=np.float64).T,np.array(weights,dtype=np.float64)

    return np.transpose(arr*weights[:,np.newaxis])
