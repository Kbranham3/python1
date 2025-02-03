def power(base, exponent):
    # Handling negative exponents by computing the reciprocal
    if exponent < 0:
        return 1 / power(base, -exponent)

    # Base case: any number raised to the power of 0 is 1
    if exponent == 0:
        return 1

    # Efficient exponentiation using recursion (Exponentiation by Squaring)
    if exponent % 2 == 0:
        half_power = power(base, exponent // 2)
        return half_power * half_power
    else:
        return base * power(base, exponent - 1)


# Example usage
print(power(2, 3))  # Output: 8
print(power(5, -2))  # Output: 0.04
print(power(3, 0))  # Output: 1
print(power(2, -3))  # Output: 0.125
