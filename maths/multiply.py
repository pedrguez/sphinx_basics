def multiply_nums(*args):
    """ 
    Multiplica un número variable de argumentos.

    Toma el primer argumento y lo multiplica por los argumentos siguientes.

    :param args: Número indefinido de argumentos.
    :type args: int or float
    :returns: El resultado de la multiplicación de los argumentos.
    :rtype: float

    :Ejemplo:
    >>> multiply_nums(100, 5, 2)
    10.0
    
    """
    result = args[0]
    for num in args[1:]:
        result *= num
    return result
answer = multiply_nums(2, 3, 5)
print(answer)