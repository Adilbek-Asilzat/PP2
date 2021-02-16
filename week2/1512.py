print("nums: ")

arr = input().split()

count = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] == arr[j] and i < j:
            count += 1

print( count )