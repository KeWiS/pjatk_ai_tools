import numpy as np
import tensorflow as tf

from dataset_creator import DatasetCreator
from model_factory import ModelFactory

# Dataset creation and standardization
DatasetCreator = DatasetCreator("banknote_data.csv", ";")

train_data, test_data, train_result, test_result = DatasetCreator.create_datasets_from_file()
train_data_std, test_data_std = DatasetCreator.standardize_data(train_data, test_data)
train_result = np.array(train_result)
test_result = np.array(test_result)

# Model creation, training and evaluation
model_factory = ModelFactory()

input_layer = tf.keras.layers.Input(shape = (None, 4))

model = model_factory.create_model(input_layer, [50, 50], 1)

loss_function = tf.keras.losses.BinaryCrossentropy()

model_factory.train_model(model, "adam", loss_function, "banknote", train_data_std, train_result, 100)

model_factory.evaluate_model(model, test_data_std, test_result)
