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
