import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    if operation=='flatten':
        return np.array(data,dtype=np.float64).flatten()
    elif operation=='transpose':
        t=np.array(data,dtype=np.float64).T
        return t
    else:
        return np.array([data],dtype=np.float64)