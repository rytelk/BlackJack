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

def plot(plot_groups, start_check_limit, usable_ace, save_to_file=False):
    fig = plt.figure();
    ax = fig.gca(projection = '3d');

    X = np.arange(2, 12, 1)
    Y = np.arange(start_check_limit, 22, 1)
    X, Y = np.meshgrid(X, Y)

    Z = []
    for arrays in zip(X, Y):
        z_array = []
        for point in zip(arrays[0], arrays[1]):
            group = next(pg for pg in plot_groups if pg.dealer_card_showing == point[0] and pg.player_sum == point[1])
            z_array.append(group.win)
        Z.append(z_array)

    Z = np.array(Z)
    surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 0, antialiased = False);

    # Customize the z axis.
    ax.set_zlim(-1, 1);
    ax.zaxis.set_major_locator(LinearLocator(10));
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'));

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink = 0.5, aspect = 5);

    ax.set_title(f"Cut-off value: {start_check_limit}, usable ace: {usable_ace}")
    ax.set_xlabel("Dealer card at hand value")
    ax.set_ylabel("Player sum at hand")
    ax.set_zlabel("Average win")

    # plt.show()

    if save_to_file:
        plt.savefig(f"img/graph_ace_{usable_ace}_{start_check_limit}.png")
    

if __name__ == '__main__':
    for usable_ace in [False, True]:
        for start_check_limit in range(15, 21):
            print(f"Generating data and graph for: limit={start_check_limit}, usable_ace={usable_ace}")

            game_results = []

            for iteration in range(100000):
                result = Game(usable_ace).play(start_check_limit)
                game_results.append(result)

            plot_groups = get_plot_groups()
            plot(plot_groups, start_check_limit, usable_ace, save_to_file=True)