from algox.sort import selectionsort
from algox.helpers import benchmark, generate, animate

@animate
def perf_SelectionSort():
    for size, arr in generate():
        time, mem = benchmark(selectionsort, arr)
        yield size, time, mem

perf_SelectionSort()
