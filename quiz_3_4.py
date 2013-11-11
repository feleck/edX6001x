def testLog():
    print myLog(1, 2)
    print myLog(2, 2)
    print myLog(16, 2) == 4
    print myLog(15, 3) == 2
    


def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    result = 0
    while b ** (result+1) <= x:
        print b**result
        result += 1
    return result
