def goldbach(n):
  # 0 = writeable
  # 1 = prime 
  # 2 = square
  p = n;
  while p > 2:
    p = next_prime_below(p);
    t = n - p;
    if t % 2 != 0:
      continue;
    t /= 2;
    t **= 0.5;
    if t % 1 == 0:
      return [True, p, t];
  return [False, -1, -1];

def is_composite(n): 
    if (n <= 1): 
      return False;
    if (n <= 3): 
      return False;
    if (n % 2 == 0 or n % 3 == 0): 
      return True;
    i = 5;
    while(i * i <= n): 
      if (n % i == 0 or n % (i + 2) == 0): 
          return True;
      i = i + 6;   
    return False;

def is_prime(n):
  if n <= 3:
    return n > 1;
  elif n % 2 == 0 or n % 3 == 0:
    return False;
  i = 5;
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False;
    i += 6;
  return True;

def next_prime_below(p):
  p -= 1;
  while not is_prime(p):
    p -= 1;
  return p;

i = -1;
while True:
  i += 2;
  if not is_composite(i):
    continue;
  if goldbach(i)[0] == False:
    print(i);
    break;
