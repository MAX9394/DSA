n = int(input())

# while n != 0:
#     r = n % 10
#     print(r, end = "")
#     n = n // 10
sign = '-' if n < 0 else ''
n = abs(n)

if n == 0:
    print(0)
else:
    result = []
    while n != 0:
        result.append(str(n % 10))
        n = n // 10
    
    print(sign + ''.join(result))