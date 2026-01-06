import os
from box.exceptions import BoxValueError
import yaml
from src.cnnClassifier import logger
import json
import joblib # type: ignore 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, List, Dict
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    
    Args:
        path_to_yaml(str): path like input
        
    Raises:
        ValueError: if yaml file is empty
        
    Returns
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
#@ensure_annotations
def create_directories(path_to_directories: List[str], verbose:bool=True):
    """create list of directories
    
    Args:
        path to directories (list): list of path of directories
        ignore_log(bool, optional): Ignore if multiple dirs is to be created 
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: Dict[Any, Any]):
    """save json data
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data
    
    Args:
        path (Path): path to json file
    """

    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from path: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
    
    Args:
        data(Any): data to be saved as binary
        path(Path): path to binary file
    """
    joblib.dump(value=data, filename=path) # type: ignore
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) ->Any:
    """load binary data
    
    Args:
        path (Path): path to binary file
        
    Returns:
    """
    data = joblib.load(path) # type: ignore
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) ->str:
    """get size in KB
    
    Args:
        path(Path): path of the file
    
    Returns:
        size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"

def decodeImage(imgstring:Any, filename:str):
    imgdata = base64.b64decode(imgstring)
    with open(filename, "wb") as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(cropped_image_path:str):
    with open(cropped_image_path, "rb") as f:
        return base64.urlsafe_b64encode(f.read())

    