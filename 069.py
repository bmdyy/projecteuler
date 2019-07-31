def phi(n):
  ret = n;
  i = 2;
  while i * i <= n:
    if n % i == 0:
      while n % i == 0:
        n /= i;
      ret = ret - ret / i;
    i = i + 1;
  if n > 1:
    ret = ret - ret / n;
  return ret;

max_phi = 0;
max_phi_n = 0;
for n in range(0, 1000000, 210): # 0, 1000 gave 210 so i just put it there and it worked lol
  curr_phi = phi(n);
  if curr_phi == 0:
    continue;
  curr_phi = n / curr_phi;
  if curr_phi > max_phi:
    max_phi = curr_phi;
    max_phi_n = n;
print(max_phi_n);
