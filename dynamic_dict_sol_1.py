a = {
    'key1': 1,
    'key2': {
        'key3': {
            'key5': 1
        },
        'key4': {
            'key6': {
                'key7' : 6,
                'key8' : 6
            }
        }
    }
}
'''a = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 4
        }
    }
}'''
def print_depth(data):
    keys = []
    values = []
    pair = {}
    for x,y in data.items():
        keys.append((x,y))
        values.append(1)
        pair[x] = 1

    while keys:
        k = keys.pop(0)
        val = k[1]
        inc = values[len(values)-1]
        if isinstance(val,dict):
            inc += 1
            for x,y in val.items():
                keys.append((x,y))
                values.append(inc)
                pair[x] = inc
    return pair

pair = print_depth(a)
for x,y in pair.items():
    print(x+" "+str(y))





