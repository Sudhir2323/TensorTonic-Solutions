import numpy as np

def angle_features(angles: list) -> np.ndarray:
    """
    Returns a (3, n) float64 array with sine, cosine, and tangent rows.
    """
    a=np.array(angles)
    return np.stack([np.sin(a),np.cos(a),np.tan(a)])
    
