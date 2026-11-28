import pandas as pd

def boolean_filter(data: dict, column: str, threshold: float) -> dict:
    """
    Returns filtered_data as a dictionary of lists and count as an integer.
    """
    df=pd.DataFrame(data)
    filtered_rows=df[df[column]>threshold]
    result={"filtered_data":{str(i):filtered_rows[i].to_list() for i in filtered_rows.columns},"count":len(filtered_rows)}
    return result
