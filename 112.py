def is_increasing_number(n):
  while n > 0:
    l = n % 10;
    n //= 10;
    c = n % 10;
    if c > l:
      return False;
  return True;

def is_decreasing_number(n):
  while n > 0:
    l = n % 10;
    n //= 10;
    c = n % 10;
    if c < l:
      if c == 0 and n == 0:
        continue;
      return False;
  return True;

def is_bouncy_number(n):
  return not is_increasing_number(n) and not is_decreasing_number(n);

num_bouncy = 0;
i = 100; # no bouncy below 100
while num_bouncy / i < 0.99:
  if is_bouncy_number(i):
    num_bouncy += 1;
  if num_bouncy / i > 0.98999:
    print(i, num_bouncy/ i);
  i += 1;
print(i);
