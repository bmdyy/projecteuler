import math

def num_divisors(n):
  r = [1];
  for i in range(2, int(math.sqrt(n)) + 1): # sqrt * sqtr = n
    if n % i == 0:
      r.append(i);
  # every divisor is paired (except for perfect squares)
  if math.sqrt(n) % 1 == 0:
    return len(r) * 2 - 1;
  elif n == 1:
    return 1;
  else:
    return len(r) * 2;

t = 1;
l = 2;
while True:
  if (num_divisors(t) > 500):
    print(t);
    quit();
  t += l;
  l += 1;
