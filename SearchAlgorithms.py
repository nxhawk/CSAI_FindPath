from Type import *
from Constants import *


def check_Node(node: Node, arr: list[Node]):
    for curr in arr:
        if curr.value == node.value:
            return True
    return False


def show_path(g: Graph, path, sc: pygame.surface):
    g.goal.set_color(purple)
    g.draw(sc)
    child = g.goal.value
    while child != g.start.value:
        pygame.draw.line(sc, green, (g.grid_cells[child].x, g.grid_cells[child].y), (
            g.grid_cells[path[child]].x, g.grid_cells[path[child]].y), 2)
        pygame.display.flip()
        child = path[child]
        g.grid_cells[child].set_color(grey)
        g.draw(sc)
    g.start.set_color(orange)
    g.draw(sc)


def BFS(g: Graph, sc: pygame.Surface):
    open_set: list[Node] = [g.start]
    closed_set: list[Node] = []
    father = [-1]*g.get_len()

    while len(open_set) > 0:
        # lay node dau stack
        N_current: Node = open_set[0]
        # change color
        N_current.set_color(yellow)
        g.draw(sc)
        # if da den dich
        if g.is_goal(N_current):
            show_path(g, father, sc)
            return
        # remove this
        open_set.remove(N_current)
        # them vao closed
        closed_set.append(N_current)
        # da tham
        N_current.set_color(blue)
        g.draw(sc)
        # them cac nut neighbors
        neighbors: list[Node] = g.get_neighbors(N_current)
        for neighbor in neighbors:
            if not check_Node(neighbor, open_set) and not check_Node(neighbor, closed_set):
                if neighbor.value != g.goal.value:
                    neighbor.set_color(red)
                    g.draw(sc)
                open_set.append(neighbor)
                father[neighbor.value] = N_current.value


def DFS(g: Graph, sc: pygame.Surface):
    open_set: list[Node] = [g.start]
    closed_set: list[Node] = []
    father = [-1]*g.get_len()

    while len(open_set) > 0:
        # lay node dau stack
        N_current: Node = open_set[len(open_set) - 1]
        # change color
        N_current.set_color(yellow)
        g.draw(sc)
        # if da den dich
        if g.is_goal(N_current):
            show_path(g, father, sc)
            return
        # them vao closed
        closed_set.append(N_current)
        # da tham
        N_current.set_color(blue)
        g.draw(sc)
        # them cac nut neighbors
        neighbors: list[Node] = g.get_neighbors(N_current)
        check: bool = False
        for neighbor in neighbors:
            if not check_Node(neighbor, open_set) and not check_Node(neighbor, closed_set):
                if neighbor.value != g.goal.value:
                    neighbor.set_color(red)
                    g.draw(sc)
                open_set.append(neighbor)
                father[neighbor.value] = N_current.value
                check = True
                break
        if not check:
            open_set.remove(N_current)


def Min_Cost(open_set: list[Node], cost):
    min = 100_000
    temp = open_set[0]
    for node in open_set:
        if min > cost[node.value]:
            min = cost[node.value]
            temp = node
    return temp


def UCS(g: Graph, sc: pygame.Surface):
    open_set: list[Node] = [g.start]
    closed_set: list[Node] = []
    father = [-1]*g.get_len()
    cost = [100_000] * g.get_len()
    cost[g.start.value] = 0

    while len(open_set) > 0:
        # lay node dau stack
        N_current: Node = Min_Cost(open_set, cost)
        # change color
        N_current.set_color(yellow)
        g.draw(sc)
        # if da den dich
        if g.is_goal(N_current):
            show_path(g, father, sc)
            return
        # remove this
        open_set.remove(N_current)
        # them vao closed
        closed_set.append(N_current)
        # da tham
        N_current.set_color(blue)
        g.draw(sc)
        # them cac nut neighbors
        neighbors: list[Node] = g.get_neighbors(N_current)
        for neighbor in neighbors:
            if not check_Node(neighbor, open_set) and not check_Node(neighbor, closed_set):
                if neighbor.value != g.goal.value:
                    neighbor.set_color(red)
                    g.draw(sc)
                open_set.append(neighbor)
                father[neighbor.value] = N_current.value
                cost[neighbor.value] = cost[N_current.value] + \
                    g.Cost_two_Node(N_current, neighbor)


def AStar(g: Graph, sc: pygame.Surface):
    open_set: list[Node] = [g.start]
    closed_set: list[Node] = []
    father = [-1]*g.get_len()
    cost = [100_000] * g.get_len()
    cost[g.start.value] = 0 + g.heuristic(g.start)

    while len(open_set) > 0:
        # lay node dau stack
        N_current: Node = Min_Cost(open_set, cost)
        # change color
        N_current.set_color(yellow)
        g.draw(sc)
        # if da den dich
        if g.is_goal(N_current):
            show_path(g, father, sc)
            return
        # remove this
        open_set.remove(N_current)
        # them vao closed
        closed_set.append(N_current)
        # da tham
        N_current.set_color(blue)
        g.draw(sc)
        # them cac nut neighbors
        neighbors: list[Node] = g.get_neighbors(N_current)
        for neighbor in neighbors:
            if not check_Node(neighbor, open_set) and not check_Node(neighbor, closed_set):
                if neighbor.value != g.goal.value:
                    neighbor.set_color(red)
                    g.draw(sc)
                open_set.append(neighbor)
                father[neighbor.value] = N_current.value
                cost[neighbor.value] = cost[N_current.value] + \
                    g.Cost_two_Node(N_current, neighbor) + \
                    g.heuristic(neighbor)
