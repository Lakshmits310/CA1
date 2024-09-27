import unittest

class TestMovieRecommendation(unittest.TestCase):
    def test_recommend_movies(self):
        user_data = {
            'User_ID': 1,
            'Watched_Genres': ['Action'],
            'Favorite_Actors': ['Actor1']
        }
        result = recommend_movies(user_data, movies_data)
        self.assertGreater(len(result), 0)  # Check that recommendations are made

if _name_ == '_main_':
    unittest.main()
