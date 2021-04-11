import unittest

from deepgetter.deep_get import deep_get


class TestGetByType(unittest.TestCase):
    def test_with_basic_number(self):
        """
        Test basic number
        """
        data: int = 39
        result = deep_get(data, '')
        self.assertEqual(result, 39)

    def test_with_number_in_dict(self):
        """
        Test basic number inside structure
        """
        data: dict = {
            'value': 39,
        }
        result = deep_get(data, 'value')
        self.assertEqual(result, 39)

    def test_with_basic_str(self):
        """
        Test basic string
        """
        data: str = 'test str'
        result = deep_get(data, '')
        self.assertEqual(result, 'test str')

    def test_with_str_in_dict(self):
        """
        Test basic string inside structure
        """
        data: dict = {
            'value': 'test str',
        }
        result = deep_get(data, 'value')
        self.assertEqual(result, 'test str')


if __name__ == '__main__':
    unittest.main()
