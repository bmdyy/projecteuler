n = '';
for i in range(1, 1000000):
  n += str(i);

p = 1;
for i in range(0, 7):
  p *= int(n[10 ** i - 1]);

print(p);
