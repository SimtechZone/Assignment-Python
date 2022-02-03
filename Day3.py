s = "welcome"
d = {}

for i in s:
    d[i] = d.get(i, 0) + 1
    print(d)

x = list(d.values())
y = list(d.keys())
print(y[x.index(max(x))])
