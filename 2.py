a = 1;
b = 1;
sum = 0

while b < 4000000:
  if b % 2 == 0:
    sum += b;

  c = a;
  a = b;
  b += c;

print(sum);
