def outer():
    def inner():
        print('This is returning function.')


    print('This is outter function invoking inner function.')
    return inner
