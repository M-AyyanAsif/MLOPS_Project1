import sys
import os
import pickle
from pandas import DataFrame
from src.exception import MyException
from src.logger import logging

# Project Root directory find karne ke liye dynamic path setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VehicleData:
    def __init__(self,
                 Gender,
                 Age,
                 Driving_License,
                 Region_Code,
                 Previously_Insured,
                 Annual_Premium,
                 Policy_Sales_Channel,
                 Vintage,
                 Vehicle_Age_lt_1_Year,
                 Vehicle_Age_gt_2_Years,
                 Vehicle_Damage_Yes
                 ):
        """
        Vehicle Data constructor
        """
        try:
            def cast_to_int(value):
                try:
                    return int(float(value))
                except (ValueError, TypeError):
                    return value

            def cast_to_float(value):
                try:
                    return float(value)
                except (ValueError, TypeError):
                    return value

            self.Gender = cast_to_int(Gender)
            self.Age = cast_to_int(Age)
            self.Driving_License = cast_to_int(Driving_License)
            self.Region_Code = cast_to_int(Region_Code)
            self.Previously_Insured = cast_to_int(Previously_Insured)
            self.Annual_Premium = cast_to_float(Annual_Premium)
            self.Policy_Sales_Channel = cast_to_int(Policy_Sales_Channel)
            self.Vintage = cast_to_int(Vintage)
            self.Vehicle_Age_lt_1_Year = cast_to_int(Vehicle_Age_lt_1_Year)
            self.Vehicle_Age_gt_2_Years = cast_to_int(Vehicle_Age_gt_2_Years)
            self.Vehicle_Damage_Yes = cast_to_int(Vehicle_Damage_Yes)

            if self.Vehicle_Age_lt_1_Year == 1 and self.Vehicle_Age_gt_2_Years == 1:
                self.Vehicle_Age_lt_1_Year = 0 

        except Exception as e:
            raise MyException(e, sys) from e

    def get_vehicle_input_data_frame(self) -> DataFrame:
        try:
            vehicle_input_dict = self.get_vehicle_data_as_dict()
            return DataFrame(vehicle_input_dict)
        except Exception as e:
            raise MyException(e, sys) from e

    def get_vehicle_data_as_dict(self):
        try:
            input_data = {
                "Gender": [self.Gender],
                "Age": [self.Age],
                "Driving_License": [self.Driving_License],
                "Region_Code": [self.Region_Code],
                "Previously_Insured": [self.Previously_Insured],
                "Annual_Premium": [self.Annual_Premium],
                "Policy_Sales_Channel": [self.Policy_Sales_Channel],
                "Vintage": [self.Vintage],
                "Vehicle_Age_lt_1_Year": [self.Vehicle_Age_lt_1_Year],
                "Vehicle_Age_gt_2_Years": [self.Vehicle_Age_gt_2_Years],
                "Vehicle_Damage_Yes": [self.Vehicle_Damage_Yes]
            }
            return input_data
        except Exception as e:
            raise MyException(e, sys) from e


class VehicleDataClassifier:
    def __init__(self) -> None:
        pass

    def predict(self, dataframe) -> str:
        try:
            logging.info("Entered predict method of VehicleDataClassifier class")
            
            # Dynamically model path build karna jo har operating system par chalay
            local_model_path = os.path.join(BASE_DIR, "saved_models", "model.pkl")
            
            if not os.path.exists(local_model_path):
                raise FileNotFoundError(f"Local model file not found at '{local_model_path}'.")
            
            with open(local_model_path, "rb") as model_file:
                local_model = pickle.load(model_file)
            
            # Ensure columns are sorted correctly before any processing
            if hasattr(local_model, 'feature_names_in_'):
                expected_cols = list(local_model.feature_names_in_)
                dataframe = dataframe[expected_cols]

            # -----------------------------------------------------------------
            # 🛠️ DYNAMIC PREPROCESSOR SEARCH & APPLICATION
            # -----------------------------------------------------------------
            preprocessor_applied = False
            possible_preprocessor_paths = [
                os.path.join(BASE_DIR, "saved_models", "preprocessor.pkl"),
                os.path.join(BASE_DIR, "concept_artifacts", "preprocessor.pkl")
            ]
            
            for path in possible_preprocessor_paths:
                if os.path.exists(path):
                    try:
                        with open(path, "rb") as f:
                            preprocessor = pickle.load(f)
                        dataframe = preprocessor.transform(dataframe)
                        print(f"📦 Successfully loaded and applied preprocessor scaling from: {path}")
                        preprocessor_applied = True
                        break
                    except Exception as e:
                        print(f"⚠️ Found preprocessor at {path} but failed to transform: {e}")

            if not preprocessor_applied:
                print("⚠️ No valid preprocessor.pkl found. Sending raw numerical features directly to the model.")
            # -----------------------------------------------------------------

            # Run the prediction
            result = local_model.predict(dataframe)
            
            print("\n" + "="*60)
            print("📊 RAW MODEL PREDICTION VALUE RESULT:")
            print(f"The model directly outputted: {result}")
            print("="*60 + "\n")
            
            return result
        
        except Exception as e:
            raise MyException(e, sys)