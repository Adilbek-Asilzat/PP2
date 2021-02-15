a = list(input().split())

b = 0

for i in range(len(a)): 
    if a[i] != '0':
        print(a[i])
        
        b = b + 1

for i in range(len(a)-b):
    print(0)