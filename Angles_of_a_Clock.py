def calcAngle(h, m):
    degree = abs((abs(h-m/5)*30-m/2))
    return int(degree)


print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165
