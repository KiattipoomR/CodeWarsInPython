def generate_hashtag(s):
    if len(s) == 0 or len(s) > 140 : return False
    else :
        words = s.split()
        result = "#"
        for word in words :
            result += word[0].upper() + word[1:].lower()
        return result
