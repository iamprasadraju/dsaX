from algox.sort import bubblesort
from algox.helpers import animate, _timeit, generate

@animate
def perf_BubbleSort():
	for size, arr in generate(upper_limit=2000, step=20):
		time = _timeit(bubblesort, arr)
		yield size, time
		
		
perf_BubbleSort()