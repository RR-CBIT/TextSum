from src.TextSum.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.TextSum.pipeline.stage_02_data_validation import DataValidationPipeline
from src.TextSum.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.TextSum.logging import logger

STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started succesfully!! <<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed!! <<<<")
except Exception as e:
    raise e

STAGE_NAME= "Data Validation Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started succesfully!! <<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed!! <<<<")
except Exception as e:
    raise e

STAGE_NAME= "Data Transformation Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started succesfully!! <<<<")
    data_validation = DataTransformationPipeline()
    data_validation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed!! <<<<")
except Exception as e:
    raise e