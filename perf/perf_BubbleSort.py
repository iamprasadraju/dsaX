from algox.sort import bubblesort
from algox.helpers import animate, benchmark, generate

@animate
def perf_BubbleSort():
	for size, arr in generate(upper=2000, step=20):
		time, mem = benchmark(bubblesort, arr)
		yield size, time, mem
		
perf_BubbleSort()