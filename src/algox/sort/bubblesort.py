# Bubble Sort
def BubbleSort(arr: list[int],  reverse: bool = False) -> list[int]:
	if reverse:
		comp = lambda a, b: (a < b)
	else:
		comp = lambda a, b: (a > b)
	
	size = len(arr)
	swapped = True
	
	for i in range(size - 1):
		swapped = False
		for j in range(size - i - 1):
			if comp(arr[j], arr[j + 1]):
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				swapped = True
			
		if not swapped:
			break
	return arr