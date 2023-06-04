import os

import pandas as pd

from constants import Constants


class DataCleaning:
    def __init__(self):
        pass
        # CACHE_DIR = Constants.CACHE_DIR
        # dataset_path = os.path.join(CACHE_DIR, 'Customer_data.csv')
        # self.df = df_to_clean

    def clean_data(self,df):
        # drop the missing values
        df.dropna(inplace=True)

        # drop ID column
        cleaned_df = df.drop(columns=["ID"], axis=1)
        return cleaned_df


data_cleaning_service = DataCleaning()

# cleaned_dataset_path = os.path.join(self.CACHE_DIR, 'cleaned_Customer_data.csv')
# cleaned_dataset_path.to_csv(cleaned_dataset_path, index=False)
