def decodeMorse(morse_code):
    morse_code = morse_code.strip().split(" ")
    idx = 0
    result = ""
    while idx < len(morse_code) :
        if morse_code[idx] == "" and result != "" :
            result += " "
            idx += 2
        else :
            if morse_code[idx] != ""  :
                result += MORSE_CODE[morse_code[idx]]
            idx += 1
    return result
