import unittest
from typing import Set

from deepfinder import deep_find


class TestFindInSets(unittest.TestCase):
    def test_first_value_of_a_set(self):
        """
        Should return first value of a set.
        """
        data = {1, 2, 3}
        result = deep_find(data, '0')
        self.assertEqual(result, 1)

    def test_set_access_by_non_numeric_value(self):
        """
        Should return None if set index is not numeric
        """
        data = {1, 2, 3}
        result = deep_find(data, 'b')
        self.assertEqual(result, None)

    def test_set_access_by_not_hashable_json(self):
        """
        Should return None if set index is not numeric
        """
        data = {1, 2, 3}
        result = deep_find(data, '[]')
        self.assertEqual(result, None)

    def test_first_value_of_embedded_set(self):
        """
        Should return first value of a embedded set.
        """
        data: dict = {
            'values': {1, 2, 3},
        }
        result = deep_find(data, 'values.0')
        self.assertEqual(result, 1)

    def test_all_values_of_set(self):
        """
        Should return all values of a set.
        """
        data: dict = {
            'values': {1, 2, 3},
        }
        result = deep_find(data, 'values.*')
        self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
