from dsax.sort import insertionsort
from dsax.helpers import generate, _timeit, animate


@animate
def perf_InsertionSort():
	for size, arr in generate():
		time = _timeit(insertionsort, arr)
		yield size, time
		

perf_InsertionSort()