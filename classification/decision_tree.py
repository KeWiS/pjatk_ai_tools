from sklearn.tree import DecisionTreeClassifier


class DecisionTree():
    """
    DecisionTree class - implementing DecisionTreeClassifier model training and predictions with given datasets
    """

    def __init__(self, train_data, test_data, train_result):
        self._classifier = DecisionTreeClassifier()
        self._train_data = train_data
        self._test_data = test_data
        self._train_result = train_result

    def train_model_and_predict(self):
        """
        Trains the model on train data and predicts classes based on test data

        :return: The predicted classes
        """
        self._classifier.fit(self._train_data, self._train_result)

        return self._classifier.predict(self._test_data)
