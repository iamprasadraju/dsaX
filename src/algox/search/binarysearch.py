# Binary Search -> O(log n)

def BinarySearch(arr: list[int], target: int):
	size = len(arr)
	left = 0
	right = size - 1
	
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] == target:
			return mid
		elif target > arr[mid]:
			left = mid + 1
		else:
			right = mid - 1
	return None