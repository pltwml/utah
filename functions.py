''' functions playground'''


def fib(n: int):
    """

    :rtype: None
    """
    a, b, c = 0, 1, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        c +=1
    print('\r')
    print('Fibonacci terms in the range: ', c)


print("Evaluating")
fib(2000)


def fib2(n: int):
    """

    :param n:
    :return: list
    """

    a, b = 0, 1
    num = []

    while a < n:
        num.append(a)
        a, b, = b, a + b

    return num


ret = fib2(2000)
print(ret)

i = 5


def f1(n=i):
    print('\n', n)


i = 6
f1()


def f2(a, tab=None):
    if tab == None:
        tab = []
    tab.append(a)
    print(tab)


f2(1)
f2(2)
f2(3)

f2(6, [4, 5])
