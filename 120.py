def r(a, n):
  return ((a-1)**n + (a+1)**n) % a**2;

def r_max(a):
  ret = 0;
  for n in range(1, a, 2):
    # even numbers always 2
    # pattern repeats after max a digits
    r_ = r(a, n);
    if r_ > ret:
      ret = r_;
  return ret;

t = 0;
for a in range(3, 1001):
  t += r_max(a);
print(t);
