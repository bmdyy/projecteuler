def reverse_num(n):
  return int(str(n)[::-1]);

def is_palindrome(n):
  return n == reverse_num(n);

def is_lychrel(n, r):
  for i in range(r):
    n += reverse_num(n);
    if is_palindrome(n):
      return False;
  return True;

t = 0;
for i in range(0, 10000):
  if is_lychrel(i, 50):
    t += 1;
print(t);
