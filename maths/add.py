def add_nums(*args):
    """
    Suma un número variable de argumentos

        :param args: Número indefinido de argumentos
        :type args: enteros o flotantes
        :returns: La suma de los argumentos
        :rtype: enteros o flotantes
    
    :Ejemplo:
    >>> add_nums(2,3,5)
    10
    """
    result = sum(args)
    return result
answer = add_nums(2,3,5)
print(answer)
