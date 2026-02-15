numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = []

for num in numbers:
    if num % 2 == 0:
        pairs.append(num)

print(numbers)
print(pairs)


def is_pair(num):
    """Determina si un número es par. - Determines if a number is even."""
    return num % 2 == 0


pairs_filter = list(
    filter(
        is_pair, numbers
    )  # Devuelve un iterador con los números pares - Returns an iterator with the even numbers
)
print(pairs_filter)
