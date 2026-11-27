import numpy as np

def winsorize(data: list, lo_q: float, hi_q: float) -> np.ndarray:
    
    data = np.array(data,dtype=np.float64)
    x=np.stack([np.percentile(data,lo_q,axis=0),np.percentile(data,hi_q,axis=0)])
    result=np.clip(data,*x)
    low_mask=np.where(data!=np.clip(data,x[0],None),1,0)
    high_mask=np.where(data!=np.clip(data,None,x[1]),1,0)
    return np.stack([result,low_mask,high_mask])
    
