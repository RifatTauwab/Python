def swap_char(sentance):
    sentance = list(sentance)
    for i in range(len(sentance)):    
        if sentance[i].isalpha():
            if ord(sentance[i])<91:        
                sentance[i] = chr(ord(sentance[i])+32)
            else:          
                sentance[i] =  chr(ord(sentance[i])-32)
    return ''.join(sentance)

print swap_char("HeLlo")
