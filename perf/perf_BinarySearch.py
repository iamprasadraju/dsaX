from algox.search import binarysearch
from algox.helpers import animate, benchmark, generate

@animate
def perf_BinarySearch():
	for size, arr in generate(step = 10, sort=True):
		target = arr[-1]
		time, mem = benchmark(binarysearch, arr, target)
		yield size, time, mem

perf_BinarySearch()
