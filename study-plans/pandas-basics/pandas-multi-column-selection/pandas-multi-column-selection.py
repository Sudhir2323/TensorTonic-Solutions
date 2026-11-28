import pandas as pd

def select_columns(data: dict, columns: list) -> dict:
    """
    Returns a dictionary of value lists in the requested column order.
    """
    df=pd.DataFrame(data)
    return {str(i):df[i].to_list() for i in df[columns]}
    pass
