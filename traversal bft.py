import collections

def bft(graph, root):

    vis, queue = set(), collections.deque([root])
    vis.add(root)

    while queue:

        ver = queue.popleft()
        print(str(ver) + " ", end="")

        for nbr in graph[ver]:
            if nbr not in vis:
                vis.add(nbr)
                queue.append(nbr)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("This is the traversal algorithm of breadth first traversal: ")
    bft(graph, 0)