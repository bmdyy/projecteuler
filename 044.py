def next_pent_num(n):
  return n*(3*n-1)/2;

p = 1;
l_p = 0;
while p < 1000:
  l_p = p;
  p = next_pent_num(p);

  s = l_p + p;
  d = l_p - p;
