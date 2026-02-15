"""Ejemplos y explicaciones de f-strings en Python. - Examples and explanations of f-strings in Python."""

from datetime import datetime

name = "Ana"
born_year = 1990
text = f"Hola, {name}!"
print(text)

text_format = "Hola, {}!".format(name)
print(text_format)

text_suma = f"El resultado de 2 + 2 es {2 + 2}."
print(text_suma)

text_calc = f"Hola, {name}. Tu edad es: {2026 - born_year} años."
print(text_calc)


text_func = f"HOLA {name.upper()}!"
print(text_func)

edad = 30
text_if = f"Hola {name}, tienes {'más de 30 años' if edad > 30 else '30 años o menos'}."
print(text_if)

bank_balance = 1200000000
text = f"Tu saldo bancario es: {bank_balance:,}."
print(text)

stock_price = 1.405
text_stock = f"El valor del stock es: {stock_price:.1f}."
print(text_stock)

user_id = 1
text_id = f"El ID del usuario es: {user_id:04d}."
print(text_id)

product = "laptop"
price = 1000
text_product = f"Producto {product:>10} | Precio: ${price:.2f}"
print(text_product)


date = datetime(2026, 12, 5, 10, 10)
text = f"La fecha completa es: {date: %A %d de %B de %Y a las %I:%M %p}."
print(text)

# Formatear porcentajes y numeros en notación científica - Format percentages and numbers in scientific notation
percentage = 0.1234
text_percentage = f"El porcentaje es: {percentage:.2%}."
print(text_percentage)

number = 123456789
text_scientific = f"El número en notación científica es: {number:.2e}."
print(text_scientific)
