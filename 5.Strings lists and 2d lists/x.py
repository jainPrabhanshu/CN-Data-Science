r = [11, 12, 13, 14]
A = [[0, 10, 20],
     [30, 40, 50],
     [60, 70, 80]]
for row in A:
    for col in row:
        r.append(col+10)
print(r)