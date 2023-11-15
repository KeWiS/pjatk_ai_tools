import numpy as np


class Recommender:
    def __init__(self, movies_dict_en):
        self._movies_dict_en = movies_dict_en
        print("Recommender")

    def calculate_distance_score(self):
        score_dict = {}
        lecturer = list(self._movies_dict_en.items())[0][1]

        for user in list(self._movies_dict_en.items())[1:]:
            user_values = user[1]

            euclidean = self._euclidean_score(lecturer, user_values)
            pearson = self._pearson_score(lecturer, user_values)

            score_dict[user[0]] = {"euclidean": euclidean, "pearson": pearson}

        return score_dict

    def _euclidean_score(self, user1, user2):
        common_movies = {}

        for item in user1:
            if item in user2:
                common_movies[item] = 1

        if len(common_movies) == 0:
            return 0

        squared_diff = []

        for item in user1:
            if item in user2:
                squared_diff.append(np.square(user1[item] - user2[item]))

        return 1 / (1 + np.sqrt(np.sum(squared_diff)))

    def _pearson_score(self, user1, user2):
        common_movies = {}

        for item in user1:
            if item in user2:
                common_movies[item] = 1

        num_ratings = len(common_movies)

        if num_ratings == 0:
            return 0

        user1_sum = np.sum([user1[item] for item in common_movies])
        user2_sum = np.sum([user2[item] for item in common_movies])

        user1_squared_sum = np.sum([np.square(user1[item]) for item in common_movies])
        user2_squared_sum = np.sum([np.square(user2[item]) for item in common_movies])

        sum_of_products = np.sum([user1[item] * user2[item] for item in common_movies])

        Sxy = sum_of_products - (user1_sum * user2_sum / num_ratings)
        Sxx = user1_squared_sum - np.square(user1_sum) / num_ratings
        Syy = user2_squared_sum - np.square(user2_sum) / num_ratings

        if Sxx * Syy == 0:
            return 0

        return Sxy / np.sqrt(Sxx * Syy)
