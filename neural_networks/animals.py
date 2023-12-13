import numpy as np
import tensorflow as tf

from model_factory import ModelFactory

# Dataset creation and standardization
animals_mnist = tf.keras.datasets.cifar10

(train_data, train_result), (test_data, test_result) = animals_mnist.load_data()

# Standardization of data, here it is simple because we can simply divide values by 255
train_data = train_data / 255.0
test_data = test_data / 255.0
train_result = train_result.flatten()
test_result = test_result.flatten()
train_result = tf.one_hot(train_result.astype(np.int32), depth = 10)
test_result = tf.one_hot(test_result.astype(np.int32), depth = 10)

# Model creation, training and evaluation
model_factory = ModelFactory()

input_layer = tf.keras.layers.Flatten(input_shape = (32, 32, 3))

model = model_factory.create_model(input_layer, [100, 100], 10)

loss_function = tf.keras.losses.CategoricalCrossentropy()

model_factory.train_model(model, "adam", loss_function, "cifar10", train_data, train_result, 10)

model_factory.evaluate_model(model, test_data, test_result)
