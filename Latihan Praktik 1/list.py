data = list((1, 2, 3, 4, 10))

print(data) # sebelum

data.append(7)
print(data) # sesudah append

data.sort()
print(data)

data[1] = 6
print(data)

data.sort()
print(data)

data.remove(7)
print(data)

for x in data:
    print(x)