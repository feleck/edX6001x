def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''

    #this was my solution:
    ''' 
    result = 1
    if exp > 0:
        result = base * recurPower(base, exp-1)
    return result
    '''
    #this was MIT solution:
    if exp <= 0:
        return 1

    return base * recurPower(base, exp - 1)
