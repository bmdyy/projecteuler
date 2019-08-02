import math;

# start parameters for the laser:
# x, y, delta y, delta x (for slope)
c_x = 0;
c_y = 10.1;
c_m = (c_y + 9.6) / (c_x - 1.4);

def qdr_eq(a, b, c):
  # quadratic equation
  s1 = (-b + math.sqrt((b * b) - 4 * a * c)) / (2 * a);
  s2 = (-b - math.sqrt((b * b) - 4 * a * c)) / (2 * a);
  return [s1, s2];

def find_b(x, y, m):
  # y = mx + b;
  # we have y, m, x 
  # b = y - mx
  return y - m * x;

def oval_fx(x):
  # 4x^2 + y^2 = 100
  # we are given x 
  # sqrt(4x^2 - 100) = y
  return math.sqrt(4 * (x ** 2) - 100);

def next_intersection(x, y, m):
  # our oval is defined as 4x^2 + y^2 = 100
  # ...
  # sub y = mx + b into oval equation
  # 4x^2 + (mx + b)^2 = 100
  # 4x^2 + (m^2x^2 + 2bmx + b^2) = 100
  # 4x^2 + (m^2x^2 + 2bmx + b^2) - 100 = 0
  # (4 + m^2)x^2 + 2bmx + (b^2 - 100) = 0
  # ...
  # quadratic equation with qdr_a/b/c:
  # qdr_a = 4 + m^2
  # qdr_b = 2bm
  # qdr_c = b^2 - 100

  b = find_b(x, y, m);

  qdr_a = 4 + m ** 2;
  qdr_b = 2 * b * m;
  qdr_c = b ** 2 - 100;

  i_x = qdr_eq(qdr_a, qdr_b, qdr_c);
  sol = [[i_x[0], oval_fx(i_x[0])], [i_x[1], oval_fx(i_x[1])]];

  return sol;

print(next_intersection(c_x, c_y, c_m));
