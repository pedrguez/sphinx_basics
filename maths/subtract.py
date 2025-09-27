def subtract_nums(*args):
    """
    Este método será usado para restar números indefinidos

        :param args: Numero indefinido de argumentos
        :type args: enteros o flotantes
        :returns: la resta de los argumentos
        :rtype: enteros o flotantes
        
    :Ejemplo:
    >>> substract(100, 20, 30, 40)
    10    
        
    """
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

answer = subtract_nums(100, 20, 30, 40)
print(answer)