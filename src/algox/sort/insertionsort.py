# Insertion Sort
def InsertionSort(arr: list[int], reverse: bool = False) -> list[int]:
	if reverse:
		comp = lambda a, b: (a < b)
	else:
		comp = lambda a, b: (a > b)
		
	size = len(arr)
	for i in range(1, size):
		key = arr[i]
		j = i - 1
		while j >=0 and comp(arr[j], key):
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
	
	return arr
