import unittest
from dsax.search.BinarySearch import binarysearch
from dsax.helpers import generate

class TestSearching(unittest.TestCase):
	def test_BinarySearch(self):
		for _, arr in generate(upper_limit=1000, step=100):
			tmp = sorted(arr)
			target = tmp[-1]
			self.assertEqual(binarysearch(tmp, target), len(arr) - 1)



if __name__ == "__main__":
	unittest.main()