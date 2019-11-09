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
        wins = [o.win for o in group]
        wins_avg = s.mean(wins)
        plot_groups.append(GameResult(group[0].player_sum, group[0].dealer_card_showing, wins_avg))
    return plot_groups

def plot(plot_groups):
    fig = plt.figure();
    ax = fig.gca(projection = '3d');

    # Plot the surface.
    # X - liczba kroków
    # Y - wartość odsłoniętej karty dealera
    # Z - uśredniona wartość z przedziału [0, 1]

    surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 0, antialiased = False);

    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01);
    ax.zaxis.set_major_locator(LinearLocator(10));
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'));

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink = 0.5, aspect = 5);
    plt.show();

if __name__ == '__main__':
    usable_ace = False

    game_results = []
    for iteration in range(100000):
        result = Game(usable_ace).play(10)
        game_results.append(result)

    plot_groups = get_plot_groups()
