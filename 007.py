import math

p = [2, 3];
c = p[-1];

def isPrime(n):
  u = math.sqrt(n);
  for i in p:
    if n % i == 0:
      return False;
    if i > u:
      break;
  return True;

while len(p) < 10001:
  c += 2;
  if isPrime(c):
    p.append(c);

print(p[-1]);
