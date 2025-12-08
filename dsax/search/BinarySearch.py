def binarysearch(A: list[int], target: int) -> int:
	left = 0
	right = len(A) - 1

	while left <= right:
		mid = (left + right) // 2
		if A[mid] == target:
			return mid
		elif A[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return None
	
if __name__ == "__main__":	
	A = [1, 2, 3, 4, 5]
	result = binarysearch(A, target = 2)
	print(result)