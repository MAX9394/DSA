n = int(input())

# n = abs(n)

# if str(n) == str(n)[::-1]:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")

n = str(abs(n))

print("Palindrome Number" if n == n[::-1] else "Not a Palindrome Number")