from sklearn import svm


class SupportVectorMachine:
    def __init__(self, train_data, test_data, train_result):
        self._classifier = svm.SVC()
        self._train_data = train_data
        self._test_data = test_data
        self._train_result = train_result

    def train_model_and_predict(self):
        self._classifier.fit(self._train_data, self._train_result)

        return self._classifier.predict(self._test_data)
