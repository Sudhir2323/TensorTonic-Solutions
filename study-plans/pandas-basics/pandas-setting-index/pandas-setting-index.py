import pandas as pd

def set_index_column(data: dict, index_col: str) -> dict:
    
    df=pd.DataFrame(data)
    df=df.set_index(index_col)
    return {"index_values":df.index.to_list(),"columns":df.columns.to_list(),"data":{str(i):df[i].to_list() for i in df.columns}}
