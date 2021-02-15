a = int(input())

d = {}

for i in range(a):

    first, second = input().split()

    d[first] = second

    d[second] = first

print(d[input()])