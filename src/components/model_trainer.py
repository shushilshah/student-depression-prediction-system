import joblib
from src.logger import logging
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


class ModelTrainer:
    def __init__(self, data):
        self.data = data
        self.model = AdaBoostClassifier(n_estimators=250, random_state=42)

    def train_model(self):
        try:
            logging.info("starting model training.")
            X = self.data.drop(columns=['depression'])
            y = self.data['depression']
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42)

            logging.info(
                f"Dataset split:{X_train.shape[0]} training samples, {X_test.shape[0]} test samples.")

            # Fitting the model
            self.model.fit(X_train, y_train)
            logging.info(f"AdaBoostClassifier model training completed.")
            y_pred = self.model.predict(X_test)

            # Model evaluation
            accuracy = accuracy_score(y_test, y_pred)
            logging.info(f"Model accuracy: {accuracy:.4f}")

            report = classification_report(y_test, y_pred)
            logging.info(f"Classification Report:\n{report}")

            # saving trained model
            joblib.dump(self.model, "model.pkl")
            logging.info("Model saved as 'model.pkl'.")

            return accuracy, report

        except Exception as e:
            logging.error(f"Error occured during model training: {e}")
            raise Exception(f"Model training error: {e}")
