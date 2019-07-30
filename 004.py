def isPalindrome(n):
  return n == int(str(n)[::-1]);

l = 0;
i = 999;
while ( i >= 100 ):
  j = 999;
  while ( j >= 100 ):
    p = i * j;
    if isPalindrome(p) and p > l:
      l = p;
    j -= 1;
  i -= 1;
print(l);
