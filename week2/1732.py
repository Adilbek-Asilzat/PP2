print("gain: ")

arr = []

arr.append(input())

list = []

list.append(0)

for i in range(0,len(arr)):

    sum = list[i] + arr[i]

    list.append(sum)



print(max(list))
