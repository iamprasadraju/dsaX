# Optimized Bubble Sort
def bubble_sort(arr: list[int], reverse=False) -> list[int]:
	n = len(arr)
	swapped = True
	
	if reverse:	
		for i in range(n-1):
			swapped = False
			for j in range(0, n - i - 1):
				if arr[j] < arr[j + 1]:
					arr[j], arr[j + 1] = arr[j + 1], arr[j]
					swapped = True
			if not swapped:
				break
		return arr
	else:
		for i in range(n-1):
			swapped = False
			for j in range(0, n - i - 1):
				if arr[j] > arr[j + 1]:
					arr[j], arr[j + 1] = arr[j + 1], arr[j]
					swapped = True
			if not swapped:
				break
		return arr
			
		
if __name__ == "__main__":
	result = bubble_sort([2, 1, 5, 7, 9, 5])
	print(result)