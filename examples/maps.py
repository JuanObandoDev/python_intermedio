numbers = [1, 2, 3, 4, 5]
squared_nums = []

for num in numbers:
    squared_nums.append(num**2)

print(numbers)
print(squared_nums)


def square_number(x):
    """Devuelve el cuadrado de un número. - Returns the square of a number."""
    return x**2


squared_nums_map = list(
    map(square_number, numbers)
)  # Devuelve un iterador con los números al cuadrado - Returns an iterator with the squared numbers
print(squared_nums_map)
