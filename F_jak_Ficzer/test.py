from functools import wraps
diss = {'olek': 'czubiak'}
# for x,y in diss.keys():
#     print(x + ' ' + y)
cookie_list = ['olek', 'bolek', 'wpierdolek']

# def auth(cookie: str):
#     def decorator(to_be_decorated):
#         if cookie in cookie_list:
#             x = f'Zautoryzowałem cookie: {cookie}'
#             print(x)
#             return x
#     return decorator

# auth('olek')
# def gra_myzuka():
#     print("DicoPolo")




def auth(cookie: str):
    def przodownik(to_be_decorated):
        @wraps(to_be_decorated)
        def inner(*args, **kwargs):
            if to_be_decorated in cookie_list:
                print('auth')
                return to_be_decorated(*args, **kwargs)
            else: 
                print('no auth')
                return to_be_decorated(*args, **kwargs)
        return inner
    return przodownik

@auth
def play(music):
    print(f'Gra: {music}')

play('olek')
print(play.__name__)