def validate_transaction(function):

    def wrapper(*args, **kwargs):
        for arg in args:
            if not arg:
                return print("No es posible completar la operación")
                break
        else:
            result = function(*args, **kwargs)
            return print(result)

    return wrapper

@validate_transaction
def deposit(amount, balance):
    return amount + balance

@validate_transaction
def withdraw(amount, balance):
    return balance - amount

deposit(10, 100)
deposit(0, 100)
withdraw(0, 100)
withdraw(10, 100)
