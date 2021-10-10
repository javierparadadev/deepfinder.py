import unittest

from deepfinder.entity import DeepFinderList, DeepFinderDict


class TestNativeDeepFind(unittest.TestCase):

    def test_deep_finder_list(self):
        """
        Should run deepFind in list.
        """
        data: [str] = DeepFinderList(['a', 'b', 'c'])
        result = data.deep_find('0')
        self.assertEqual(result, 'a')

    def test_deep_finder_dict(self):
        """
        Should run deepFind in dict.
        """
        data: [str] = DeepFinderDict({'a': 'b', 'c': 'd'})
        result = data.deep_find('a')
        self.assertEqual(result, 'b')


if __name__ == '__main__':
    unittest.main()
