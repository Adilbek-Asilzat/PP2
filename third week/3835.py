min = 1000

a = list(input().split())

for i in range(len(a)):

    b = int(a[i])

    if b < min and b > 0:

        min = b

print(min)