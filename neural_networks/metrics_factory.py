class MetricsFactory:
    """
    MetricsFactory

    Class responsible for generating and printing metrics of classifier model
    """

    def print_confusion_matrix(self, acc_score, false_negatives, false_positives, true_negatives, true_positives):
        """
        Creates and displays confusion matrix for predicted data by classifier model

        :param acc_score: accuracy score of model's predictions
        :type acc_score: float
        """
        print("\nConfusion matrix:")
        print(f"TP: {true_positives}  |   FN: {false_negatives}")
        print(f"FP: {false_positives}  |   TN: {true_negatives}")
        print(f"Accuracy: {acc_score * 100}%\n")
