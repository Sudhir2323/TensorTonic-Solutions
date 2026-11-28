import pandas as pd

def handle_missing(data: dict, fill_value: float) -> dict:
    df=pd.DataFrame(data)
    return {"null_counts":{str(i):df[i].isnull().sum() for i in df.columns},"cleaned_data":{str(i):df[i].fillna(fill_value).to_list() for i in df.columns}}
