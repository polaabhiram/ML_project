from dataclasses import dataclass
import os
import pandas as pd
from src.logger import logging
from sklearn.model_selection import train_test_split
import sys
from src.exception import CustomException
from src.components.data_transformation import DataTransformation,DataTransformationconfig 
from src.components.model_trainer import Model_trainer_config,ModelTrainer


@dataclass
class DataIngestionConfig:
        artifact_dir: str = "artifacts"
        train_data_path: str = os.path.join("artifacts", "train.csv")
        test_data_path: str = os.path.join("artifacts", "test.csv")
        raw_data_path: str = os.path.join("artifacts", "raw.csv")

class DataIngestion:
    def __init__ (self):
        self.config=DataIngestionConfig()

    def initiate_ingestion(self):

        try:
             
            df = pd.read_csv(os.path.join("datasource", "stud.csv"))

            

            os.makedirs(self.config.artifact_dir,exist_ok=True)
            logging.info("Storing raw data")

            df.to_csv(self.config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.config.train_data_path,index=False,header=True)

            test_set.to_csv(self.config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(self.config.train_data_path,self.config.test_data_path)

        except Exception as e:
             raise CustomException(e,sys)




if __name__ == "__main__":
    obj= DataIngestion()
    a,b=obj.initiate_ingestion()
    dt=DataTransformation()
    x,y,z=dt.initiate_transformation(a,b)
    mod=ModelTrainer()
    mod.initiate_train(x,y)