s = 'azcbobobegghakl' # beggh
s = 'abcbcd'
s = 'abcdefghijklmnopqrstuvwxyz'
s = 'lzhhfwwccgiw' # ccgiw
s = 'esmyrioepeyxbspaii' # aii

i = 0
longest_sub_string = ''
sub_string = ''

for i in range(len(s)-1):
    print(i, s[i])
    if s[i] <= s[i+1]:
        sub_string += s[i] #+ s[i+1]
        if i+1 == len(s)-1:
            sub_string += s[i+1]
        if len(sub_string) > len(longest_sub_string):
            longest_sub_string = sub_string
    else:
        sub_string += s[i]
        if len(sub_string) > len(longest_sub_string):
            longest_sub_string = sub_string
        sub_string = ''
    i += 1
print 'Longest substring in alphabetical order is: ' + str(longest_sub_string)
