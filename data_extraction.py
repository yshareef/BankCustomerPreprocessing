import glob  # this module helps in selecting files
import os

import pandas as pd  # this module helps in processing CSV files
import xml.etree.ElementTree as ET  # this module helps in processing XML files.
from datetime import datetime
from constants import Constants


class DataExtraction:
    @staticmethod
    def extract_from_csv(file_to_process):
        dataframe = pd.read_csv(file_to_process)
        return dataframe

    @staticmethod
    def extract_from_json(file_to_process):
        dataframe = pd.read_json(file_to_process, lines=True)
        return dataframe

    def extract(self):
        DATA_DIR = Constants.DATA_DIR
        extracted_data = pd.DataFrame(
            columns=['ID', 'BALANCE', 'BALANCE_FREQUENCY', 'PURCHASES', 'ONEOFF_PURCHASES',
                     'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'PURCHASES_FREQUENCY',
                     'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY',
                     'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX',
                     'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS',
                     'PRC_FULL_PAYMENT', 'TENURE'])

        # process all csv files
        for csvfile in glob.glob(DATA_DIR + "/*.csv"):
            extracted_data = pd.concat([extracted_data, (self.extract_from_csv(csvfile))], ignore_index=True)
            print(csvfile)

        # process all json files
        for jsonfile in glob.glob(DATA_DIR + "/*.json"):
            extracted_data = pd.concat([extracted_data, (self.extract_from_csv(jsonfile))], ignore_index=True)

        return extracted_data


data_extraction_service = DataExtraction()

# df = extract()
# dataset_path = os.path.join(CACHE_DIR, 'Customer_data.csv')
# df.to_csv(dataset_path, index=False)
