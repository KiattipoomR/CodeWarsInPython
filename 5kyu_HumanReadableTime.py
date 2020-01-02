def make_readable(seconds):
    result = ""

    dh = seconds // 3600
    dm = (seconds // 60) % 60
    ds = seconds % 60
    
    if dh < 10 : result += "0"
    result += str(dh) + ":"

    if dm < 10 : result += "0"
    result += str(dm) + ":"
    
    if ds < 10 : result += "0"
    result += str(ds)
    
    return result
