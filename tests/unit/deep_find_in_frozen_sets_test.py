import unittest
from typing import Set

from deepfinder import deep_find


class TestFindInfrozenSets(unittest.TestCase):
    def test_first_value_of_a_frozen_set(self):
        """
        Should return first value of a set.
        """
        data = frozenset((1, 2, 3))
        result = deep_find(data, '0')
        self.assertEqual(result, 1)

    def test_frozen_set_access_by_non_numeric_value(self):
        """
        Should return None if set index is not numeric
        """
        data = frozenset((1, 2, 3))
        result = deep_find(data, 'b')
        self.assertEqual(result, None)

    def test_frozen_set_access_by_not_hashable_json(self):
        """
        Should return None if set index is not numeric
        """
        data = frozenset((1, 2, 3))
        result = deep_find(data, '[]')
        self.assertEqual(result, None)

    def test_first_value_of_embedded_frozen_set(self):
        """
        Should return first value of a embedded set.
        """
        data: dict = {
            'values': frozenset((1, 2, 3)),
        }
        result = deep_find(data, 'values.0')
        self.assertEqual(result, 1)

    def test_all_values_of_frozen_set(self):
        """
        Should return all values of a set.
        """
        data: dict = {
            'values': frozenset((1, 2, 3)),
        }
        result = deep_find(data, 'values.*')
        self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
