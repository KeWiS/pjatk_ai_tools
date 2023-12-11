import tensorflow as tf
import datetime


class ModelFactory:
    def create_model(self, input_layer, neuron_amounts, outputs):
        layers = [input_layer]

        for neuron_amount in neuron_amounts:
            layers += [tf.keras.layers.Dense(neuron_amount, activation = 'relu')]

        layers += [tf.keras.layers.Dense(outputs, activation = 'sigmoid')]

        return tf.keras.Sequential(layers)

    def train_model(self, model, optimizer, loss_function, log_name, train_data, train_result, epochs):
        model.compile(optimizer = optimizer, loss = loss_function, metrics = ['accuracy'])

        logdir = "logs/fit/" + log_name + "_" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

        tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir = logdir)

        model.fit(train_data, train_result, epochs = epochs, callbacks = [tensorboard_callback])

    def evaluate_model(self, model, test_data, test_result):
        print("\nEvaluating model:")
        loss, accuracy = model.evaluate(test_data, test_result)

        print(f"Final loss: {loss} \nFinal accuracy: {accuracy}")
