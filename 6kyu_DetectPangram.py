import string

def is_pangram(s):
    letter = set()
    for alphabet in s :
        alphabet = alphabet.lower()
        if "a" <= alphabet <= "z" :
            letter.add(alphabet)
    return len(letter) == 26
