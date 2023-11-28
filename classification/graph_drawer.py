import matplotlib.pyplot as plt


class GraphDrawer:
    @staticmethod
    def draw_accuracy_graph(classifier_names, accuracy_scores, bar_colors):
        figure, axes = plt.subplots()

        axes.bar(classifier_names, accuracy_scores, label = classifier_names, color = bar_colors)
        axes.set_title("Classifier accuracy")
        axes.legend(title = "Classifier")
        plt.show()
