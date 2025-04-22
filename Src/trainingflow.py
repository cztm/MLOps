from metaflow import FlowSpec, step
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

class TrainingFlow(FlowSpec):

    @step
    def start(self):
        self.data = pd.read_csv("../Data/student_mental_health.csv")
        self.next(self.preprocess)

    @step
    def preprocess(self):
        df = self.data.copy()
        df = df.dropna()
        
        
        self.features = df.drop(columns=["Do you have Depression?"])
       
        non_numeric_cols = self.features.select_dtypes(include=["object", "datetime"]).columns
        self.features = self.features.drop(columns=non_numeric_cols)
        
        self.labels = LabelEncoder().fit_transform(df["Do you have Depression?"])

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.features, self.labels, test_size=0.2)
        self.next(self.train_model)

    @step
    def train_model(self):
        self.model = DecisionTreeClassifier()
        self.model.fit(self.X_train, self.y_train)
        self.predictions = self.model.predict(self.X_test)
        self.accuracy = accuracy_score(self.y_test, self.predictions)
        self.next(self.register_model)

    @step
    def register_model(self):
        mlflow.set_tracking_uri("https://mlflow-server-152716764493.us-west2.run.app")
        mlflow.set_experiment("student-mental-health")
        with mlflow.start_run():
            mlflow.log_param("model_type", "DecisionTree")
            mlflow.log_metric("accuracy", self.accuracy)
            mlflow.sklearn.log_model(
                sk_model=self.model,
                artifact_path="model",
                registered_model_name="student-mental-health-model"
            )
        self.next(self.end)

    @step
    def end(self):
        print(f" Model trained and registered with accuracy: {self.accuracy:.4f}")

if __name__ == '__main__':
    TrainingFlow()
