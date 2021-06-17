import unittest
from sort_array import sort_array

class TestSortArray(unittest.TestCase):
    def test_sort_array(self):
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
        self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])

if __name__ == '__main__':
    unittest.main()
