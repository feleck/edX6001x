animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    length = 0
    biggest = None
    for key in aDict.keys():
        val = aDict[key]
        if len(val) >= length:
            length = len(val)
            biggest = key
    return biggest
