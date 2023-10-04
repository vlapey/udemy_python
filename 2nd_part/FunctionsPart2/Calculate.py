def if_calculate(**kwargs):
    result = 0
    if "operation" in kwargs:
        if kwargs["operation"] == "add":
            result = kwargs["first"] + kwargs["second"]
        elif kwargs["operation"] == "subtract":
            result = kwargs["first"] - kwargs["second"]
        elif kwargs["operation"] == "multiply":
            result = kwargs["first"] * kwargs["second"]
        elif kwargs["operation"] == "divide":
            result = kwargs["first"] / kwargs["second"]

    if "make_float" in kwargs:
        if not kwargs["make_float"]:
            result = int(result)

    if "message" in kwargs:
        return f"{kwargs['message']} {result}"

    return f"The result is {result}"


print(if_calculate(make_float=True, operation='divide', first=3.5, second=3))


def calculate(**kwargs):

    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 1),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }

    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        result = f"{kwargs.get('message', 'The result is')} {float(operation_value)}"
    else:
        result = f"{kwargs.get('message', 'The result is')} {int(operation_value)}"
    return result
