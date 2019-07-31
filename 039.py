import math

def how_many_sol_for(p):
  num_sol = 0;
  sols = [];
  for a in range(1, p):
    for b in range(1, p-a):
      c = math.sqrt(a*a + b*b);
      if a + b + c == p and not a in sols and not b in sols:
        num_sol += 1;
        sols.append(a);
        sols.append(b);
  return num_sol;

best = -1;
best_p = -1;
for p in range(1001):
  curr = how_many_sol_for(p);
  if curr > best:
    best = curr;
    best_p = p;
print(best_p);
