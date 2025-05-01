import joblib
import importlib.resources as resources

from .preprocessor import UserMessagesPreprocessor

RANDOM_FOREST: str = "RANDOM_FOREST"
LOGISTIC_REGRESSION: str = "LOGISTIC_REGRESSION"
LIGHTGBM: str = "LIGHTGBM"
XGBOOST: str = "XGBOOST"


def predict_user_pattern(user_messages: list[str], model: str = RANDOM_FOREST) -> int:
    p = UserMessagesPreprocessor(user_messages)
    df = p.get_df()

    model = _load_model(model)

    return model.predict(df)[0]



def _load_model(model: str):
    if model == RANDOM_FOREST:
        path = "chatcluster.models.random_forest"
        filename = "model.pkl"
    elif model == LOGISTIC_REGRESSION:
        path = "chatcluster.models.logistic_regression"
        filename = "model.pkl"
    elif model == LIGHTGBM:
        path = "chatcluster.models.gradient_boosting"
        filename = "model_lightgbm.pkl"
    elif model == XGBOOST:
        path = "chatcluster.models.gradient_boosting"
        filename = "model_xgboost.pkl"
    else:
        path = "chatcluster.models.random_forest"
        filename = "model.pkl"

    model_path = resources.files(path).joinpath(filename)
    return joblib.load(model_path)
