import pandas as pd

def reset_index_demo(data: dict, index_col: str) -> list:
    df=pd.DataFrame(data)
    new_df=df.set_index(index_col)
    new_df.index.name=index_col
    new_cols=new_df.reset_index()
    return [new_df.columns.to_list(),new_cols.columns.to_list()]
   
