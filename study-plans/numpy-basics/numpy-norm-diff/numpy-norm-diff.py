import numpy as np

def norm_diff(a: list, b: list, lo: float, hi: float) -> np.ndarray:
    """
    Returns a float64 array of absolute normalized differences.
    """
    a,b=np.array(a,dtype=np.float64),np.array(b,dtype=np.float64)
    return abs(np.clip(a,lo,hi)-np.clip(b,lo,hi))/(hi-lo)
