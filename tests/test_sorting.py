import unittest
from dsax.sort.SelectionSort import selection_sort
from dsax.sort.BubbleSort import bubble_sort
from dsax.helpers import generate

class TestSorting(unittest.TestCase):
	def test_SelectionSort(self):
		for _, arr in generate():
			self.assertEqual(selection_sort(arr, reverse=True), sorted(arr, reverse=True))
	def test_BubbleSort(self):
		for _, arr in generate():
			self.assertEqual(bubble_sort(arr), sorted(arr))

if __name__ == "__main__":
	unittest.main()