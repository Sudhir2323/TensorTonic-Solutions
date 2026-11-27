import numpy as np

def norm_gate(X: list, Y: list, threshold: float) -> np.ndarray:
    """
    Returns an (n, k) float64 matrix of norm-gated transformed rows.
    """
    _dtype=np.float64
    X,Y=np.array(X,dtype=_dtype),np.array(Y,dtype=_dtype)
    norms=np.linalg.norm(X@Y,axis=1)
    gate=norms>=threshold
    Z=(X@Y)*gate[:,np.newaxis]
    return Z
    
    
