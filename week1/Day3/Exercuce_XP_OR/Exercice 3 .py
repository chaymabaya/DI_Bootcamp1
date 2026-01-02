def throw_until_doubles():
    count = 0

    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        count += 1

        if dice1 == dice2:
            break

    return count
def throw_dice():
    import random
    return random.randint(1, 6)