from src.TextSum.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.TextSum.logging import logger

STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started succesfully!! <<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed!! <<<<")
except Exception as e:
    raise e