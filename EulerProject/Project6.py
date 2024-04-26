"""The sum of the squares of the first ten natural numbers is,
  1² + 2² + ... 10² = 385

The square of the sum of the first ten natural numbers is,
  (1 + 2 + ... + 10)² = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
s = 0
for n in range(1, 101):
    s += n ** 2

p = 0

for v in range(1, 101):
    p += v

r = (p**2) - s

print(r)
