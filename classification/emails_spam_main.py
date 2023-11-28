from dataset_creator import DatasetCreator
from decision_tree import DecisionTree
from graph_drawer import GraphDrawer
from metrics_factory import MetricsFactory
from svm import SupportVectorMachine

# Dataset creation and standardization
DatasetCreator = DatasetCreator("emails_data.csv", ",")

train_data, test_data, train_result, test_result = DatasetCreator.create_datasets_from_file()
train_data_std, test_data_std = DatasetCreator.standardize_data(train_data, test_data)

# Classifier configuration
decision_tree_classifier_name = "Decision Tree"
support_vector_machine_classifier_name = "Support Vector Machine"

decision_tree = DecisionTree(train_data_std, test_data_std, train_result)
support_vector_machine = SupportVectorMachine(train_data_std, test_data_std, train_result)

# Training models and making predictions
dt_prediction = decision_tree.train_model_and_predict()
svm_prediction = support_vector_machine.train_model_and_predict()

# Metrics creation
dt_metrics_factory = MetricsFactory(decision_tree_classifier_name, test_result, dt_prediction)
svm_metrics_factory = MetricsFactory(support_vector_machine_classifier_name, test_result, svm_prediction)

# Calculating accuracy scores
dt_accuracy_score = dt_metrics_factory.calculate_accuracy_score()
svm_accuracy_score = svm_metrics_factory.calculate_accuracy_score()

# Printing confusion matrices
dt_metrics_factory.print_confusion_matrix(dt_accuracy_score)
svm_metrics_factory.print_confusion_matrix(svm_accuracy_score)

# Graph configuration
classifier_names = [decision_tree_classifier_name, support_vector_machine_classifier_name]
bar_colors = ["blue", "green"]
accuracies = [dt_accuracy_score, svm_accuracy_score]

# Drawing graph
GraphDrawer.draw_accuracy_graph(classifier_names, accuracies, bar_colors)
