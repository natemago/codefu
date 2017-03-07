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
  nrc = 1
  print('rc=', rc, 'n=', n, 'total', n-rc)
  while rc <= n:
    res *= rc
    print(rc)
    while res%nrc == 0 and nrc <= nr_lim:
      #print('nrc=', nrc, 'res=', res)
      res //= nrc
      nrc +=1
    
    if nrc > nr_lim:
      res %= mod
      
    rc += 1
  
  return res % mod


MEM = {}

def binom_mem(r, n, mod):
  key = (r,n, mod)
  if MEM.get(key):
    return MEM[key]
  r = binom_mod(r,n,mod)
  MEM[key] = r
  return r


binom = lambda r,n: binom_mem(r,n,1000007)

def sumz(arr, N, mod=1000007):
  coeff = [0 for a in arr]
  
  for i in range(0, len(coeff)):
    print('ai', i, 'of', len(coeff))
    m = len(arr)
    cf = 0
    n = 0
    s = 0
    if N > mod:
      s = N - mod + 1
    while s + n*m+i <= N:
      print('cf', cf, 'from', s + n*m + i, 'to', N)
      cf += int(binom(s + n*m + i, N))
      n += 1
    coeff[i] = cf
  
  res = []
  for i in range(0, len(arr)):
    s = 0
    for j in range(0, len(arr)):
      s += coeff[j]*(arr[j])
    res.append(int(s)%mod)
    coeff = [coeff[-1]] + coeff[0:-1]
  
  return res


def sumz_test(arr, N):
  for i in range(0, N):
    res = []
    for j in range(0, len(arr)):
      res.append( (arr[j] + arr[(j+1)%len(arr)] )%1000007)
    arr = res
    print(arr)
  return arr

#print(sumz1([1,36,66,89,58,63,16,78,10,99,67,46,29,99,92,42,11,16,4], 109))


#import sys
#sys.exit(1)
#Test Case 1:
print('Case 1')
assert sumz([4,2,1], 2) == [9,8,11]

#Test Case 2:
print('Case 2')
assert sumz([3,15,7,1,16], 5) == [241,250,284,297,272]

#Test Case 3:
print('Case 3')
assert sumz([1,36,66,89,58,63,16,78,10,99,67,46,29,99,92,42,11,16,4], 109) == [930544,44670,909263,674386,222785,415636,796691,21207,847119,823411,683987,342624,719360,15823,192706,935726,980568,909280,658345]

#Test Case 4:
print('Case 4')
assert sumz([15,54,38,27,43,90,36,22,62,73,41,10], 191) == [791725,153618,254093,420536,692667,422027,91273,804845,117048,287776,940147,798151]

#Test Case 5:
print('Case 5')
assert sumz([16,47,89,8,93,22,18,19,9,25,89,44], 136) == [94121,182313,284954,595822,580993,646863,440661,559755,4883,34324,841777,228312]

#Test Case 6:
print('Case 6')
assert sumz([73,24,1,11,32,5,58,72,93,34,93,66], 143) == [214718,40745,661056,782201,137397,810059,414988,132886,723530,269412,370340,486726]

#Test Case 7:
print('Case 7')
assert sumz([63,65,93,10,45,30,40,43,92,20,60,42,42,10,77], 135) == [476792,336105,140970,67490,531911,57863,23028,584568,860061,916669,354474,456717,859236,536109,827445]

#Test Case 8:
print('Case 8')
assert sumz([29,86,43,92,85,39,18,43,68,47,31,90,30,81,18], 109) == [87909,285548,152083,858098,876817,103605,695045,538935,937230,642834,970465,528138,13768,625938,576530]

#Test Case 9:
print('Case 9')
assert sumz([18,48,99,55,3,72,48,2,68,34,46,75,81,78,63,80,2], 191) == [820370,922851,380025,727962,98346,242879,322340,118490,711508,544989,574095,957582,697631,670075,71941,102438,672176]

#Test Case 10:
print('Case 10')
assert sumz([15,33,75,19,61,18,3,50,21,67,37,63,94,31,76,96,77,32,5,93,25,20,38,63,33,8,17,62,65,56,84,12,50,80,21,80,43,53,73,90,5,29,63,52,1,35,12,78,49,46], 1710116208) == [111029,262097,373756,99799,561347,349224,229067,919662,659236,60364,265601,878972,619372,193597,520632,640003,683267,159686,176491,323921,982995,771484,773133,270612,287015,693542,373258,744740,48991,385868,338778,425,837662,564428,575895,206923,104391,822374,716087,435381,774297,615557,365990,61584,406835,113115,492148,357464,132029,478473]

