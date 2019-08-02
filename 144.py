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

def get_tangent_m(x, y):
  return -4 * x / y;

def get_refl_angle(m1, m2):
  return math.pi - math.atan(abs( (m1 - m2)/(1 + m1 + m2) ));

def get_refl_m(m1, m2):
  return math.tan(get_refl_angle(m1, m2));

def oval_fx(x):
  return -math.sqrt(100 - 4 * (x ** 2));

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
  sol_0 = [i_x[0], oval_fx(i_x[0])];
  sol_1 = [i_x[1], oval_fx(i_x[1])];

  print(sol_0);
  print(sol_1);

  return sol_1;

next_int = next_intersection(c_x, c_y, c_m);
c_x = next_int[0];
c_y = next_int[1];
c_m = get_refl_m(c_m, get_tangent_m(c_x, c_y));
#print(c_x,'\t',c_y,'\t',c_m);
