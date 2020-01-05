import string

def pig_it(text):
    text = text.split()
    for i in range(len(text)) :
        check = [letter in string.ascii_letters for letter in text[i]]
        if check.count(True) == len(text[i]) :
            text[i] = text[i][1:] + text[i][0] + "ay"
    return " ".join(text)
