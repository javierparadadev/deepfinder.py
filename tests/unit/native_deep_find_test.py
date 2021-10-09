import unittest

from deepfinder.nativify import nativify, DeepFinderList, DeepFinderDict


class TestNativeDeepFind(unittest.TestCase):

    def test_first_value_of_a_list(self):
        """
        Should run native deepFind in list.
        """
        data: [str] = DeepFinderList(['a', 'b', 'c'])
        result = data.deep_find('0')
        self.assertEqual(result, 'a')

    def test_first_value_of_a_dict(self):
        """
        Should run native deepFind in dict.
        """
        data: [str] = DeepFinderDict({'a': 'b', 'c': 'd'})
        result = data.deep_find('a')
        self.assertEqual(result, 'b')


if __name__ == '__main__':
    unittest.main()
