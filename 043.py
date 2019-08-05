from itertools import permutations;

def passed_test(p):
  if int(p[1:4])%2!=0:
    return False;
  if int(p[2:5])%3!=0:
    return False;
  if int(p[3:6])%5!=0:
    return False;
  if int(p[4:7])%7!=0:
    return False;
  if int(p[5:8])%11!=0:
    return False;
  if int(p[6:9])%13!=0:
    return False;
  if int(p[7:])%17!=0:
    return False;
  return True;

P = [''.join(p) for p in permutations('0123456789')]
total = 0;

for p in P:
  if p[0] == 0:
    continue;
  if not passed_test(p):
    continue;
  total += int(p);

print(total);
