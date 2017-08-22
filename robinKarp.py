def nextHash(prevHash,firstLetter,prime,lastLetter):
    value = ((prevHash - ord(firstLetter))/prime)+(ord(lastLetter)*(prime**(m-1)))
    return value

def firstHash(text,prime):
    length = len(text)
    value = 0
    for i in range(length):
        value = value + ord(text[i])*(prime**i)
    return value

def match(text,pattern):
    global prime
    n = len(text)
    m = len(pattern)
    H0 = firstHash(text[:m],prime)
    Hprev = H0
    PHash = firstHash(pattern,prime)
    Hnext = 0
    matchPosition = -1
    for i in range(n-m+1):
        if(i == 0):
            if(H0 == PHash):
                matchPosition = i
                print "found at position %d"% (matchPosition)
        else:
            Hnext = nextHash(Hprev,text[i-1],prime,text[m+i-1])
            if(Hnext == PHash):
                matchPosition = i
                print "found at position %d"% (matchPosition)
            else:
                Hprev = Hnext
    if(matchPosition == -1):
        print matchPosition
    

text = 'I have a Book'  
pattern = 've'
m = len(pattern)
prime = 3
match(text,pattern)

        
        
