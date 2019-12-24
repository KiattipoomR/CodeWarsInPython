def namelist(names):
    length = len(names)
    result = ""
    if length > 2 :
        others = names[:-2]
        names = names[-2:]
        result += ", ".join([person["name"] for person in others]) + ", "
    if length > 1 :
        result += names[-2]["name"] + " & "
    if length > 0 :
        result += names[-1]["name"]
    return result
