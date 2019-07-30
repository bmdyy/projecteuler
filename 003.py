n = 600851475143;
f = []

while (n != 1):
  i = 2;
  while (n % i != 0):
    i += 1;
  f.append(i);
  n /= i;
print(f[-1]);
