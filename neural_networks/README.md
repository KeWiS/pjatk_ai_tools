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