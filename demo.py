# below code is to check the logging config
# import sys
# from src.exception import MyException
# from src.logger import logging

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")


# below code is to check the exception config

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e


# from src.pipline.training_pipeline import TrainPipeline

# pipline = TrainPipeline()
# pipline.run_pipeline()


from src.pipeline.training_pipeline import TrainingPipeline

if __name__ == "__main__":
    data_path = "data/student_depression_dataset.csv"
    pipeline = TrainingPipeline(data_path)
    accuracy, report = pipeline.run_pipeline()

    print(f"Model accuracy: {accuracy:.4f}")
    print(f"Classification report: ", report)
