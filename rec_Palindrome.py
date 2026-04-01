a = input()

l, r = 0, len(a)-1

# def Palindrome(a,l,r):
#     if l < r:
#         if a[l] == a[r]:
#             return Palindrome(a, l+1, r-1)
#         else:
#             print("Not a Palindrome")
#     else:
#         print("Palindrome")
    
# Palindrome(a,l,r)

def is_Palindrome(a,l,r):
    if l >= r:
        return True
    if a[l] != a[r]:
        return False
    return is_Palindrome(a,l+1,r-1)

print("Palindrome" if is_Palindrome(a,l,r) else "Not a Palindrome")