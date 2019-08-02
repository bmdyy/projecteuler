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

def next_prime(p):
  p += 1;
  while not is_prime(p):
    p += 1;
  return p;

# phi = n * (1 - 1/p_0) * ... * (1 - 1/p_i);
# first we will find a lower bound aka
# a number that doesnt pass the target, but multiplied
# by the next prime does
# then we backpedal by 1 prime and do some brute forcing
# multipying by composite numbers

p = 2; # curr prime number
num = 1;
den = 1;
target = 15499/94744;

# (1 - 1/p) = ((p - 1) / p)

while True:
  num *= p - 1;
  den *= p;

  if num / den < target:
    for i in range(1, p):
      num_ = i * num;
      den_ = i * den;
      if num_/(den_-1) < target:
        print(den_);
        exit();

  p = next_prime(p);
