"""
Explicacion de docstrings en Python. - Explanation of docstrings in Python.

En esta clase puedo explicar como funcionan los docstrings en python - In this class I can explain how docstrings work in Python.
"""


def example_without_docstring(a, b):
    return a + b


def example_with_docstring(a, b):
    """
    Esta funcion devuelve la suma de dos numeros. - This function returns the sum of two numbers.

    returns:
        int: La suma de a y b. - The sum of a and b.
    """
    return a + b


print(
    example_with_docstring.__doc__
)  # Imprime el docstring de la función - Prints the function's docstring


def anatomy_of_docstring():
    """
    Descripcion - Description: Explica el propósito de la función o clase. - Explains the purpose of the function or class.
    Args - Arguments: Detalla los parámetros de entrada, su tipo y su propósito. - Details the input parameters, their type, and their purpose.
    Returns: Describe el valor de retorno, su tipo y su significado. - Describes the return value, its type, and its meaning.
    Exceptions: Enumera las excepciones que la función puede lanzar. - Lists the exceptions that the function can raise.
    Examples: Proporciona ejemplos de uso de la función. - Provides examples of how to use the function.
    """
    pass
