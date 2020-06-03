def is_correct(f,*args):
    def wrapper(f):
        def inner():
            f.value = 0
            for element in args:
                if element in f():
                    f.value += 1
            if f.value==len(args):
                    return f()
            else:
                    return None
        return inner
    return wrapper

@is_correct('first_name','last_name')
def get_data():
    return {
        'first_name': 'Jan',
        'last_name': 'Kowalski',
        'email': 'jan@kowalski.com'
    }

@is_correct('first_name', 'last_name', 'email')
def get_other_data():
    return {
        'first_name': 'Jan',
        'email': 'jan@kowalski.com'
    }


assert get_other_data() is None

assert get_data() == {
        'first_name': 'Jan',
        'last_name': 'Kowalski',
        'email': 'jan@kowalski.com'
    }