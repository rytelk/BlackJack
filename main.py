from game import Game

if __name__ == '__main__':
    usable_ace = False

    for start_check_limit in range(10, 20):
        for iteration in range(10000):
            Game(usable_ace).play(start_check_limit)