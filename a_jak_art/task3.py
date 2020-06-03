import datetime  # do not change this import, use datetime.datetime.now() to get date


def add_date(format):
    def wrapper(fafafafafafaf):
        def inner(*args, **kwargs):
            date = dict(fafafafafafaf(*args,**kwargs))
            date['date']= datetime.datetime.now().strftime(format)
            return date
        return inner
    return wrapper

        


@add_date('%B %Y')
def get_data(a):
    return {1: a, 'name': 'Jan'}


assert get_data(2) == {
    1: 2, 'name': 'Jan', 'date': 'April 2020'
}