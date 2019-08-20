u = 10000000; # 10 000 000
T = [-1] * u;

def f(n):
  # case 1: we already traced this number to either 1 or 89
  if T[n] != -1:
    return T[n];

  # case 2: we didnt trace this number yet 
  c = n;
  C = [n]; # numbers we will pass along the chain
  e = -1;

  while c != 1 and c != 89:
    m = c;
    t = 0;
    while m > 0:
      t += (m % 10) ** 2;
      m //= 10;
    c = t;
    C.append(c);
    e = c;
    if T[c] != -1:
      e = T[c];
      break;

  for i in C:
    T[i] = e;

  return e;

a = 0;
for i in range(1, u):
  if i % 1000000 == 0:
    print(i);
  if f(i) == 89:
    a += 1;
print(a);
