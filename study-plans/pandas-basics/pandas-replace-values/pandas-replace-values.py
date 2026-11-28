import pandas as pd

def replace_values(data: dict, column: str, old_val: object, new_val: object) -> dict:
    df=pd.DataFrame(data)
    df2=df.copy()
    df[column].replace(old_val,new_val,inplace=True)
    return {"data":{str(i):df[i].to_list() for i in df.columns},"count":(df!=df2)[column].sum()}
