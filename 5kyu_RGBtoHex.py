def to_hex(x):
    if x < 0 : x = 0
    elif x > 255 : x = 255
    
    if x < 10 : x = "0" + hex(x)[2:]
    else : x = hex(x)[2:]
    return x

def rgb(r, g, b):
    return (to_hex(r) + to_hex(g) + to_hex(b)).upper()
