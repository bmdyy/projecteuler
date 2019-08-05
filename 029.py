def num_dist_terms(a, b):
  t = [];
  for a in range(2, a + 1):
    for b in range(2, b + 1):
      a_b = a ** b;
      if not a_b in t:
        t.append(a_b);
  return len(t);

print(num_dist_terms(100, 100));
