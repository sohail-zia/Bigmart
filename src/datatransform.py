from .dataclean import Clean
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
clean = Clean()
df = clean.data_cleaner()
class Transform:
    def __init__(self):
        pass
    def transformer(self):
        x = df.drop('Item_Outlet_Sales', axis = 1)
        y = df['Item_Outlet_Sales']
        
        categorical = x.select_dtypes(include = 'object').columns
        numeric = x.select_dtypes(include = 'number').columns
        
        scaler = StandardScaler()
        scaler.fit(x[numeric])
        x[numeric]=scaler.transform(x[numeric])

        label_encoder = preprocessing.LabelEncoder()
        for col in categorical:
          x[col] = label_encoder.fit_transform(x[col])
        return x, y
