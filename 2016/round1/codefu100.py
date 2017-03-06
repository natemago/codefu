def findIt(arr):
  s = set()
  for i in arr:
    if i in s:
      s.remove(i)
    else:
      s.add(i)
  return s.pop()

#Test Case 1:
assert findIt([1, 2, 1]) == 2

#Test Case 2:
assert findIt([2, 5, 1, 5, 2]) == 1

#Test Case 3:
assert findIt([3]) == 3

#Test Case 4:
assert findIt([4, 3, 2, 1, 1, 2, 3]) == 4

#Test Case 5:
assert findIt([1, 3, 5, 7, 9, 7, 5, 3, 1]) == 9

#Test Case 6:
assert findIt([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 6, 7, 8, 9]) == 5

#Test Case 7:
assert findIt([2, 8, 2, 6, 6, 4, 4]) == 8

#Test Case 8:
assert findIt([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10

#Test Case 9:
assert findIt([5, 4, 3, 2, 1, 5, 4, 3, 2]) == 1

#Test Case 10:
assert findIt([11, 22, 33, 44, 55, 66, 77, 66, 55, 44, 33, 22, 11]) == 77