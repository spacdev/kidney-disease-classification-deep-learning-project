from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_evaluation_with_mlflow import EvaluationPipeline


STAGE_NAME = "Data Ingestion State"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e