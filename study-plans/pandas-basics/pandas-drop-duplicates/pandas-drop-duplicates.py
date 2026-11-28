import pandas as pd

def drop_duplicates(data: dict) -> list:
    df=pd.DataFrame(data)
    drop_duplicated=df.drop_duplicates(keep="first")
    return [len(df),len(drop_duplicated),{str(i):drop_duplicated[i].to_list() for i in df.columns}]

