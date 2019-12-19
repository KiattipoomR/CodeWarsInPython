def likes(names) :
    length = len(names)
    if length == 0 :
        return "no one likes this"
    if length == 1 :
        return names[0] + " likes this"
    else :
        output = names[0]
        if length > 2 :
            output += ", " + names[1]
        output += " and "
        if length > 3 :
            output += str(length - 2) + " others"
        else :
            output += names[-1]
        output += " like this"
        return output
