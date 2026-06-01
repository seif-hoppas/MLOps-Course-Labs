"""
Churn Prediction API

Run with:
    litestar --app main:app run --reload
Then open:
    http://localhost:8000/schema/swagger
"""

from litestar import Litestar, get, post
from pydantic import BaseModel

from app.model_utils import predict_churn
from app.logger_setup import setup_logging

logger = setup_logging()


# ---------------------------------------------------------------------------
# Request Schema
# ---------------------------------------------------------------------------
class ChurnRequest(BaseModel):
    CreditScore: float
    Geography: str
    Gender: str
    Age: float
    Tenure: float
    Balance: float
    NumOfProducts: float
    HasCrCard: float
    IsActiveMember: float
    EstimatedSalary: float


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

# TODO 2: Create a GET endpoint at "/" that returns a welcome message
#         Log that the home endpoint was accessed


@get("/")
def home() -> dict:
    logger.info("Home endpoint accessed")
    return {"message": "Welcome to the Churn Prediction API!"}


# TODO 3: Create a GET endpoint at "/health" that returns {"status": "healthy"}
@get("/health")
def health() -> dict:
    logger.info("Health endpoint accessed")
    return {"status": "healthy"}


# TODO 4: Create a POST endpoint at "/predict" that:
#         - Accepts a ChurnRequest as the data parameter
#         - Extracts features into a list
#         - Calls predict_churn(features)
#         - Returns the prediction
#         - Logs the input features and the prediction result


@post("/predict")
def predict(data: ChurnRequest) -> dict:
    features = [
        data.CreditScore,
        data.Geography,
        data.Gender,
        data.Age,
        data.Tenure,
        data.Balance,
        data.NumOfProducts,
        data.HasCrCard,
        data.IsActiveMember,
        data.EstimatedSalary,
    ]

    prediction = predict_churn(features)
    logger.info(f"Input features: {features}")
    logger.info(f"Prediction: {prediction}")

    return {"prediction": prediction}


# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------
# TODO 5: Register your endpoint functions in the list below
app = Litestar(
    route_handlers=[home, health, predict],
)
