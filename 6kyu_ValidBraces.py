def validBraces(string):
    braces_dict = {"{" : "}", "[" : "]", "(" : ")"}
    stack = []
    for brace in string :
        if ("[","(","{").count(brace) == 1 :
            stack.append(brace)
        else :
            if len(stack) == 0 :
                return False
            checker = stack.pop(len(stack)-1)
            if braces_dict[checker] != brace :
                return False
    if len(stack) == 0 :
        return True
    else :
        return False
