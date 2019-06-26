def rectangle(a, b):
    check(rectangle())
    return a * b


def triangle(a, h):
    check(triangle())
    return 0.5 * a * h


def trapez(a, b, h):
    check(trapez())
    return 0.5 * (a + b) * h


def check(*values):
    for i in values:
        if not(isinstance(i, (int, float))):
            print('ok')
        else:
            raise ValueError('not ok', i, 'not int or float')
