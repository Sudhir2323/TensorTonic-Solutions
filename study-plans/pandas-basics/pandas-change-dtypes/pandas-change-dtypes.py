import pandas as pd

def change_dtype(data: dict, column: str, target_type: str) -> list:
    df=pd.DataFrame(data)
    df2=df.copy()
    df2[column]=df2[column].astype(target_type)
    return [{str(i):str(df[i].dtype) for i in df.columns},{str(i):str(df2[i].dtype) for i in df2.columns}]
    
    