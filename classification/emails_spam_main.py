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

decision_tree = DecisionTree(train_data_std, test_data_std, train_result)
