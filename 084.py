from random import randint;
from random import shuffle;

GO = 0;
JAIL = 10;
CH = [7, 22, 36];
CC = [2, 17, 33];
G2J = 30;

curr_square = GO;

CH_DECK = [None] * 16;
CH_DECK[0] = GO;
CH_DECK[1] = JAIL;
CH_DECK[2] = 11; # c1
CH_DECK[3] = 24; # e3
CH_DECK[4] = 39; # h2
CH_DECK[5] = 5; # r1
CH_DECK[6] = 111; # next R
CH_DECK[7] = 111;
CH_DECK[8] = 222; # next u
CH_DECK[9] = -3;

CC_DECK = [None] * 16;
CC_DECK[0] = GO;
CC_DECK[1] = JAIL;

shuffle(CH_DECK);
shuffle(CC_DECK);

def draw_from(n):
  c = 0;
  if n == 0: # ch
    c = CH_DECK.pop(0);
    CH_DECK.append(c);
  else:
    c = CC_DECK.pop(0);
    CC_DECK.append(c);
  return c;

def roll():
  # 0 = TOTAL, 1 = DOUBLE
  d1 = randint(1, 4);
  d2 = randint(1, 4);
  return [d1 + d2, d1 == d2];

def next_r(): # 5, 15, 25, 35
  if curr_square < 5 or curr_square >= 35:
    return 5;
  elif curr_square < 15:
    return 15;
  elif curr_square < 25:
    return 25;
  else:
    return 35;

def next_u(): # 12, 28
  if curr_square < 12 or curr_square >= 28:
    return 12;
  else:
    return 28;

def do_move(n): # n = num doubles
  global curr_square;
  
  if n == 3:
    curr_square = JAIL;
    return True;
  
  curr_roll = roll();
  curr_square += curr_roll[0];

  if curr_square >= 40:
    curr_square -= 40;

  if curr_square in CH:
    card = draw_from(0);
    if card != None and card >= 0 and card < 40:
      curr_square = card;
    else:
      if card == -3:
        curr_square -= 3;
      elif card == 111:
        curr_square = next_r();
      elif card == 222:
        curr_square = next_u();
  
  if curr_square in CC:
    card = draw_from(1);
    if card != None:
      curr_square = card;
  
  if curr_square == G2J:
    curr_square = JAIL;
    return True;

  if curr_roll[1] == True:
    do_move(n + 1);

S = [0] * 40;
T = 500000;

for move in range(T):
  do_move(0);
  S[curr_square] += 1;

r = [0] * 3;
for i in range(len(S)):
  if S[i] > S[r[0]]:
    r[0] = i;
  elif S[i] > S[r[1]]:
    r[1] = i;
  elif S[i] > S[r[2]]:
    r[2] = i;

print('%02d%02d%02d' % (r[0], r[1], r[2]));
