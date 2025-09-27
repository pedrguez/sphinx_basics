def divide_nums(*args):
    """
    Divide un número variable de argumentos.

    Toma el primer argumento y lo divide por los argumentos siguientes.

    :param args: Número indefinido de argumentos.
    :type args: int or float
    :returns: El resultado de la división de los argumentos.
    :rtype: float

    :Ejemplo:
    >>> divide_nums(100, 5, 2)
    10.0
    
    """
    result = args[0]
    for num in args[1:]:
        result /= num
    return result

answer = divide_nums(100, 5, 2)
print(answer)
