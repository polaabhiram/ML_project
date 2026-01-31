from dataclasses import dataclass
import pandas as pd
import os
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import sys
from src.exception import CustomException
from src.utils import save_object


@dataclass
class DataTransformationconfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.config=DataTransformationconfig()

    def get_preprocessor(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                    "gender",
                    "race_ethnicity",
                    "parental_level_of_education",
                    "lunch",
                    "test_preparation_course",
                ]
            
            num_pipeline=Pipeline(
                [('imputer',SimpleImputer(strategy="median")),("scaler", StandardScaler())]
            )

            cat_pipeline=Pipeline(
                [("imputer",SimpleImputer(strategy="most_frequent")),("ohe",OneHotEncoder())]
            )

            transformer= ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)    
                ]
            )
            return transformer
        
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_transformation(self,train_data_path,test_data_path):
        try:
            train=pd.read_csv(train_data_path)
            test=pd.read_csv(test_data_path)

            preprocessor= self.get_preprocessor()

            train_data_input=train.drop(columns=["math_score"])
            train_data_output=train.math_score

            test_data_input=test.drop(columns=["math_score"])
            test_data_output=test.math_score
            
            train_fit_transformed=preprocessor.fit_transform(train_data_input)
            test_transformed=preprocessor.transform(test_data_input)

            final_train=np.c_[train_fit_transformed,np.array(train_data_output)]
            final_test=np.c_[test_transformed,np.array(test_data_output)]

            save_object(os.path.join("artifacts/models","preprocessor.pkl"),preprocessor)

            return final_train, final_test, self.config.preprocessor_obj_file_path


            

        except Exception as e:
            raise CustomException(e,sys)

