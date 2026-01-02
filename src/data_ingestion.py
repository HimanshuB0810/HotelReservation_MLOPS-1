import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.custom_exception import CustomException
from src.logger import get_logger
from config.paths_config import *
from utils.common_functions import read_yaml
from minio import Minio

logger=get_logger(__name__)

class DataIngestion:
    def __init__(self,config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.bucket_file_name = self.config["bucket_file_name"]
        self.train_test_ratio = self.config['train_ratio']

        os.makedirs(RAW_DIR,exist_ok=True)

        logger.info(f"Data Ingestion Started with {self.bucket_name} and file is {self.bucket_file_name}")

    def download_csv_from_minio(self):
            try:
                client = Minio(
                    "localhost:9000",
                    access_key="minioadmin",
                    secret_key="minioadmin",
                    secure=False
                )

                client.fget_object(
                    self.bucket_name,        # same as GCP bucket
                    self.bucket_file_name,   # same as blob name
                    RAW_FILE_PATH            # same as local path
                )

                logger.info(
                    f"Raw file successfully downloaded from MinIO to {RAW_FILE_PATH}"
                )

            except Exception as e:
                logger.error("Error while downloading CSV file from MinIO")
                raise CustomException("Failed to download csv file from MinIO", e)
            
    def split_data(self):
        try:
              logger.info("Starting the splitting process")
              data = pd.read_csv(RAW_FILE_PATH)
              train_data, test_data = train_test_split(data, test_size=1-self.train_test_ratio,random_state=42)

              train_data.to_csv(TRAIN_FILE_PATH)
              test_data.to_csv(TEST_FILE_PATH)

              logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
              logger.info(f"Test data saved to {TEST_FILE_PATH}")

        except Exception as e:
                logger.error("Error while splitting data")
                raise CustomException("Failed to split data into training and testing sets", e)
        
    def run(self):
        try:
             logger.info("Starting the data ingestion process")

             self.download_csv_from_minio()
             self.split_data()

             logger.info("Data Ingestion Completed Successfully")
        except CustomException as ce:
             logger.error(f"CustomException : {str(ce)}")

        finally:
            logger.info("Data Ingestion Completed")

if __name__=="__main__":
    
    data_ingestion=DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()