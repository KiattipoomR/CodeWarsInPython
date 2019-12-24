def to_weird_case(string):
    result = ""
    sel = 0
    for i in string : 
        if sel or i == " " :
            sel = 0
            result += i.lower()
        else :
            sel = 1
            result += i.upper()
    return result
