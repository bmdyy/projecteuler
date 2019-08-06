def prime_factors(n):
  factors = [];
  while n%2==0:
    factors.append(2);
    n/=2;
  for i in range (3, int(n ** 0.5) + 1, 2):
    while n%i==0:
      factors.append(i);
      n/=i;
  if n>2:
    factors.append(n);
  return set(factors);

def rad(n):
  x = 1;
  for f in prime_factors(n):
    x *= f;
  return x;

def table(n):
  t = [];
  for i in range(1, n + 1):
    t.append([i, rad(i)]);
  return t;

def mergesort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2;
    L = arr[:mid];
    R = arr[mid:];
    mergesort(L);
    mergesort(R);
    i = j = k = 0;
    while i < len(L) and j < len(R):
      if L[i][1] < R[j][1]:
        arr[k] = L[i];
        i+=1;
      elif L[i][1] > R[j][1]:
        arr[k] = R[j];
        j+=1;
      else: # equal
        if L[i][0] < R[j][0]:
          arr[k] = L[i];
          i+=1;
        else:
          arr[k] = R[j];
          j+=1;
      k+=1;
    while i < len(L):
      arr[k] = L[i];
      i+=1;
      k+=1;
    while j < len(R):
      arr[k] = R[j];
      j+=1;
      k+=1;

def sorted_table(n):
  t = table(n);
  mergesort(t);
  return t;

def E(t, k):
  return t[k - 1][0];

print(E(sorted_table(100000), 10000));
