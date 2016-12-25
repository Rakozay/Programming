# What is the value of a? = 110
# 1 11      (1)
# 12 22     (2)
# 23 33     (3)
# 34 44     (4)
# 45 55     (5)
# 56 66     (6)
# 67 77     (7)
# 78 88     (8)
# 89 99     (9)
# 100 110   (10)

a = 0
for i in range(10):
    a += 1
    for j in range(10):
        a += 1
print(a)