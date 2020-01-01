def format_duration(seconds):
    if seconds < 1 : return "now"
    result = ""
    time = [seconds//31536000,(seconds//86400)%365,(seconds//3600)%24,(seconds//60)%60,seconds%60]
    
    if time[0] :
        result += str(time[0]) + (" years" if time[0] > 1 else " year")
        if time[1:].count(0) < 3 : result += ", "
        elif time[1:].count(0) < 4 : result += " and "
    if time[1] :
        result += str(time[1]) + (" days" if time[1] > 1 else " day")
        if time[2:].count(0) < 2 : result += ", "
        elif time[2:].count(0) < 3 : result += " and "
    if time[2] :
        result += str(time[2]) + (" hours" if time[2] > 1 else " hour")
        if not time[3:].count(0) : result += ", "
        elif time[3:].count(0) == 1 : result += " and "
    if time[3]:
        result += str(time[3]) + (" minutes" if time[3] > 1 else " minute")
        if time[4] : result += " and "
    if time[4] :
        result += str(time[4]) + (" seconds" if time[4] > 1 else " second")
    return result
