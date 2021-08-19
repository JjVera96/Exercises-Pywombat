class PyWombatError(BaseException):
    pass

def custome_decorator(function):

    def wrapper(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception:
            raise PyWombatError('A PyWombat Error ocurred') from None

    return wrapper

@custome_decorator
def div(x, y):
    return x/y

div(10,0)
