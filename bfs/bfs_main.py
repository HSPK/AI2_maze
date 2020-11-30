from bfs import bfs
import settings
import numpy as np

def make_maze_path(prev, start, end):
    """
    :param prev: 前置节点表: 从终点向前倒推出路径。二维列表,基本元素是元组,存放前置结点
    :param start: 起点,元组 (a,b)
    :param end: 终点,元组 (a,b)
    :return: 迷宫路径: path。元组列表 [(a,b),(c,d),...,]
    """
    # path 存放要返回的结果---迷宫路径
    path = list()
    # 根据prev和end，从终点向前倒推
    current = end
    while current != start:
        current = prev[current[0]][current[1]]
        path.append(current)
    path.append(start)
    return path


def make_maze_result(maze_origin, path):
    """

    :param maze_origin: 迷宫地图，二维列表: 基本元素是字符,迷宫字符
    :param path: 迷宫路径，元组列表 [(a,b),(c,d),...,]
    :return: 带有↑↓←→的迷宫地图 maze。二维列表: 基本元素是字符,迷宫字符和上下左右字符
    """
    # maze = copy.deepcopy(maze_origin)
    maze = maze_origin.copy()
    for i in range(len(path) - 1):
        if (path[i][0] == path[i + 1][0] + 1):
            maze[path[i][0]][path[i][1]] = '↓'
        elif (path[i][0] == path[i + 1][0] - 1):
            maze[path[i][0]][path[i][1]] = '↑'
        elif (path[i][1] == path[i + 1][1] - 1):
            maze[path[i][0]][path[i][1]] = '←'
        elif (path[i][1] == path[i + 1][1] + 1):
            maze[path[i][0]][path[i][1]] = '→'
    return maze


maze = []  # list of list
start = (-1, -1)
end = (-1, -1)

with open(settings.filename) as file:
    # 将file按行读取到maze中，并且更新起点start，终点end
    for i, line in enumerate(file):
        line = line.strip()
        start_col = line.find(settings.start_char)
        end_col = line.find(settings.end_char)
        if (start_col != -1):
            start = (i, start_col)
        if end_col != -1:
            end = (i, end_col)
        maze.append(list(line))


maze = np.array(maze)
prev = bfs(maze, start, end)

path = make_maze_path(prev, start, end)

print('\n\n【Steps】:', len(path))

print('\n【Path】:')
length = len(path)
print('-' * 85)
for i in range(1, length + 1):
    print(path[length - i], end="\t")
    if i % 10 == 0:
        print()
print()
print('-' * 85)

print('\n【result】:')
maze_result = make_maze_result(maze, path)
for line in maze_result:
    print(''.join(line))