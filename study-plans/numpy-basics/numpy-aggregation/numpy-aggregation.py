import numpy as np

def summarize(data: list, axis: int) -> np.ndarray:
    """
    Returns float64 rows of mean, standard deviation, minimum, and maximum.
    """
    data=np.array(data,dtype=np.float64)
    if axis==0:
        return np.stack([data.mean(axis=0),data.std(axis=0),data.min(axis=0),data.max(axis=0)])
    else:
        return np.stack([data.mean(axis=1),data.std(axis=1),data.min(axis=1),data.max(axis=1)])
        
