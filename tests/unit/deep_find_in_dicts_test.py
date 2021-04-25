import unittest

from src.deepfinder import deep_find


class TestFindInDicts(unittest.TestCase):
    def test_dict_with_0_lvl(self):
        """
        Test basic dictionary with no profundity level.
        """
        data: dict = {
            'value': 39,
        }
        result = deep_find(data, '')
        self.assertEqual(result, data)

    def test_dict_with_1_lvl(self):
        """
        Test basic dictionary with one profundity level.
        """
        data: dict = {
            'value': 39,
        }
        result = deep_find(data, 'value')
        self.assertEqual(result, 39)

    def test_dict_with_2_lvl(self):
        """
        Test basic dictionary with 2 profundity levels.
        """
        data: dict = {
            'value': {
                'subdata': 39,
            },
        }
        result = deep_find(data, 'value.subdata')
        self.assertEqual(result, 39)

    def test_dict_with_3_lvl(self):
        """
        Test basic dictionary with 3 profundity levels.
        """
        data: dict = {
            'value': {
                'sub-data': {
                    'sub-sub-data': 39,
                },
            },
        }
        result = deep_find(data, 'value.sub-data.sub-sub-data')
        self.assertEqual(result, 39)


if __name__ == '__main__':
    unittest.main()
