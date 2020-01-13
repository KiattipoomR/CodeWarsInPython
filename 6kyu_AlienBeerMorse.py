def morse_converter(string):
    morse = ""
    for i in range(0,len(string),5) :
        num = string[i:i+5]
        if num[0] == '.' : morse += str(num.count('.'))
        else : morse += str((num.count('-') + 5) % 10)
    return int(morse)
