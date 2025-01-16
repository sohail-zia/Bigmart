import pandas as pd

class Loader:
    def __init__(self):
        pass
    def data_loader(self, path):
        data = pd.read_csv(path)
        return data