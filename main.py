from game import Game

if __name__ == '__main__':
    usable_ace = False

    game_results = []
    for iteration in range(1000):
        result = Game(usable_ace).play(10)
        game_results.append(result)

        # TODO: Uśrednić game_results i narysować wykres
    test = game_results