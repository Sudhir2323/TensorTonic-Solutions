import numpy as np

def normalize(data: list) -> np.ndarray:
    """
    Returns a float64 matrix standardized independently by column.
    """
    a=np.array(data,dtype=np.float64)
    return ((a.T-a.mean(axis=0)[:,np.newaxis])/a.std(axis=0)[:,np.newaxis]).T
