#function for reading a yaml file 
import os
import pandas as pd # type: ignore
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml # type: ignore


logger=get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("File is not in the given path")
        with open(file_path,"r") as yaml_file:
            config=yaml.safe_load(yaml_file)
            logger.info("Successfully read the yaml file ")
            return config 
    except Exception as e:
        logger.error("Error while reading YAML file ")
        raise CustomException("Failed to read the YAML FILE ",e)
    
def load_data(path):
    try:
        logger.info("Loading Data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error("Error loading the data {e}")
        raise CustomException("Failded to load the data",e)
    
    
