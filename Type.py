import pygame
from Constants import *
from math import *


class Node:
    def __init__(self, x, y, value, radius=10) -> None:
        '''
        x, y: toa do cua node
        value: gia tri cua node
        radius: ban kinh node default = 10
        '''
        self.x, self.y, self.value, self.radius = x, y, value, radius
        self.color = green

    def draw(self, sc: pygame.Surface) -> None:
        '''ham ve mot node voi gia tri cua node do'''
        pygame.draw.circle(sc, self.color, (self.x, self.y), self.radius, 0)

        font = pygame.font.Font(pygame.font.get_default_font(), 10)
        node_label = font.render(str(self.value), True, white)
        sc.blit(node_label, (self.x, self.y))

    def set_color(self, color) -> None:
        '''        doi mau node        color: Tuple(r, g, b)    '''
        self.color = color


class Graph:
    def __init__(self, start_pos: int, goal_pos: int) -> None:
        self.grid_cells: list[Node] = []
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                self.grid_cells.append(
                    Node(j*TILE+TILE/2, i*TILE+TILE/2, (i-1)*(cols-2)+(j-1)))

        self.start: Node = self.grid_cells[start_pos]
        self.start.set_color(orange)
        self.goal: Node = self.grid_cells[goal_pos]
        self.goal.set_color(purple)

    def draw(self, sc: pygame.Surface):
        '''
        vẽ đồ thị lên bề mặt `sc`
        '''
        for node in self.grid_cells:
            node.draw(sc)
        pygame.display.flip()

    def get_len(self) -> int:
        return len(self.grid_cells)

    def is_goal(self, node: Node) -> bool:
        return node.value == self.goal.value

    def heuristic(self, node: Node) -> float:
        return abs(self.goal.x - node.x) + abs(self.goal.y - node.y)

    def Cost_two_Node(self, a: Node, b: Node) -> float:
        return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2))

    def get_neighbors(self, node: Node) -> list[Node]:
        r = node.value//(cols-2)
        c = node.value % (cols-2)

        up = (r-1, c) if r-1 >= 0 else None
        down = (r+1, c) if r+1 < (rows-2) else None
        left = (r, c-1) if c-1 >= 0 else None
        right = (r, c+1) if c+1 < (cols-2) else None

        up_left = (r-1, c-1) if r-1 >= 0 and c-1 >= 0 else None
        up_right = (r-1, c+1) if r-1 >= 0 and c+1 < (cols-2) else None
        down_left = (r+1, c-1) if r+1 < (rows-2) and c-1 >= 0 else None
        down_right = (r+1, c+1) if r+1 < (rows-2) and c+1 < (cols-2) else None

        directions = [up, down, left, right,
                      up_left, up_right, down_left, down_right]
        neighbors = []
        for dir in directions:
            if dir is not None:
                neighbors.append(self.grid_cells[dir[0]*(cols-2) + dir[1]])
        return neighbors
