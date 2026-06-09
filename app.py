import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))
# --------------------------------------------------------

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn import run as app_run

from src.constants import APP_HOST, APP_PORT
from src.pipline.prediction_pipeline import VehicleData, VehicleDataClassifier
from src.pipline.training_pipeline import TrainPipeline

from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Vehicle Insurance Prediction App")

# Static files conditional setup (Vercel safe crash proof)
if os.path.exists(os.path.join(BASE_DIR, "static")):
    app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


def _to_int(form_data, key):
    return int(form_data.get(key))


def _to_float(form_data, key):
    return float(form_data.get(key))


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="vehicledata.html",
        context={"context": None}
    )

@app.post("/", response_class=HTMLResponse)
async def predict(request: Request):
    try:
        form = await request.form()
        vehicle_data = VehicleData(
            Gender=_to_int(form, "Gender"),
            Age=_to_int(form, "Age"),
            Driving_License=_to_int(form, "Driving_License"),
            Region_Code=_to_float(form, "Region_Code"),
            Previously_Insured=_to_int(form, "Previously_Insured"),
            Annual_Premium=_to_float(form, "Annual_Premium"),
            Policy_Sales_Channel=_to_float(form, "Policy_Sales_Channel"),
            Vintage=_to_int(form, "Vintage"),
            Vehicle_Age_lt_1_Year=_to_int(form, "Vehicle_Age_lt_1_Year"),
            Vehicle_Age_gt_2_Years=_to_int(form, "Vehicle_Age_gt_2_Years"),
            Vehicle_Damage_Yes=_to_int(form, "Vehicle_Damage_Yes"),
        )

        vehicle_df = vehicle_data.get_vehicle_input_data_frame()
        
        # Model loading and prediction logic when user submits form
        model = VehicleDataClassifier()
        prediction = int(model.predict(dataframe=vehicle_df)[0])
        
        status = (
            "Customer is likely to be interested in vehicle insurance."
            if prediction == 1
            else "Customer is unlikely to be interested in vehicle insurance."
        )
        return templates.TemplateResponse(
            request=request,
            name="vehicledata.html",
            context={"context": status}
        )
    except Exception as exc:
        return templates.TemplateResponse(
            request=request,
            name="vehicledata.html",
            context={"context": f"Error: {exc}"}
        )


@app.get("/train", response_class=PlainTextResponse)
def train_route():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return "Training completed successfully."
    except Exception as exc:
        return f"Training Error: {exc}"


if __name__ == "__main__":
    # Hugging Face environment uses port 7860 dynamically.
    # This checks for that variable; if missing, it defaults back to your local APP_HOST & APP_PORT
    port = int(os.getenv("PORT", APP_PORT))
    host = os.getenv("HOST", APP_HOST)
    
    app_run(app, host=host, port=port)