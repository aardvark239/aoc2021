import numpy as np
from collections import deque


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = {}
        self.counter = 0
        self.goal = "end"
        self.n_paths = {}
        self.n = 0
        self.id = {}

    # function to add an edge to graph
    def addEdge(self, u, v):
        if u not in self.graph.keys():
            self.graph[u] = []
            if u.islower():
                self.id[u] = self.n
                self.n += 1
        if v not in self.graph.keys():
            self.graph[v] = []
            if v.islower():
                self.id[v] = self.n
                self.n += 1
        self.graph[u].append(v)
        self.graph[v].append(u)

    # A function used by DFS
    def DFSUtil(self, v, visited, acc, path, flag):
        # Mark the current node as visited
        # and print it
        path.append(v)
        if v == self.goal:
            self.counter += 1
            print(path)
            path.pop()
            return 1
            #print(path)
        else:
            if v.islower():
                visited[v] += 1
                if visited[v] == 2:
                    flag = True
                acc += 3**self.id[v]

            if (v, acc) in self.n_paths.keys():
                res = self.n_paths[(v, acc)]
                self.counter += res
            # Recur for all the vertices
            # adjacent to this vertex
            else:
                res = 0
                for neighbour in self.graph[v]:
                    if visited[neighbour] < 1 or (neighbour != "start" and not flag and (visited[neighbour] < 2)):
                        res += self.DFSUtil(neighbour, visited, acc, path, flag)
                self.n_paths[(v, acc)] = res
            if v.islower():
                visited[v] -= 1
                if visited[v] == 1:
                    flag = False
                acc -= 3**self.id[v]
                #self.n_paths[(v, acc)] = res
            path.pop()
        return res
        #path.pop()

    def DFS(self, v):
        visited = {x: 0 for x in self.graph.keys()}
        path = []
        acc = 0
        flag = False
        res = self.DFSUtil(v, visited, acc, path, flag)
        return res


def main():
    G = Graph()
    with open("input.txt") as f:
        for line in f:
            b, e = line.strip().split("-")
            G.addEdge(b, e)

    print(G.DFS("start"))


if __name__ == "__main__":
    main()
