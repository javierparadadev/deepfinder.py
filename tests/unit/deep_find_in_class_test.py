import unittest

from deepfinder import deep_find


class TestFindInClass(unittest.TestCase):
    def test_class_attributes(self):
        """
        Test basic class with no profundity level.
        """

        class CustomClass:
            def __init__(self):
                self.a = 'test'

        data: CustomClass = CustomClass()
        result = deep_find(data, 'a')
        self.assertEqual(result, 'test')


if __name__ == '__main__':
    unittest.main()
