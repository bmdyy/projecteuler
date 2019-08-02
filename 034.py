import math;

def f(n):
  ret = 0;
  while n > 0:
    ret += math.factorial(n % 10);
    n //= 10;
  return ret;

t = 0;

for i in range(10, 1000000):
  f_i = f(i);
  if i == f_i:
    t += i;
    print(i);

print('total: %d' % t);
