# Create the logging_decorator() function 👇


def add_decorator(function):
    def wrapper(*args, **kwargs):
        texto = f"You called {function.__name__}("
        texto = texto + str(args[0])
        for numero in args[1:]:
            texto += f", {numero}"
        texto += ")\n"
        texto += "It returned: "+str(function(*args))

        print(texto)
        function(*args)
    return wrapper


@add_decorator
def a_function(*args, **kwargs):
    soma = 0
    for numero in args:
        soma += numero
    return soma

# Use the decorator 👇


a_function(1, 2, 3)
