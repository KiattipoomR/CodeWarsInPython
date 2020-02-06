def is_valid_IP(strng):
    strng = strng.split('.')
    if len(strng) == 4 :
        try :
            ipnum = [int(x) for x in strng]
            for i in range(4) :
                if not(0 <= ipnum[i] <= 255) or str(ipnum[i]) != strng[i] :
                    return False 
            return True
        except ValueError : return False
    return False
