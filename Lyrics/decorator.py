def world(func):
    print('world')
    return func


@world
def hello():
    print('hello')


hello()
