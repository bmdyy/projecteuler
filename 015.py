import math;

def nCr(n, r):
  return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)));

print(nCr(40, 20));
