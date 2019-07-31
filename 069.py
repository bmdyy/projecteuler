def ggT(a, b):
  i = max(a, b);
  j = min(a, b);
  k = 0;
  l = 1;
  prev_l = 1;

  while l > 0:
    k = i // j;
    prev_l = l;
    l = i - k * j;
    # print("%d = %d * %d + %d" % (i, j, k, l));
    i = j;
    j = l;

  return prev_l;

def phi(n):
  ret = [];
  for i in range(1, n):
    if ggT(i, n) == 1:
      ret.append(i);
  return ret;
  
print(phi(9));
