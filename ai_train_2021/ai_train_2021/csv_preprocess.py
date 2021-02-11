import os
import shutil
from typing import List
from typing import Callable

import pandas as pd


class CSVPreprocessor:
    _DATA_ROOT_PATH = "data_set"
    _SUF_COLUMN = "_cols"
    _SUF_PREPROCESSED = "_processed"

    def __init__(self, csv_path):
        self.base_name = os.path.basename(csv_path).split(".")[0]
        self.data_set_dir = self._make_path([self.base_name])
        if not os.path.exists(self.data_set_dir):
            print("Making save directory")
            os.makedirs(self.data_set_dir)

        self.csv_path = self._make_path([self.base_name, os.path.basename(csv_path)])
        if not os.path.exists(self.csv_path):
            print("Copying csv to " + self.csv_path)
            shutil.copy(csv_path, self.data_set_dir)

        self.df = pd.read_csv(self.csv_path)

    @classmethod
    def _make_path(cls, dirs: List[str], contain_root_path: bool = True):
        if contain_root_path:
            dirs = [CSVPreprocessor._DATA_ROOT_PATH] + dirs
        return os.sep.join(dirs)

if __name__ == "__main__":
    sample_path = "data_set/sample/sample.csv"

    csvp = CSVPreprocessor(sample_path)