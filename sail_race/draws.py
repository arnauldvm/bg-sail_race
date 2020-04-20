from pytgbb.randomizers import Die


die = Die(6)
die.seed(0)


def draw():
    # 2 random numbers in [1, 6]
    # Not really useful, since we could use Die(36) immediately,
    #   but so we simulate the real game more closely
    return die.draws(2)


def draw36():
    # 1 random number in [0, 35]
    d = draw()
    return (d[0]-1)*6+(d[1]-1)
