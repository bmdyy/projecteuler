def is_leap_year(y):
    if y % 100 == 0:
        return y % 400 == 0;
    else:
        return y % 4 == 0;

def what_day_of_week_was(d, m, y):
    # 1 Jan 1900 was a Monday.
    d_ = 1;
    m_ = 1;
    y_ = 1900;
    w_ = 0; # 0 = monday
    while not (d_ == d and m_ == m and y_ == y):
        d_ += 1;
        w_ += 1;

        if w_ > 6:
            w_ = 0;
        
        inc_month = False;
        if m_ in [4, 6, 9, 11] and d_ > 30: # apr, jun, sep, nov
            inc_month = True;
        elif m_ == 2: # february (28 or 29)
            if is_leap_year(y_):
                if d_ > 29: # leap year
                    inc_month = True;
            else:
                if d_ > 28:
                    inc_month = True;
        elif d_ > 31: # long months 
            inc_month = True;

        if inc_month == True:
            d_ = 1;
            m_ += 1;

            if m_ > 12:
                m_ = 1;
                y_ += 1;

    return w_;

total_sundays = 0;
for y in range(1901, 2001):
    for m in range(1, 13):
        if what_day_of_week_was(1, m, y) == 6:
            total_sundays += 1;
print(total_sundays);
            
