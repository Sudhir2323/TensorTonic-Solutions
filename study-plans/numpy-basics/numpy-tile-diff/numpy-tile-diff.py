import numpy as np

def tile_diff(data: list, reps: int) -> np.ndarray:
    data=np.array(data,dtype=np.float64)
    tiled=np.tile(data,(reps,1))
    diff=np.diff(tiled,axis=0)
    return np.stack([tiled,np.pad(diff,((0,1),(0,0)))])
    
