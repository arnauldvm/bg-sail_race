from pytgbb.randomizers import Die


_die = Die(6)


def seed(*args, **kwargs):
    _die.seed(*args, **kwargs)


def draw():
    # 2 random numbers in [1, 6]
    # Not really useful, since we could use Die(36) immediately,
    #   but so we simulate the real game more closely
    return _die.draws(2)


def _2d6_to_d36(dice):
    return (dice[0]-1)*6+(dice[1]-1)


def draw36():
    # 1 random number in [0, 35]
    return _2d6_to_d36(draw())


seed(None)  # Initializes from system time
