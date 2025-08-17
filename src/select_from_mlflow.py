import os
import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
import pandas as pd
from pathlib import Path
import shutil

DB = Path(__file__).resolve().parents[1] / "notebooks" / "mlflow.db"
uri = f"sqlite:///{DB.as_posix()}"
EXPERIMENT_NAME = "chronic-kidney-disease-prediction"
OUTPUT_PATH = Path("models/model.pkl")  # where Docker/API will read from
def export_best_model():
    
    mlflow.set_tracking_uri(uri)
    exp = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
    assert exp is not None, "Experiment not found"

    # Get all runs; filter to child runs (those having a parent) OR just sort all and pick top
    runs_df = mlflow.search_runs(
        experiment_ids=[exp.experiment_id],
        filter_string="",  # optionally: "tags.mlflow.parentRunId != ''"
        output_format="pandas"
    )

    # Keep only runs that have test_accuracy metric
    runs_df = runs_df.dropna(subset=["metrics.test_accuracy"])
    best = runs_df.sort_values("metrics.test_accuracy", ascending=False).iloc[0]
    run_id = best.run_id
    model_uri = f"runs:/{run_id}/model"

    print(f"Best run: {best['tags.mlflow.runName']} ({run_id})  test_accuracy={best['metrics.test_accuracy']:.4f}")

    # load model then re-save as a single pickle for simple deployment
    model = mlflow.sklearn.load_model(model_uri)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    import pickle
    with open(OUTPUT_PATH, "wb") as f:
        pickle.dump(model, f)
    print(f"Exported model to {OUTPUT_PATH.resolve()}")

if __name__ == "__main__":
    export_best_model()
