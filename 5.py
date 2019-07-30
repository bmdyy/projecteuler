divisors = [11,12,13,14,15,16,17,18,19,20]; # can ignore 1-10
curr = divisors[-1];

while True:
  found = True
  for d in divisors:
    if curr % d != 0:
      found = False;
      break;

  if found:
    break;
  curr += divisors[-1];
print(curr);
