from dsax.search import linearsearch
from dsax.helpers import _timeit, animate, generate

@animate
def pref_LinearSearch():
	for size, arr in generate(sort=True):
		target = arr[-1]
		time = _timeit(linearsearch, arr, target)
		yield size, time


pref_LinearSearch()