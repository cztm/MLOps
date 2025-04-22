from metaflow import FlowSpec, step
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.preprocessing import LabelEncoder

class ScoringFlow(FlowSpec):

    @step
    def start(self):
        # Load dataset
        df = pd.read_csv("../Data/student_mental_health.csv")
        df = df.dropna()

        # Identify non-numeric columns first
        non_numeric_cols = df.select_dtypes(include=["object", "datetime"]).columns
        numeric_df = df.drop(columns=[col for col in non_numeric_cols if col != "Do you have Depression?"])

        # Simulate new data by using a 20% holdout
        holdout = numeric_df.sample(frac=0.2)
        self.X_holdout = holdout.drop(columns=["Do you have Depression?"])
        self.y_true = LabelEncoder().fit_transform(holdout["Do you have Depression?"])
        self.next(self.load_model)

    @step
    def load_model(self):
        # Connect to MLflow server and load latest Production model
        mlflow.set_tracking_uri("https://mlflow-server-152716764493.us-west2.run.app")
        model_uri = "models:/student-mental-health-model/1"
        self.model = mlflow.sklearn.load_model(model_uri)
        self.next(self.score)

    @step
    def score(self):
        # Make predictions on the holdout set
        self.predictions = self.model.predict(self.X_holdout)
        self.next(self.end)

    @step
    def end(self):
        # Display a few predictions with true labels
        print("Scoring completed. Sample predictions:")
        print(list(zip(self.predictions[:5], self.y_true[:5])))

if __name__ == '__main__':
    ScoringFlow()

