def house_numbers_sum(inp):
    sums = 0
    for house in inp :
        if house == 0 :
            return sums
        else : 
            sums += house
