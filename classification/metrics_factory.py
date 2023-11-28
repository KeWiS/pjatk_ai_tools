from sklearn.metrics import confusion_matrix, accuracy_score


class MetricsFactory:
    """
    MetricsFactory

    Class responsible for generating and printing metrics of classifier model
    """

    def __init__(self, classifier, test_result, prediction):
        self._classifier = classifier
        self._test_result = test_result
        self._prediction = prediction

    def print_confusion_matrix(self, acc_score):
        """
        Creates and displays confusion matrix for predicted data by classifier model

        :param acc_score: accuracy score of model's predictions
        :type acc_score: float
        """
        matrix = confusion_matrix(self._test_result, self._prediction)

        print(f"{self._classifier}, confusion matrix:")
        print(f"TP: {matrix[0][0]}  |   FN: {matrix[0][1]}")
        print(f"FP: {matrix[1][0]}  |   TN: {matrix[1][1]}")
        print(f"Accuracy: {acc_score}%\n")

    def calculate_accuracy_score(self):
        """
        Calculates accuracy of the model's predictions based on test data and predicted classes

        :return: Percentage accuracy score of model's predictions
        :rtype: float
        """
        return round(accuracy_score(self._test_result, self._prediction) * 100, 2)
