def d(n):
  ret = 1;
  for i in range(2, n // 2 + 1):
    if n % i == 0:
      ret += i;
  return ret;

def is_amicable(n):
  partner = d(n);
  return [n == d(partner), partner];

t = 0;
a = [];

for i in range(2, 10000):
  if not (i in a):
    i_a = is_amicable(i);
    if i_a[0] and i != i_a[1]:
      t += i + i_a[1];
      a.append(i);
      a.append(i_a[1]);
      
print(t);
