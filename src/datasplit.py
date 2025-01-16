from .datatransform import Transform
from sklearn.model_selection import train_test_split
t = Transform()
x, y = t.transformer()
class Split:
    def __init__(self):
       pass
    def spliter(self, x=x, y=y):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
        return x_train, x_test, y_train, y_test
        