def is_prime(n):
  if n <= 3:
    return n > 1;
  elif n % 2 == 0 or n % 3 == 0:
    return False;
  
  i = 5;
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False;
    i = i + 6;
  return True;

def num_con_primes(a, b):
  n = 0;
  while is_prime(n*n+a*n+b):
    n += 1;
  return n;

best_coeffs = [-1001, -1001];
best_num_con_primes = 0;

for a in range(-1000, 1000): # |a| < 1000
  for b in range(-1000, 1001): # |b| <= 1000
    curr_num_con_primes = num_con_primes(a, b);
    if curr_num_con_primes > best_num_con_primes:
      best_num_con_primes = curr_num_con_primes;
      best_coeffs = [a, b];

print(best_coeffs, best_coeffs[0] * best_coeffs[1]);
