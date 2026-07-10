import json
from pathlib import Path
import joblib

# __file__ = current file ka path
# resolve() = absolute path
# .parent = one folder above
models_dir = Path(__file__).resolve().parent.parent / "models"


# models dictionary
models = {'Source':joblib.load(models_dir / "source_model.joblib"),
          'Assigned':joblib.load(models_dir / "assigned_model.joblib"),
          'Dynamic':joblib.load(models_dir / "dynamic_model.joblib")}


with open (models_dir / "thresholds.json","r") as f:
    thresholds = json.load(f)