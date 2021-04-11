import unittest

from deepgetter.deep_get import deep_get


class TestSum(unittest.TestCase):
    def test_dict_with_0_lvl(self):
        """
        Test basic dictionary with no profundity level.
        """
        data: dict = {
            'value': 39,
        }
        result = deep_get(data, '')
        self.assertEqual(result, data)

    def test_dict_with_1_lvl(self):
        """
        Test basic dictionary with one profundity level.
        """
        data: dict = {
            'value': 39,
        }
        result = deep_get(data, 'value')
        self.assertEqual(result, 39)

    def test_dict_with_2_lvl(self):
        """
        Test basic dictionary with two profundity levels.
        """
        data: dict = {
            'value': {
                'subdata': 39,
            },
        }
        result = deep_get(data, 'value.subdata')
        self.assertEqual(result, 39)


if __name__ == '__main__':
    unittest.main()
