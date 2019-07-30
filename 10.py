import math

p = [2,3]
s = 5;
v = 5;

def isPrime(n):
  u = math.sqrt(n);
  for i in p:
    if n % i == 0:
      return False;
    if i > u:
      break;
  return True;

while v < 2000000:
  if isPrime(v):
    s += v;
    p.append(v);
  v += 2;
print(s);
