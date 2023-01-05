import os
import math
import heapq
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__))+ "/../../Search_Based")

from Algos import grid, animation

class Astar:
    def __init__(self, s_start, s_goal, heuristic_name):
        self.s_start = s_start
        self.s_goal = s_goal
        self.heuristic_name = heuristic_name

        self.grid = grid.Grid()
        self.input = self.grid.motions
        self.obs = self.grid.obs

        self.DISCOVERED = []
        self.EXPANDED = []
        self.P_node = dict()
        self.g = dict()



    def Search(self):
        self.P_node[self.s_start] = self.s_start
        self.g[self.s_start] = 0
        self.g[self.s_goal] = math.inf
        heapq.heappush(self.DISCOVERED, (self.f_cost(self.s_start), self.s_start))

        while self.DISCOVERED:
            _, s = heapq.heappop(self.DISCOVERED)
            self.EXPANDED.append(s)

            if s == self.s_goal:
                break
           
            for node in self.neighbour(s):
                updated_cost = self.g[s] + self.cost(s, node)

                if node not in self.g:
                    self.g[node] = math.inf

                if updated_cost <  self.g[node]:
                    self.g[node] = updated_cost
                    self.P_node[node] = s
                    heapq.heappush(self.DISCOVERED, (self.f_cost(node), node))

        return self.generate_path(self.P_node), self.EXPANDED

    def neighbour(self, s):
        return [(s[0] + i[0], s[1] + i[1]) for i in self.input]

    def cost(self, s_start, s_goal):
        
        if self.collision(s_start, s_goal):
            return math.inf

        return math.hypot(s_goal[0] - s_start[0], s_goal[1] - s_start[1])

    def collision(self, s_start, s_collide):
        if s_start in self.obs or s_collide in self.obs:
            return True

        if s_start[0] != s_collide[0] and s_start[1] != s_collide[1]:
            if s_collide[0] - s_start[0] == s_start[1] - s_collide[1]:
                s1 = (min(s_start[0], s_collide[0]), min(s_start[1], s_collide[1]))
                s2 = (max(s_start[0], s_collide[0]), max(s_start[1], s_collide[1]))
            else:
                s1 = (min(s_start[0], s_collide[0]), max(s_start[1], s_collide[1]))
                s2 = (max(s_start[0], s_collide[0]), min(s_start[1], s_collide[1]))

            if s1 in self.obs or s2 in self.obs:
                return True

        return False

    def f_cost(self, s):
        return self.g[s] + self.heuristic(s)
    


    
    def generate_path(self, P):

        path = [self.s_goal]
        s = self.s_goal

        while True:
            s = P[s]
            path.append(s)

            if s == self.s_start:
                break

        return list(path)

    def heuristic(self, s):
        heuristic_name = self.heuristic_name
        goal = self.s_goal

        if heuristic_name == "manhattan":
              return abs(goal[0] - s[0]) + abs(goal[1] - s[1])
        else:
          return math.hypot(goal[0] - s[0], goal[1] - s[1])

def main():
        s_start = (5,5)
        s_goal = (45,27)

        a_star = Astar(s_start, s_goal, "manhattan")
        grid = animation.Plotting(s_start, s_goal)

        path, visited = a_star.Search()
        grid.animation(path, visited, "A*")
        
if __name__ == '__main__':
        main()
