import pandas as pd
from .dataloading import Loader

PATH = r'C:\Users\RC\Desktop\Bigmart\artifacts\Train.csv'
loader = Loader()
data = loader.data_loader(PATH)
class Clean:
    def __init__(self):
         pass
    def data_cleaner(self, data=data):
        data = data.apply(lambda col: col.fillna(col.mean()) if col.dtype in ['float64', 'int64'] else col)
        data = data.apply(lambda col: col.fillna(col.mode()[0]) if col.dtype == 'object' else col) 
        data['Item_Fat_Content'] = data['Item_Fat_Content'].replace({'reg':'Regular', 'LF':'Low Fat', 'low fat':'Low Fat'})
        data.drop('Item_Identifier', axis=1, inplace= True)
        data.drop('Outlet_Identifier', axis=1,inplace= True)
        data.to_csv(r'./artifacts/clean_data.csv')
        return data