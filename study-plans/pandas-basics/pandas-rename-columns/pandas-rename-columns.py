import pandas as pd

def rename_columns(data: dict, rename_map: dict) -> dict:
    df=pd.DataFrame(data)
    df.rename(columns=rename_map,inplace=True)
    return {str(i):df[i].to_list() for i in df.columns}
