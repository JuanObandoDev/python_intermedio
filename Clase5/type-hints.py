"""Typing con Python - Type hints with Python."""

var = 42  # int
print(f"Variable: {var}, Tipo: {type(var)}")

var = "Hola, mundo!"  # str
print(f"Variable: {var}, Tipo: {type(var)}")


# Var: type = value
other_var: int = 42
print(f"Variable: {other_var}, Tipo: {type(other_var)}")

other_var = "Hola, mundo!"  # str

user_id: int | None = None
