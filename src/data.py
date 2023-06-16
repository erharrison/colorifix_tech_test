import pandas as pd


class Data:
    def __init__(self,
                 column_names,
                 data
                 ):
        self.column_names = column_names
        self.data = data

    def create_data(self):
        df = pd.DataFrame(self.data, self.column_names)
        return df
