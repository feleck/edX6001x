def isVowel2(char):
    '''
    char: a single letter of any case
    with use of _in_
    vowels are:  ('a', 'e', 'i', 'o', or 'u'),
    returns: True if char is a vowel and False otherwise.
    '''
    return char in ('aAeEiIoOuU')
    # solution:
    # return char.lower() in 'aeiou'


