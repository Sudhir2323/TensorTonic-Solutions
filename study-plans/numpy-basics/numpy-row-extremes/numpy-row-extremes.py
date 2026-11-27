import numpy as np

def row_extremes(data: list) -> np.ndarray:
    """
    Returns float64 rows of maxima, maximum indices, minima, and minimum indices.
    """
    data=np.array(data,dtype=np.float64)
    return np.stack([data.max(axis=1),data.argmax(axis=1),data.min(axis=1),data.argmin(axis=1)])
