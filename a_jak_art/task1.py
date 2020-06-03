def wraps(sentenced):
    def wrapper(to_be_decorated):
        def inner(*args,**kwargs):
            inner.__doc__ = to_be_decorated.__doc__
            inner.__name__ = to_be_decorated.__name__
            inner.__qualname__= to_be_decorated.__qualname__
            inner.__annotations__ = to_be_decorated.__annotations__
            return to_be_decorated
        return inner
    if callable(sentenced):
        return wrapper(sentenced)
    else:
        return wrapper

@wraps
def say_python():
    """jakis opis"""
    return "PYTHON"
