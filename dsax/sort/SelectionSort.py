def selection_sort(arr: list[int], reverse=False) -> list[int]:
	n = len(arr)
	if reverse:
		for i in range(n):
			idx = i # descending
			for j in range(i+1, n):
				if arr[j] > arr[idx]:
					idx = j
			arr[i], arr[idx] = arr[idx], arr[i]
		return arr
	else:
		for i in range(n):
			idx = i # ascending
			for j in range(i+1, n):
				if arr[j] < arr[idx]:
					idx = j
			arr[i], arr[idx] = arr[idx], arr[i]
		return arr
	
	
if __name__ == "__main__":
	arr = [2, 1, 7, 4, 2, 9, 5]
	print(selection_sort(arr))
	print(sorted(arr) == selection_sort(arr))