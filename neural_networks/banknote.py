import numpy as np

from dataset_creator import DatasetCreator
from model_factory import ModelFactory

# Dataset creation and standardization
DatasetCreator = DatasetCreator("banknote_data.csv", ";")

train_data, test_data, train_result, test_result = DatasetCreator.create_datasets_from_file()
train_data_std, test_data_std = DatasetCreator.standardize_data(train_data, test_data)
train_result = np.array(train_result)
test_result = np.array(test_result)

model_factory = ModelFactory()

model = model_factory.create_model([50, 50], (None, 4), 1)

model_factory.train_model(model, "banknote", train_data_std, train_result, 100)

model_factory.evaluate_model(model, test_data_std, test_result)
