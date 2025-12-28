# Selection Sort
def SelectionSort(arr: list[int], reverse: bool = False) -> list[int]:
	if reverse:
	 	comp = lambda a, b: (a < b)
	else: 
		comp = lambda a, b: (a > b)
		
	size = len(arr)
	for i in range(size):
		for j in range(i, size):
			if comp(arr[i], arr[j]):
				arr[i], arr[j] = arr[j], arr[i]
				
	return arr