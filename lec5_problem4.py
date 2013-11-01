def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # my solution:
    '''
    result = min(a, b)
    while result > 0:
        if a % result == 0 and b % result == 0:
            return result
        result -= 1
    '''
    # MIT solution:
    testValue = min(a, b)
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue
