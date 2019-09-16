# 16 sept 2019 collatz.py

# n is the number we will perform Collatz on.
n = 20

# Keep looping until n = 1.
# Note: Assumes Collatz conjecture is true.
while n != 1:
# Print the current value of n.
    print(n)
    # Check if n is even.
    if n % 2 == 0:
        # If n is even, divide n by 2.
        n = n / 2
    else:
        # If n is odd, multiply n by 3 and add 1.
        n = (3 * n) + 1
# Finally, print the current value of n.
print(n)
