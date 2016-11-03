givenString = raw_input()
matchingString = raw_input()
print len([i for i in range(len(givenString)) if givenString.startswith(matchingString, i)])

    

