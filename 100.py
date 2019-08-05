#https://www.alpertron.com.ar/QUAD.HTM
# b = num blue
# n = num blue + red
# b/n * b-1/n-1 = 1/2
# b^2-b / n^2-n = 1/2
# 2b^2-2b = n^2-n
# 2b^2 - 2b - n^2 + n = 0

b = 15;
n = 21;
while b + n <= 10**12:
  b_ = b;
  b = 3*b + 2*n - 2;
  n = 4*b_ + 3*n - 3;
print(b);
