import math;
import time;

def fill_form(f, b):
  ret = '';
  b_ = str(b);
  b_len = len(b_);
  idx = 0;
  for i in range(len(f)):
    if f[i] != '_':
      ret += f[i];
    else:
      if idx >= b_len:
        ret += '0';
      else:
        ret += b_[idx];
      idx += 1;
  return int(ret);

start = time.time();
blanks = 0; # lim = 999 999 999
form = '38_318_9';

while blanks < 999999999:
  sqrt_ = math.sqrt(fill_form(form, blanks));
  if sqrt_ // 1 == sqrt_:
    break;
  blanks += 1;

print(fill_form(form, blanks));
print("ela %f seconds" % (time.time() - start));

# needs to go like this
# form has 9 blanks
# 000 000 001
# 000 000 002
# ...
# instead of going
# 100 000 000
# 200 000 000
# ...
