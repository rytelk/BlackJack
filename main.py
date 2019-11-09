from game import Game
from game_result import GameResult
from itertools import groupby
import statistics as s
from mpl_toolkits.mplot3d import Axes3D;
import matplotlib.pyplot as plt;
from matplotlib import cm;
from matplotlib.ticker import LinearLocator, FormatStrFormatter;
import numpy as np;

def get_plot_groups():
    sorted_groups = sorted(game_results, key=lambda a: (a.player_sum, a.dealer_card_showing))
    groups = groupby(sorted_groups, lambda a: (a.player_sum, a.dealer_card_showing))
    plot_groups = []
    for key, group in groups:
        group = list(group)
        wins = [g.win for g in group]
        wins_avg = s.mean(wins)
        plot_groups.append(GameResult(group[0].player_sum, group[0].dealer_card_showing, wins_avg))
    return plot_groups

def plot(plot_groups, start_check_limit):
    fig = plt.figure();
    ax = fig.gca(projection = '3d');

    X = np.arange(2, 11, 1)
    Y = np.arange(start_check_limit, 21, 1)
    X, Y = np.meshgrid(X, Y)

    Z = []
    for x_array in X:
        for y_array in Y:
            z_array = []
            for x in x_array:
                for y in y_array:
                    group = next(pg for pg in plot_groups if pg.dealer_card_showing == x and pg.player_sum == y)
                    x = 5
                    z_array.append(group.win)
            Z.append(z_array)


    surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 0, antialiased = False);

    # Customize the z axis.
    ax.set_zlim(-1, 1);
    ax.zaxis.set_major_locator(LinearLocator(10));
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'));

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink = 0.5, aspect = 5);
    plt.show();

if __name__ == '__main__':
    usable_ace = False

    start_check_limit = 10
    game_results = []
    for iteration in range(1000):
        result = Game(usable_ace).play(start_check_limit)
        game_results.append(result)

    plot_groups = get_plot_groups()
    plot(plot_groups, start_check_limit)