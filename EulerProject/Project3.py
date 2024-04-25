# The prime factors of 132195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?
list = []
for prime in range(3, int(600851475143 ** 0.5) + 1, 2):
    if 600851475143 % prime == 0:
        list.append(prime)

print(list)
# Result = 6857
