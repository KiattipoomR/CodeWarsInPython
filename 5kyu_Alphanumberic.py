def alphanumeric(password):
    alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    if len(password) == 0 : return False
    for letter in password :
        if letter not in alphanumeric : return False
    return True
