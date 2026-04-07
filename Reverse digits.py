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

# Bit shift Method
# if x<=-(1<<31) or x>=(1<<31)-1:
#     return 0
            
# if x>0:
#     a=int(str(x)[::-1])
#     if  a>(1<<31)-1:
#         return 0
#     return a
# else:
#     a=-int(str(-x)[::-1])
#     if a<-(1<<31):
#         return 0
#     return a