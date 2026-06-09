import os
import shutil
import sys

from src.exception import MyException
from src.logger import logging
from src.entity.artifact_entity import ModelPusherArtifact, ModelEvaluationArtifact
from src.entity.config_entity import ModelPusherConfig


class ModelPusher:
    def __init__(self, model_evaluation_artifact: ModelEvaluationArtifact,
                 model_pusher_config: ModelPusherConfig):
        """
        :param model_evaluation_artifact: Output reference of data evaluation artifact stage
        :param model_pusher_config: Configuration for model pusher
        """
        try:
            self.model_evaluation_artifact = model_evaluation_artifact
            self.model_pusher_config = model_pusher_config
        except Exception as e:
            raise MyException(e, sys)

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        """
        Method Name :   initiate_model_pusher
        Description :   This function is used to copy the trained model to a local production directory
        
        Output      :   Returns model pusher artifact
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info("Entered initiate_model_pusher method of ModelPusher class")
        print("------------------------------------------------------------------------------------------------")
        
        try:
            # 1. Source path of the newly trained model from your training artifacts
            trained_model_path = self.model_evaluation_artifact.trained_model_path
            
            # 2. Target path where your local web application reads the model from
            local_saved_model_dir = "saved_models"
            os.makedirs(local_saved_model_dir, exist_ok=True)
            local_saved_model_path = os.path.join(local_saved_model_dir, "model.pkl")
            
            logging.info(f"Copying trained model from {trained_model_path} to local storage: {local_saved_model_path}")
            
            # 3. Copy the file directly on your hard drive
            shutil.copy(trained_model_path, local_saved_model_path)
            logging.info("Model saved locally to the saved_models directory successfully.")

            # 4. Create artifact tracking paths using the local layout
            model_pusher_artifact = ModelPusherArtifact(
                bucket_name="local_storage",
                s3_model_path=local_saved_model_path
            )

            logging.info(f"Model pusher artifact created: [{model_pusher_artifact}]")
            logging.info("Exited initiate_model_pusher method of ModelPusher class")
                
            return model_pusher_artifact

        except Exception as e:
            raise MyException(e, sys)