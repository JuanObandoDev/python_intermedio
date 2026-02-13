class DivisionError(Exception):
    """Excepción personalizada para errores de división."""

    pass


a = 0
b = 0
result = None

try:
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese otro número: "))
    if b == 2:
        raise DivisionError("Error personalizado: No se permiten divisiones por 2.")
    result = a / b
    print(f"El resultado de {a} dividido por {b} es: {result}")
except ValueError:
    print("Error: Debe ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally:
    print("Operación finalizada.")

print("Continuando con el resto del programa...")
