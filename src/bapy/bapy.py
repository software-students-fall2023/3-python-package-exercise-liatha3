def add_one(number):
    return number + 1

def fooloo(n, i, operation):
    # check if operation is a lambda function
    if callable(operation) and operation.__name__ == '<lambda>':
        # iteration from start i to end n
        while i <= n:
            # execute the operation function, passing through i and increment at the end of function call
            operation(i)
            i += 1
    # if operation is not a lambda function, print it must be a lambda function
    else:
        print("The 'operation' argument must be a lambda function")

def fuh(condition, if_true, if_false):
    """
    If Statement for babies.
    
    :param condition: Boolean condition to evaluate.
    :param if_true: Callable to execute if the condition is True.
    :param if_false: Callable to execute if the condition is False.
    :return: The result of either the if_true or if_false callable.
    """
    
    if callable(if_true) and callable(if_false):
        return if_true() if condition else if_false()
    else:
        raise ValueError("Both if_true and if_false must be callable.")
