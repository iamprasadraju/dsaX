from dsax.search import binarysearch
from dsax.helpers import animate, _timeit, generate

@animate
def perf_BinarySearch():
	for size, arr in generate(step = 10, sort=True):
		target = arr[-1]
		time = _timeit(binarysearch, arr, target)
		yield size, time

perf_BinarySearch()
