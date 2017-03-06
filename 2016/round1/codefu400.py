def find_idx(i, arr):
  for idx in range(0, len(arr)):
    if arr[idx] == i:
      return idx

def min(arr):
  total = 0
  
  while True:
    swaps = False
    for i in range(0, len(arr)):
      idx = find_idx(i+1, arr)
      if idx != i:
        t = arr[i]
        arr[i] = arr[idx]
        arr[idx] = t
        total += 1
        swaps = True
    if not swaps:
      break
  
  return total


#Test Case 1:
assert min([1]) == 0

#Test Case 2:
assert min([1,2]) == 0

#Test Case 3:
assert min([2,1]) == 1

#Test Case 4:
assert min([4,3,2,1]) == 2

#Test Case 5:
assert min([4,1,3,2]) == 2

#Test Case 6:
assert min([4,1,2,3]) == 3

#Test Case 7:
assert min([2,1,12,10,3,11,13,9,8,4,6,7,5]) == 8

#Test Case 8:
assert min([8,5,16,13,11,17,12,9,2,15,6,7,4,10,14,3,1]) == 12

#Test Case 9:
assert min([9,1,4,3,15,11,6,2,12,13,14,8,10,7,16,5]) == 11

#Test Case 10:
assert min([28,29,8,13,26,3,12,19,2,20,25,7,21,23,1,9,27,6,5,10,17,24,22,11,14,15,16,18,4]) == 24