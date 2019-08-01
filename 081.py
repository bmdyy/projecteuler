f = open("p081_matrix.txt");
m = [];

for r in f:
    r_ = r.split(',');
    m_ = [];
    for c in r_:
        m_.append(int(c));
    m.append(m_);

len_m = len(m);

# bottom row + right column
n = len_m - 1;
while n > 0:
    m[len_m - 1][n - 1] += m[len_m - 1][n];
    m[n - 1][len_m - 1] += m[n][len_m - 1];
    n -= 1;

# the rest
y = len_m - 2;
while y >= 0:
    x = len_m - 2;
    while x >= 0:
        m[y][x] += min(m[y+1][x], m[y][x+1]);
        x -= 1;
    y -= 1;

print(m[0][0]);
