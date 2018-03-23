#!/usr/bin/env python3
'''A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(word):
    for idx in range(len(word)//2):
        if word[idx] != word[-idx-1]:
            return False
    return True


a = 100
b = 100
largest_palindrome = 0

for a in range(100, 999):
    for b in range(100, 999):
        x = a * b
        print(x)
        if is_palindrome(str(x)):
            largest_palindrome = max(x, largest_palindrome)

print(largest_palindrome)
