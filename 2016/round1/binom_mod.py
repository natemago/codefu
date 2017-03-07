from math import ceil, factorial as fac

def binom(r, n):
  if r == 0:
    return 1
  return int(fac(n))//int((fac(r))*int(fac(n-r)))




def binom_mod(r, n, mod):
  """
    n        n!         n!       1                        1
  |   | = ---------- = ---- * -------- = P[r+1, n] * -----------
    r      r!(n-r)!     r!     (n-r)!                 P[1, n-r]
  
  n!     = P[1, n]
  r!     = P[1, r]
  (n-r)! = P[1, n-r]

  n - r < mod - so this is bound to [0, mod]
  r - unbound, may be very close to n
  n - unbound
  """
  
  if r == 0:
    return 1
  
  nr_lim = n - r
  
  res = 1
  
  rc = r + 1
  nrc = nr_lim
  while rc <= n:
    res *= rc
    
    while res%nrc == 0 and nrc > 1:
      res //= nrc
      nrc -=1
    
    if nrc == 1:
      res %= mod
      
    rc += 1
  
  return res % mod
  #return res


for i in range(0, 100):
  for j in range(i, 101):
    b1 = binom(i, j) % 100
    b2 = binom_mod(i, j, 100)
    print(i,j,b1,b2)
    assert b1 == b2