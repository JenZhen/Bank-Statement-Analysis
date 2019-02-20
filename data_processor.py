import numpy as np
import re
from enum import Enum
import pandas as pd

ORIGINAL_DATA_DIR = "./original_transactions/"
CLEAN_DATA_DIR = "./clean_transactions/"

BOA_COLS = ["Posted Date", "Payee", "Amount"]
CHASE_COLS = ["Transaction Date", "Description", "Amount"]
CITI_COLS = ["Date", "Description", "Amount"]
GENERIC_COLS = ["Date", "Description", "Amount"]

# to convert raw data (downloaded from various bank site) to clean data
# definition of clean data: transaction_date, description, amount
# raw data will be used as 1)training data for labeling 2) for testing
class Bank(Enum):
    AMEX = 1
    BOA = 2
    CHASE = 3
    CITI = 4
    DISCOVER = 5

class DataProcessor:
    # input file: /path/to/files/AMEX_3008.csv
    # eg. ./original_transactions/AMEX_
    def __init__(self, input_file):
        self.raw_transaction_file = input_file
        self.bank, self.input_file_name = self._get_bank_name(input_file)
        self.output_file = None

    def generate_clean_data(self):
        output_file_name = self._get_output_file_name(self.input_file_name)
        self.output_file = CLEAN_DATA_DIR + output_file_name
        if self.bank == Bank.AMEX.name:
            self._parse_AMEX()
        elif self.bank == Bank.BOA.name:
            self._parse_BOA()
        elif self.bank == Bank.CHASE.name:
            self._parse_CHASE()
        elif self.bank == Bank.CITI.name:
            self._parse_CITI()
            pass
        elif self.bank == Bank.DISCOVER.name:
            # TODO
            pass
        else:
            print("Unsupported Bank type -- " + self.bank_name)

    def _parse_AMEX(self):
        df = pd.read_csv(self.raw_transaction_file)
        # In Amex raw data, 1st, 3rd, 4th col are
        # date, amount, description
        df = df.iloc[:, [0, 3, 2]]
        df.columns = GENERIC_COLS
        df.to_csv(self.output_file, index=False)

    def _parse_BOA(self):
        df = pd.read_csv(self.raw_transaction_file)
        df = df[BOA_COLS]
        df.columns = GENERIC_COLS
        df.to_csv(self.output_file, index=False)

    def _parse_CHASE(self):
        df = pd.read_csv(self.raw_transaction_file)
        df = df[CHASE_COLS]
        df.columns = GENERIC_COLS
        df.to_csv(self.output_file, index=False)

    def _parse_CITI(self):
        """
        In Citi csv file, Debit is positive value, Credit is negative value,
        They are of 2 different columns. Need to create a new col "Amount" that
        reverse the original sign.
        """
        df = pd.read_csv(self.raw_transaction_file)
        # print(df)
        df["Amount"] = df.apply(lambda row: row.Debit * (-1) if not pd.isnull(row.Debit) else row.Credit * (-1), axis=1)
        df = df[CITI_COLS]
        df.columns = GENERIC_COLS
        df.to_csv(self.output_file, index=False)

    def _get_bank_name(self, input_file):
        # if passed in has dir, parse file name first,
        # else the whole str is file name
        file_name = None
        if "/" in input_file:
            last_slash_idx = input_file.rfind("/")
            file_name = input_file[last_slash_idx + 1 : ]
            # print("input_file name:" + file_name)
        else:
            file_name = input_file
        first_udscore_idx = file_name.find("_")
        bank_name = file_name[: first_udscore_idx]
        # print("bank name: " + bank_name)
        return bank_name, file_name

    def _get_output_file_name(self, input_file_name):
        idx = input_file_name.find(".")
        return input_file_name[ : idx] + "_clean.csv"

if __name__ == '__main__':
    files = [
        "AMEX_3008.csv",
        "BOA_9291_201809.csv",
        "BOA_9291_201810.csv",
        "CHASE_1516.csv",
        "CHASE_9814.csv",
        "CITI_4321_201901.csv"
    ]
    for file in files:
        file_dir = ORIGINAL_DATA_DIR + file
        dp = DataProcessor(file_dir)
        dp.generate_clean_data()
