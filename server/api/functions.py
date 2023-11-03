def sum_of_squares(number):
    """Given a number n, return the sum of the squares of the first n natural numbers"""
    return sum([i**2 for i in range(number + 1)])


def square_of_sums(number):
    """Given a number n, return the square of the sum of the first n natural numbers"""
    return sum([i for i in range(number + 1)]) ** 2


def is_pythagorean_triplet(a, b, c):
    """Given a sequence of three numbers, return whether they together make a Pythagorean triplet"""
    return a**2 + b**2 == c**2


def product_of_three(a, b, c):
    """Given three numbers, return their product"""
    return a*b*c
