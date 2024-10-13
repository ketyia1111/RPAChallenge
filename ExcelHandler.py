import pandas as pd
from Constants import *

class ExcelHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_excel(self):
        df = pd.read_excel(self.file_path)
        data_dict = df.to_dict(orient=RECORD)
        return data_dict