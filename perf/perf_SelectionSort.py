from dsax.sort.SelectionSort import selection_sort
from dsax.helpers import animate, _timeit, generate
import random

@animate
def perf_SelectionSort(step=50):
	for size, arr in generate(upper_limit= 2000):
		time = _timeit(selection_sort, arr)
		yield size, time

perf_SelectionSort()
