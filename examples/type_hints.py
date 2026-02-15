"""Explicaciones y ejemplos de type hints en Python. - Explanations and examples of type hints in Python."""

from typing import Any

# Var = value
var: int | str = 42  # int
print(f"Variable: {var}, Tipo: {type(var)}")

var = "Hola, mundo!"  # str
print(f"Variable: {var}, Tipo: {type(var)}")


# Var: type = value
other_var: int | str = 42
print(f"Variable: {other_var}, Tipo: {type(other_var)}")

other_var = "Hola, mundo!"  # str

user_id: int | None = None


def addition(a: int, b: int) -> int:
    """Suma dos números enteros. - Adds two integers."""
    return a + b


articles: list[dict[str, str]] = [
    {
        "title": "Python 3.10 lanzado",
        "content": "Python 3.10 trae nuevas características...",
    },
    {
        "title": "PEP 8 actualizado",
        "content": "PEP 8 ahora incluye nuevas recomendaciones...",
    },
]


def process_data(data: Any) -> None:
    """Procesa datos de cualquier tipo. - Processes data of any type."""
    print(f"Procesando datos: {data}, Tipo: {type(data)}")
