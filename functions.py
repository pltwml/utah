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


fib(2000)

