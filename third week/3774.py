n = int(input())
d = {}
a = {}
 
for i in range(n-1):
    a1, a2 = input().split()
    d[a1] = a2
    a[a1] = 0
    a[a2] = 0
    
for i in d:
    s = i
    while s in d:
        s = d[s]
        a[i] += 1
    
for i in sorted(a):
    print(i, a[i])