import math

def get_c(a,b):
  s = a**2 + b**2;
  q = math.sqrt(s);
  if q % 1 == 0:
    return int(q);
  return -1;

for a in range(1, 500):
  for b in range(1, 500):
    c = get_c(a,b);
    if c > 0:
      if a+b+c == 1000:
        print(a*b*c);
        quit();
