n = int(input())

if n == 0:
    print(0)
else:
    x = abs(n)
    divisors = []

    for i in range(1,(x//2)+1):
        if n % i == 0:
            divisors.append(str(i))

    print(','.join(divisors))