import pandas as pd
import numpy as np

def clean_missing_values(data_df: pd.DataFrame)->pd.DataFrame:
    """
    Returns input DataFrame with columns having more than 20%
    of its values being missing values dropped
    """
    threshold = 0.8
    data_df = data_df.dropna(axis=1, thresh=int((1-threshold)*data_df.shape[0]))
    
    return data_df
