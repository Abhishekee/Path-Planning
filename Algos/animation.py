import os
import sys
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
                "/../../Search_Based/")

from Algos import grid


class Plotting:
    def __init__(self, S, G):
        self.S, self.G = S, G
        self.grid = grid.Grid()
        self.obs = self.grid.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    def animation(self, path, visited,  name):
        self.plot_grid(name)
        self.plot_visited(visited)
        self.plot_path(path)
        plt.show()

    def plot_grid(self, name):
        obs_x = [x[0] for x in self.obs]
        obs_y = [x[1] for x in self.obs]

        plt.plot(self.S[0], self.S[1], "bs")
        plt.plot(self.G[0], self.G[1], "gs")
        plt.plot(obs_x, obs_y, "sk")
        plt.title(name)
        plt.axis("equal")

    def plot_visited(self, visited, cl='b'):
        if self.S in visited:
            visited.remove(self.S)

        if self.G in visited:
            visited.remove(self.G)

        count = 0

        for x in visited:
            count += 1
            plt.plot(x[0], x[1], color=cl, marker='o')
            plt.gcf().canvas.mpl_connect('key_release_event',
                                         lambda event: [exit(0) if event.key == 'escape' else None])

            if count < len(visited) / 3:
                length = 20
            elif count < len(visited) * 2 / 3:
                length = 30
            else:
                length = 40
            

            if count % length == 0:
                plt.pause(0.001)
        plt.pause(0.01)

    def plot_path(self, path, cl='g', flag=False):
        path_x = [path[i][0] for i in range(len(path))]
        path_y = [path[i][1] for i in range(len(path))]

        if not flag:
            plt.plot(path_x, path_y, linewidth='3', color='g')
        else:
            plt.plot(path_x, path_y, linewidth='3', color=cl)

        plt.plot(self.S[0], self.S[1], "bs")
        plt.plot(self.G[0], self.G[1], "gs")

        plt.pause(0.01)



    