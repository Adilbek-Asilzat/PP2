print("n = ")

a = int(input())

product = 1

sum = 0

while a != 0:

    product *= (a%10)
    
    sum += (a%10)
    
    a /= 10

print(product - sum)