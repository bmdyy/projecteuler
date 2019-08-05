from math import sqrt;

def pent_num(n):
  return n * (3 * n - 1) / 2;

def is_pent(n):
  if n < 0:
    return False;
  return (1 + sqrt(1 + 24*n)) / 6 % 1 == 0;

for j in range(1, 5000):
  p_j = pent_num(j);
  for k in range(1, 5000):
    p_k = pent_num(k);
    s = p_j + p_k;
    if not is_pent(s):
      continue;
    d = p_k - p_j;
    if not is_pent(d):
      continue;
    print(d);
