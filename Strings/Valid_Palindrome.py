# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

raw_string = input()

def function(raw_string):
    result = "".join(char.lower() for char in raw_string if char.isalnum())
    return result == result[::-1]

print(function(raw_string))