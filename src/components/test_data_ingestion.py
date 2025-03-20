from src.components.data_ingestion import DataIngestion
from src.logger import logging
# Provide the path to your CSV file
file_path = "data\student_depression_dataset.csv"

# Create an instance of DataIngestion
data_ingestion = DataIngestion(file_path)

# Load data
data = data_ingestion.load_data()

# Log the record
logging.info("Data ingestion test completed successfully! ")
print(data)

# Check if DataFrame is empty
if data.empty:
    print("Error: DataFrame is empty!")
else:
    print("Success: Data loaded correctly!")
