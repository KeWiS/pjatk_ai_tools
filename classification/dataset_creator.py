import csv

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class DatasetCreator:
    def __init__(self, file_path, data_delimiter):
        self._file_path = file_path
        self._data_delimiter = data_delimiter

    def create_datasets_from_file(self):
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

            return train_test_split(data, result, test_size = 0.33, random_state = 1)

    def standarize_data(self, train_data, test_data):
        sc = StandardScaler()
        sc.fit(train_data)
        train_data_std = sc.transform(train_data)
        test_data_std = sc.transform(test_data)

        return train_data_std, test_data_std
