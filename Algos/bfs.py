import os
import sys
from collections import deque

sys.path.append(os.path.dirname(os.path.abspath(__file__))+ "/../../Search_Based/")

from Algos import grid, animation
from Algos.A_star import Astar
import math
import heapq

class BFS(Astar):

    def Search(self):

        self.P_node[self.s_start] = self.s_start
        self.g[self.s_start] = 0
        self.g[self.s_goal] = math.inf
        heapq.heappush(self.DISCOVERED, (0, self.s_start))

        while self.DISCOVERED:
            _, s = heapq.heappop(self.DISCOVERED)
            self.EXPANDED.append(s)

            if s == self.s_goal:
                break

            for node in self.neighbour(s):
                updated_cost = self.g[s] + self.cost(s, node)

                if node not in self.g:
                    self.g[node] = math.inf

                if updated_cost < self.g[node]:
                    self.g[node] = updated_cost
                    self.P_node[node] = s

                    prior = self.DISCOVERED[-1][0]+1 if len(self.DISCOVERED) > 0 else 0
                    heapq.heappush(self.DISCOVERED, (prior, node))

        return self.generate_path(self.P_node), self.EXPANDED

def main():
     s_start = (4, 2)
     s_goal =  (45, 27)

     bfs = BFS(s_start, s_goal, 'None')
     grid = animation.Plotting(s_start, s_goal)

     path, visited = bfs.Search()
     grid.animation(path, visited, "Breadth-First Search")


if __name__ == '__main__':
    main()