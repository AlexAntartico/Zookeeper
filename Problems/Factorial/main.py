factorial = int(input())
num = 1

while factorial > 1:
    num *= factorial
    factorial -= 1

print(num)