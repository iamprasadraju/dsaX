from algox.search import linearsearch
from algox.helpers import animate, generate, benchmark


@animate
def perf_LinearSearch():
	for size, arr in generate():
		target = arr[-1]
		time, mem = benchmark(linearsearch, arr, target)
		yield size, time, mem
		
perf_LinearSearch()