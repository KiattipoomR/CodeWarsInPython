def rearrange(num) :
    return int(''.join(sorted([i for i in str(num)])[::-1]))

def sqr_modulus(z):
    typecheck = [False for x in z[1:] if type(x) != int]
    if len(typecheck) > 0 or ('cart','polar').count(z[0]) != 1 :
        return (False, -1, 1)
        
    num = 0
    for i in range(1, len(z), 2) :
        if z[0] == 'cart' : num += (z[i] ** 2) + (z[i+1] ** 2)
        else : num += z[i] ** 2
    return (True, num, rearrange(num))
