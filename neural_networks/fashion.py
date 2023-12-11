import tensorflow as tf

from model_factory import ModelFactory

# Dataset creation and standardization
fashion_mnist = tf.keras.datasets.fashion_mnist

(train_data, train_result), (test_data, test_result) = fashion_mnist.load_data()

# Class names for the images, their position in array corresponds to the actual label they have in the dataset
# class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Standardization of data, here it is simple because we can simply divide values by 255
train_data = train_data / 255.0
test_data = test_data / 255.0

# Model creation, training and evaluation
model_factory = ModelFactory()

input_layer = tf.keras.layers.Flatten(input_shape = (28, 28))

model = model_factory.create_model(input_layer, [100, 100], 10)

loss_function = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True)

model_factory.train_model(model, "adam", loss_function, "fashion", train_data, train_result, 10)

model_factory.evaluate_model(model, test_data, test_result)
