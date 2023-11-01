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

