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

def get_refl_angle(m1, m2): # i think this is correct
  return abs((m2-m1)/(1 + m2 * m1));

def get_refl_m(m1, m2): # this might be wrong
  return math.tan(get_refl_angle(m1, m2));

def on_line(x0, y0, m1, b1):
  # check if the solution makes sense
  return y0 == m1 * x0 + b1;

def dist_2d(x0, y0, x1, y1):
  return math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2);

def oval_fx(x, m_, b_):
  y0 = math.sqrt(100 - 4 * (x ** 2));
  y1 = -y0;

  if on_line(x, y0, m_, b_):
    return y0;
  else:
    return y1;

def exits_oval(x, y):
  return -0.01 <= x and x <= 0.01 and y > 0;

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
  sol_0 = [i_x[0], oval_fx(i_x[0], m, b)];
  sol_1 = [i_x[1], oval_fx(i_x[1], m, b)];

  # we want the further solution
  if dist_2d(x, y, sol_0[0], sol_0[1]) > dist_2d(x, y, sol_1[0], sol_1[1]):
    return sol_0;
  else:
    return sol_1;

bounces = 0;
for i in range(4):
  next_int = next_intersection(c_x, c_y, c_m);
  c_x = next_int[0];
  c_y = next_int[1];
  c_m = get_refl_m(c_m, get_tangent_m(c_x, c_y)); # this might be incorrrect

  print(round(c_x, 2),'\t',round(c_y, 2),'\t',round(c_m, 2),'\t',bounces);

  if exits_oval(c_x, c_y):
    break;

  bounces += 1;
print(bounces);
