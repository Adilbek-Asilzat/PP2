   
print("gain: ")

arr = []

arr.append(input())

ans = []

ans.append(0)

for i in range(0,len(arr)):

            tmp=ans[i]+arr[i]

            ans.append(tmp)
            
print(max(ans))