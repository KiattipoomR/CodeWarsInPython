def interleave(*args):
    result = []
    length = [len(x) for x in args]
    if len(args) == 1 :
        return args[0]
    for items in args :
        if len(items) != max(length) :
            for i in range(max(length) - len(items)) :
                items.append(None)
    for j in range(max(length)) :
        for items in args :
            result.append(items[j])
    return result
