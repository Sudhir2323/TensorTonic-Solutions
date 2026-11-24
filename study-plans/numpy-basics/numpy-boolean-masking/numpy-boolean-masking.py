import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:
    arr=np.array(data,dtype=np.float64)
    mask_row=np.any(arr>threshold,axis=1)
    mask_row2=np.all(arr>threshold,axis=1)
    row_any,row_all=arr.copy(),arr.copy()
    row_any[~mask_row]=0.0
    row_all[~mask_row2]=0.0
    return np.array([np.select([arr>threshold],[1.0],default=0.0),row_any,row_all])    
