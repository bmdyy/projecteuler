raw = """...""";
T = [];
for r in raw.split("\n"):
  t = r.split(" ");
  t_ = [];
  for t__ in t:
    t_.append(int(t__));
  T.append(t_);

i = len(T) - 2;
while i >= 0:
  j = 0;
  while j < len(T[i]):
    T[i][j] += max(T[i+1][j], T[i+1][j+1]);
    j += 1;
  i -= 1;

print(T[0][0]);
