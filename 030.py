def f(n, p):
  t = 0;
  n_ = n;
  while n_ > 0:
    t += (n_ % 10) ** p;
    n_ //= 10;
  return t == n;

t = 0;
for i in range(2, 1000000):
  if f(i, 5):
    t += i;
print(t);
