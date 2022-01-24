import unittest

from deepfinder import deep_find


class TestFindDefault(unittest.TestCase):
    def test_with_basic_dict(self):
        """
        Return default if attribute is not present
        """
        data: dict = {'any': 'any'}
        result = deep_find(data, 'some', default='default')
        self.assertEqual(result, 'default')

    def test_with_list_and_find_all(self):
        """
        Return none list if does not match
        """
        data: list = [{'any': 'any'}]
        result = deep_find(data, '*.some', default='default')
        self.assertEqual(result, [None])

    def test_with_list_and_find_all_without_nulls(self):
        """
        Return empty list if does not match
        """
        data: list = [{'any': 'any'}]
        result = deep_find(data, '?*.some', default='default')
        self.assertEqual(result, [])

    def test_with_list_and_find_some(self):
        """
        Return default if attribute is not present
        """
        data: list = [{'any': 'any'}]
        result = deep_find(data, '?.some', default='default')
        self.assertEqual(result, 'default')


if __name__ == '__main__':
    unittest.main()
