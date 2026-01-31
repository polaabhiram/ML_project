from src.logger import logging
from src.exception import CustomException
import sys


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor,AdaBoostRegressor

import os

from src.utils import save_object,evaluate_models

from dataclasses import dataclass

@dataclass
class Model_trainer_config:
    trained_model_path: str = os.path.join("artifacts", "models", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.config=Model_trainer_config()
        os.makedirs(os.path.dirname(self.config.trained_model_path), exist_ok=True)


    def initiate_train(self,train_arr,test_arr):
        logging.info("Initiating model training")
        try:
            X_train,Y_train,X_test,Y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            models={
                "Linear Regression":LinearRegression(),
                "Decision Tree Reg":DecisionTreeRegressor(),
                "AdaBoost":AdaBoostRegressor(),
                "XGBOOst":XGBRegressor(),
                "Gradient Boost":GradientBoostingRegressor(),
                "Random Forest":RandomForestRegressor()
            }

            model_report=evaluate_models(X_train,Y_train,X_test,Y_test,models)

            best = max(model_report.values())


            best_model_name=list(model_report.keys())[
    list(model_report.values()).index(best)
]

            best_model=models[best_model_name]

            save_object(os.path.join(self.config.trained_model_path),best_model)
            
            
            if best<0.7:
                raise CustomException("Model performance too low")
        
        
        
        
        except Exception as e:
            raise CustomException(e,sys)
        
