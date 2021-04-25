import unittest

from src.deep_find import deep_find


class TestFindInLists(unittest.TestCase):
    def test_first_value_of_a_list(self):
        """
        Should return first value of a list.
        """
        data: [str] = ['a', 'b', 'c']
        result = deep_find(data, '0')
        self.assertEqual(result, 'a')

    def test_first_value_of_embedded_list(self):
        """
        Should return first value of a embedded list.
        """
        data: dict = {
            'values': ['a', 'b', 'c'],
        }
        result = deep_find(data, 'values.0')
        self.assertEqual(result, 'a')

    def test_all_values_of_list(self):
        """
        Should return all values of a list.
        """
        data: dict = {
            'values': ['a', 'b', 'c'],
        }
        result = deep_find(data, 'values.*')
        self.assertEqual(result, data['values'])

    def test_first_value_in_dict_of_a_list(self):
        """
        Should return first subvalue of a list.
        """
        data: dict = {
            'values': [{
                'value': 'a',
            }, {
                'value': 'b',
            }, {
                'value': 'c',
            }],
        }
        result = deep_find(data, 'values.0.value')
        self.assertEqual(result, 'a')

    def test_all_values_of_a_list(self):
        """
        Should return all subvalues of a list.
        """
        data: dict = {
            'values': [{
                'value': 'a',
            }, {
                'value': 'b',
            }, {
                'value': 'c',
            }],
        }
        result = deep_find(data, 'values.*.value')
        self.assertEqual(result, [value['value'] for value in data['values']])

    def test_existing_path_values_of_a_list(self):
        """
        Should return first existing path in list.
        """
        data: dict = {
            'values': [{
                'nya': 'a',
            }, {
                'value': 'b',
            }, {
                'nya': 'c',
            }],
        }
        result = deep_find(data, 'values.?.value')
        self.assertEqual(result, 'b')

    def test_all_values_of_a_list_inside_list(self):
        """
        Should return complete lists inside list.
        """
        data: dict = {
            'all-values': [{
                'values': ['a'],
            }, {
                'values': ['b', 'c', 'd'],
            }, {
                'values': ['e'],
            }],
        }
        result = deep_find(data, 'all-values.*.values')
        self.assertEqual(result, [['a'], ['b', 'c', 'd'], ['e']])

    def test_complete_list_inside_list(self):
        """
        Should return complete lists inside direct list.
        """
        data: dict = {
            'all-values': [['a'], ['b', 'c', 'd'], ['e']],
        }
        result = deep_find(data, 'all-values.*.*')
        self.assertEqual(result, [['a'], ['b', 'c', 'd'], ['e']])

    def test_first_value_of_list_inside_list(self):
        """
        Should return first value of all lists inside list.
        """
        data: dict = {
            'all-values': [['a'], ['b', '3', '4'], ['c']],
        }
        result = deep_find(data, 'all-values.*.0')
        self.assertEqual(result, ['a', 'b', 'c'])

    def test_existing_path_of_list_inside_list(self):
        """
        Should return existing path of lists inside direct list.
        """
        data: dict = {
            'all-values': [['a'], ['b', 'c', 'd'], ['e']],
        }
        result = deep_find(data, 'all-values.?.2')
        self.assertEqual(result, 'd')

    def test_existing_path_inside_existing_path(self):
        """
        Should return existing path inside existing path of lists inside list.
        """
        data: dict = {
            'all-values': [['a'], ['b', {'correct': 'correct'}, 'c'], ['d']],
        }
        result = deep_find(data, 'all-values.?.?.correct')
        self.assertEqual(result, 'correct')


if __name__ == '__main__':
    unittest.main()
