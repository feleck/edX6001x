stuff = ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
stuff1 = ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
stuff2 = [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
stuff3 = ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
stuff4 = "iPad"
stuff5 = 'iPad'

for thing in stuff:
    if thing == 'iPad':
        print "Found it"

for thing in stuff1:
    if thing == 'iPad':
        print "Found it0"
for thing in stuff2:
    if thing == 'iPad':
        print "Found it1"
for thing in stuff3:
    if thing == 'iPad':
        print "Found it2"
for thing in stuff4:
    if thing == 'iPad':
        print "Found it3"
for thing in stuff5:
    if thing == 'iPad':
        print "Found it4"
