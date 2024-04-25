# Using Fibonacci sequence, find the sum of all even values that are less than 4000000
r = 1
x = 2
z = 0
while True:
    x += r
    r = x - r
    if x % 2 == 0: z += x
    if x >= 4000000: break

print(f"The answer of question 2 is {z + 2}")
# The cycle was not counting the beggining value of x, 2.
