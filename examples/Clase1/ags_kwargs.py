"""Explicaciones y ejemplos de *args y **kwargs. - Explanations and examples of *args and **kwargs."""


def ejemplo_args(*args):
    """Ejemplo de función con argumentos variables. - Example of function with variable arguments."""
    print(f"TODOS {args}")


ejemplo_args(1, 2, 3, "cuatro", "cinco")
ejemplo_args("noticia1", "noticia2", "noticia3")
ejemplo_args()


def ejemplo_kwargs(**kwargs):
    """Ejemplo de función con argumentos keyword variables. - Example of function with variable keyword arguments."""
    print(f"kwargs type {type(kwargs)}")
    print(f"kwargs {kwargs}")


ejemplo_kwargs(api_key="1234567890abcdef", timeout=20, attempts=5)
ejemplo_kwargs(section="technology", from_date="2026-01-01")
ejemplo_kwargs()
