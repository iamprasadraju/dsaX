from dsax.sort.BubbleSort import bubble_sort
from dsax.helpers import animate, _timeit, generate

@animate
def perf_BubbleSort():
	for size, arr in generate(upper_limit=2000, ste):
		time = _timeit(bubble_sort, arr)
		yield size, time
		
		
perf_BubbleSort()