import unittest
from dsax.sort.SelectionSort import selection_sort
from dsax.helpers import generate

class TestSorting(unittest.TestCase):
	def test_SelectionSort(self):
		for _, arr in generate(upper_limit=1000):
			self.assertEqual(selection_sort(arr, reverse=True), sorted(arr, reverse=True))



if __name__ == "__main__":
	unittest.main()