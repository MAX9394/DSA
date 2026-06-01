n = int(input())
x = abs(n)

digits = len(str(x))
total = 0
temp = x

while temp:
    total += (temp % 10) ** digits
    temp //= 10

print("Armstrong Number" if total == x else "Not an Armstrong Number")