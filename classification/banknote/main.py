from classification.dataset_creator import DatasetCreator
from classification.decision_tree import DecisionTree

DatasetCreator = DatasetCreator("banknote_data.csv", ";")

train_data, test_data, train_result, test_result = DatasetCreator.create_datasets_from_file()
train_data_std, test_data_std = DatasetCreator.standarize_data(train_data, test_data)

decision_tree = DecisionTree(train_data_std, test_data_std, train_result)

dt_prediction = decision_tree.train_model_and_predict()
