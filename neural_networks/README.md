# Neural networks

Authors: Zuzanna Bernacka, Michał Siwek

Neural networks training based on TensorFlow library on 4 datasets: banknote authenticity, CIFAR10, Zalando fashion MNIST-like dataset, email spam classification.<br>

Code has been developed in PyCharm and Visual Studio Code.


Datasets:
* banknote authenticity dataset - [link](http://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt)
* CIFAR10 - [link](https://www.cs.toronto.edu/~kriz/cifar.html)
* Zalando fashion MNIST-like dataset - [link](https://github.com/zalandoresearch/fashion-mnist)
* email spam classification - [link](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv)

Used external libraries:
* TensorFlow - [link](https://www.tensorflow.org/install)

<h1>Installation and running instructions (for Ubuntu)</h1>

```
apt-get update && apt-get install -y python3 python3-pip
python -m pip install tensorflow
python banknote.py
*or*
python emails.py
*or*
python animals.py
*or*
python fashion.py
```

<h1>Neural networks training results:</h1>
<h2>Banknote authenticity</h2>

1. Banknote authenticity neural network - 2 layers with 50 neurons, 100 epochs and confusion matrix
![Banknote authenticity neural network](banknote_neural_network.png)
2. Banknote authenticity learning curve - accuracy
![Banknote authenticity learning curve accuracy](banknote_epoch_accuracy.png)
3. Banknote authenticity learning curve - loss
![Banknote authenticity learning curve loss](banknote_epoch_loss.png)
4. Banknote authenticity decision tree and SVM comparison
![Banknote authenticity classifiers comparison](banknote_classifiers.png)

<h2>Zalando clothes recognizing</h2>
<h3> Neural network with 2 layers, 100 neurons and 10 epochs</h3>

1. Zalando clothes recognizing neural network - 2 layers with 100 neurons, 10 epochs
![Zalando clothes recognizing](fashion_neural_network.png)
2. Zalando clothes recognizing learning curve - accuracy
![Zalando clothes learning curve accuracy](fashion_epoch_accuracy.png)
3. Zalando clothes recognizing learning curve - loss
![Zalando clothes learning curve loss](fashion_epoch_loss.png)

<h3>Neural network with 4 layers, 300 neurons, 10 epochs</h3>

4. Zalando clothes recognizing neural network - 4 layers with 300 neurons, 10 epochs
![Zalando clothes recognizing neural network larger](fashion_larger_neural_network.png)
5. Zalando clothes recognizing learning curve - accuracy
![Zalando clothes recognizing learning curve accuracy](fashion_larger_epoch_accuracy.png)
6. Zalando clothes recognizing learning curve - loss
![Zalando clothes recognizing learning curve loss](fashion_larger_epoch_loss.png)
7. Zalando clothes recognizing TensorBoard
![clothes TensorBoard](fashion_tensorboard.png)

<h3>Neural network with 2 layers, 100 neurons, 50 epochs</h3>

8. Zalando clothes recognizing TensorBoard - 100 neurons, 2 layers
![fashion 100 neurons tensorboard](fashion_100_neurons_tensorboard.png)
9. Zalando clothes recognizing neural network - 100 neurons, 2 layers
![fashion 100 neurons neural network](fashion_100n_50e.png)
10. Zalando clothes recognizing learning curve - accuracy (100 neurons, 50 epochs)
![fashion epoch accuracy 100n 50e](fashion_epoch_accuracy_100n_50e.png)
11. Zalando clothes recognizing learning curve - loss (100 neurons, 50 epochs)
![fashion epoch loss 100n 50e](fashion_epoch_loss_100n_50e.png)

<h3>Neural network with 2 layers, 300 neurons, 10 epochs</h3>

9. Zalando clothes recognizing neural network - 300 neurons, 2 layers, 50 epochs
![fashion 100 neurons neural network](fashion_300n_50e.png)
10. Zalando clothes recognizing learning curve - accuracy (300 neurons, 50 epochs)
![fashion epoch accuracy 100n 50e](fashion_epoch_accuracy_300n_50e.png)
11. Zalando clothes recognizing learning curve - loss (300 neurons, 50 epochs)
![fashion epoch loss 100n 50e](fashion_epoch_loss_300n_50e.png)