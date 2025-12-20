from algox.sort import insertionsort
from algox.helpers import generate, benchmark, animate


@animate
def perf_InsertionSort():
	for size, arr in generate():
		time, mem = benchmark(insertionsort, arr)
		yield size, time, mem

perf_InsertionSort()