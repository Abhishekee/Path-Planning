import heapq
import sys
import math
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__))+ "/../../Search_Based/")

from Algos import grid, animation
from Algos.A_star import Astar

class Dijkstra(Astar):

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

                   heapq.heappush(self.DISCOVERED, (updated_cost, node))

        return self.extract_path(self.P_node), self.EXPANDED

    def extract_path(self, P):

        path = [self.s_goal]
        s = self.s_goal

        while True:
            s = P[s]
            path.append(s)

            if s == self.s_start:
                break

        return list(path)



def main():
    s_start = (4, 2)
    s_goal = (45, 27)

    dijkstra = Dijkstra(s_start, s_goal, "None")
    grid = animation.Plotting(s_start, s_goal) 

    path, visited = dijkstra.Search()
    grid.animation(path, visited, "Dijkstra")

if __name__ == '__main__':
    main()