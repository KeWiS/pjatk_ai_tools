import matplotlib.pyplot as plt


class GraphDrawer:
    """
    GraphDrawer

    Class responsible for drawing and printing graph for model's predictions accuracies
    """

    @staticmethod
    def draw_accuracy_graph(classifier_names, accuracy_scores, bar_colors):
        """
        Creates and displays graph for given classifiers and their accuracy scores

        :param classifier_names: names of the classifiers used for predictions
        :type classifier_names: tuple
        :param accuracy_scores: accuracy scores corresponding to the models used for predictions
        :type accuracy_scores: tuple
        :param bar_colors: colors of the bards displayed on graph
        :type bar_colors: tuple
        """
        figure, axes = plt.subplots()

        axes.bar(classifier_names, accuracy_scores, label = classifier_names, color = bar_colors)
        axes.set_title("Classifier accuracy")
        axes.legend(title = "Classifier")
        plt.show()
