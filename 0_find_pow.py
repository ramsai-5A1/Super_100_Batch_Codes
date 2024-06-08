# We can solve the below function in logarithmic time complexity, using even and odd number checking technique, explore that solution yourself.
def find_power(m, n):
    if n == 0:
        return 1 

    return m * find_power(m, n - 1)



print(find_power(2, 7))
