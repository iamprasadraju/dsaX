import unittest
from dsax.sort import selectionsort, bubblesort, insertionsort
from dsax.helpers import generate

class TestSorting(unittest.TestCase):
	def test_SelectionSort(self):
		for _, arr in generate():
			self.assertEqual(selectionsort(arr), sorted(arr))
			
	def test_BubbleSort(self):
		for _, arr in generate():
			self.assertEqual(bubblesort(arr), sorted(arr))
			
	def test_InsertionSort(self):
		for _, arr in generate():
			self.assertEqual(insertionsort(arr), sorted(arr))
			
	

if __name__ == "__main__":
	unittest.main()