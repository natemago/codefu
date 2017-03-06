from math import factorial as fac

def comb(r, n):
  if r == 0:
    return 1
  return fac(n)/(fac(r)*fac(n-r))


def count(m, n, t, k, l):
  total = 0
  ki = 0
  while ki <= (m - k):
    li = 0
    while li <= (n - l):
      if (ki + li + l + k) == t:
        if (ki + k) > 0 or (li + l) > 0:
          print(ki+k, 'of', m, 'actors', li+l, 'of', n, 'actresses. for total', t)
          total += comb(ki+k, m)*comb(li+l, n)
          print('total=', total)
      li += 1
    ki += 1
  return int(total)%1000007


#Test Case 1:
assert count(1, 1, 1, 0, 0) == 2

#Test Case 2:
assert count(1, 9, 9, 0, 4) == 10

#Test Case 3:
assert count(4, 8, 3, 2, 0) == 52

#Test Case 4:
assert count(4, 6, 9, 1, 2) == 10

#Test Case 5:
assert count(7, 5, 9, 2, 0) == 220

#Test Case 6:
assert count(5, 20, 24, 1, 6) == 25

#Test Case 7:
assert count(11, 8, 16, 1, 3) == 969

#Test Case 8:
assert count(15, 1, 3, 1, 0) == 560

#Test Case 9:
assert count(17, 3, 4, 0, 1) == 2465

#Test Case 10:
assert count(9, 17, 13, 3, 5) == 894549