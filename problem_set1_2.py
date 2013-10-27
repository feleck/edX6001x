s = 'azcbobobegghaklbob'
count = 0
#i = s.find('bob') + 1
i = 0
while i < len(s):
    if 'bob' in s[i:i+3]:
            count += 1
    
    print(s[i:])
    i += 1
print 'Number of times bob occurs is: ' + str(count)
