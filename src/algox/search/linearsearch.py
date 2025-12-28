# Linear Search -> O(n)
def LinearSearch(arr: list[int], target: int):
	for i, val in enumerate(arr):
		if val == target:
			return i
	return None