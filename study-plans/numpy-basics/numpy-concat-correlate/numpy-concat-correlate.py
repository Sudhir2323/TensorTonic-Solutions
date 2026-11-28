import numpy as np

def compare_correlations(a: list, b: list) -> np.ndarray:
    """
    Returns float64 correlation matrices for a, b, and their combined rows.
    """
    a=np.array(a,dtype=np.float64)
    b=np.array(b,dtype=np.float64)
    corr_a,corr_b=np.corrcoef(a,rowvar=False),np.corrcoef(b,rowvar=False)
    combined=np.vstack([a,b])
    combined_corr=np.corrcoef(combined,rowvar=False)
    return np.stack([corr_a,corr_b,combined_corr])
