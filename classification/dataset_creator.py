import csv

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class DatasetCreator:
    """
    DatasetCreator

    Responsible for creating datasets for classifier algorithms
    """

    def __init__(self, file_path, data_delimiter):
        self._file_path = file_path
        self._data_delimiter = data_delimiter

    def create_datasets_from_file(self):
        """
        Opens given csv data source file and converts it into 4 lists:

        Training data, training labels, test data and test labels

        :return: lists containing train-test split of inputs
        """
        with open(self._file_path, 'r') as file:
            plots = csv.reader(file, delimiter = self._data_delimiter)
            has_header = csv.Sniffer().has_header(file.read(1024))
            file.seek(0)

            if has_header:
                next(plots)

            data = []
            result = []

            for row in plots:
                data.append(row[:-1])
                result.append(row[-1])

            return train_test_split(data, result, test_size = 0.33, random_state = None)

    def standardize_data(self, train_data, test_data):
        """
        Uses StandardScaler to standardize data for model training and predictions

        :param train_data: data used for model training
        :type train_data: list
        :param test_data: data used for testing the model (predicting classes)
        :type test_data: list

        :return: lists containing standardized data
        """
        sc = StandardScaler()
        sc.fit(train_data)
        train_data_std = sc.transform(train_data)
        test_data_std = sc.transform(test_data)

        return train_data_std, test_data_std
