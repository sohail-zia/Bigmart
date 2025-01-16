import joblib as j

from pipeline.model import Models
from src.datasplit import Split

split = Split()
models = Models()

x_train, x_test, y_train, y_test = split.spliter()
grid = models.rf_model()

print('Starting Training')

grid.fit(x_train, y_train)

print('Model Train')

model = grid.best_estimator_

j.dump(model, 'models/model.pkl')

print('Model Save')