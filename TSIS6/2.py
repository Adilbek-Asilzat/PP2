def sum(numbers):
    total = 0
    for x in numbers:
        total += int(x)
    return total

input_string = input()

list  = input_string.split()

print(sum(list))