"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

n = 1
list = []
for x in range(101, 999):
    for y in range(101, 999):
        n = x * y
        if n % 10 == n // 10000 or n % 10 == n // 100000:
            list.append(n)
list.sort()
print(list)

"""Shows all the numbers that begins and finishes with the same number, need a better solve"""
