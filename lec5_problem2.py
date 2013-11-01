def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    if exp > 0:
        result = base * recurPower(base, exp-1)
    return result
