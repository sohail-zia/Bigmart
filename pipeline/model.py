from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

class Models:
    def __init__(self):
        pass
    def rf_model(self):
        rf = RandomForestRegressor(random_state=42)
        param_grid = {
       'n_estimators': [50, 100],
       'max_depth': [None, 10],
       'min_samples_split': [10],
       'min_samples_leaf': [2]}
    
        grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        scoring='neg_mean_squared_error',
        cv=4,
        n_jobs=-1
        ) 
        return grid_search    