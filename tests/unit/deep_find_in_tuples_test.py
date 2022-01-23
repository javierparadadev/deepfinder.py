import unittest

from deepfinder import deep_find


class TestFindInTuples(unittest.TestCase):
    def test_first_value_of_a_tuple(self):
        """
        Should return first value of a tuple.
        """
        data = (1, 2, 3)
        result = deep_find(data, '0')
        self.assertEqual(result, 1)

    def test_tuple_access_by_non_numeric_value(self):
        """
        Should return None if tuple index is not numeric
        """
        data = (1, 2, 3)
        result = deep_find(data, 'b')
        self.assertEqual(result, None)

    def test_tuple_access_by_not_hashable_json(self):
        """
        Should return None if tuple index is not numeric
        """
        data = (1, 2, 3)
        result = deep_find(data, '[]')
        self.assertEqual(result, None)

    def test_first_value_of_embedded_tuple(self):
        """
        Should return first value of a embedded tuple.
        """
        data: dict = {
            'values': (1, 2, 3),
        }
        result = deep_find(data, 'values.0')
        self.assertEqual(result, 1)

    def test_all_values_of_tuple(self):
        """
        Should return all values of a tuple.
        """
        data: dict = {
            'values': (1, 2, 3),
        }
        result = deep_find(data, 'values.*')
        self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
