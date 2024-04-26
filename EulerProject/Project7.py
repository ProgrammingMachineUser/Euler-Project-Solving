"""7. By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""
def is_prime(n):
  """Efficient primality test using square root."""
  if n <= 1:
    return False
  # Check for divisibility by 2 separately
  if n % 2 == 0:
    return False
  # Optimized loop checks only odd divisors up to the square root of n
  for i in range(3, int(n**0.5) + 1, 2):
    if n % i == 0:
      return False
  return True

count_prime = 1
n = 2
while count_prime < 10001:
  if is_prime(n):
    count_prime += 1
  n += 1

print(n - 1)  # Because the loop increments n after the last prime is found
