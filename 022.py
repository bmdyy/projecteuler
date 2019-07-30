names = open("p022_names.txt").readline().replace("\"", "").split(",");
names.sort();

def name_score(name, i):
    t = 0;
    for c in name:
        t += ord(c) - 64;
    return t * i;

total = 0;
for i in range(len(names)):
    total += name_score(names[i], i + 1);
print(total);
