def score(dice):
    points = 0
    if dice.count(6) > 2 : points += 600
    if dice.count(4) > 2 : points += 400
    if dice.count(3) > 2 : points += 300
    if dice.count(2) > 2 : points += 200
    if dice.count(1) > 0 :
        points += (100 * (dice.count(1) % 3))
        if dice.count(1) > 2 : points += 1000
    if dice.count(5) > 0 :
        points += (50 * (dice.count(5) % 3))
        if dice.count(5) > 2 : points += 500
    return points
