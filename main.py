from game import Game

if __name__ == '__main__':
    usable_ace = False

    for start_check_limit in range(10, 20):
        game_results = []
        for iteration in range(10000):
            result = Game(usable_ace).play(start_check_limit)
            game_results.append(result)

        # TODO: Uśrednić game_results i narysować wykres