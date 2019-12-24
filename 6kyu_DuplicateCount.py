def duplicate_count(text):
    count = dict()
    duplicate = set()
    for letter in text :
        letter = letter.lower()
        if letter not in count :
            count[letter] = 0
        else :
            count[letter] += 1
            duplicate.add(letter)
    return len(duplicate)
