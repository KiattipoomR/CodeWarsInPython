def find_time_unit(seq) :
    zeroes = [len(x) for x in seq.split("1") if x != ""]
    ones = [len(x) for x in seq.split("0") if x != ""]
    if zeroes == [] or min(zeroes) > min(ones) :
        return min(ones)
    else : return min(zeroes)

def decodeBits(bits) :
    bits = bits.strip("0"); print(bits)
    time_unit = find_time_unit(bits)
    count = [0,0]
    morse_result = ""

    for i in range(len(bits)) :
        if bits[i] == "1" :
            count[1] += 1
            if count[0] == 3 * time_unit :
                morse_result += " "
            elif count[0] == 7 * time_unit :
                morse_result += "   "
            count[0] = 0
        if bits[i] == "0" or i == len(bits)-1 :
            if bits[i] == "0" :
                count[0] += 1
            if count[1] == time_unit :
                morse_result += "."
            elif count[1] == 3 * time_unit :
                morse_result += "-"
            count[1] = 0
    return morse_result

def decodeMorse(morseCode) :
    return " ".join(["".join([MORSE_CODE[morse] for morse in word.split()]) for word in morseCode.split("   ")])
