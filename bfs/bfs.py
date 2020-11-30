import settings
import copy

def bfs(maze_origin, start, end):
    """

    @param maze_origin: 二维列表，基本元素是字符，迷宫字符
    @param start: 元组 起始坐标
    @param end:  元组 终点坐标
    @return: 前置节点表 prev: 从终点向前倒推出路径。二维列表,基本元素是元组，存放前置结点
    """
    maze = []
    maze = copy.deepcopy(maze_origin)
    prev = []

    rows = len(maze)
    cols = len(maze[0])
    for i in range(rows):
        tmp = list()
        for j in range(cols):
            tmp.append((-1, -1));
        prev.append(tmp)
    
    openlist = []
    openlist.append(start)
    maze[start[0]][start[1]] = settings.wall_char

    dirs = list()
    dirs.append((-1, 0))
    dirs.append((1, 0))
    dirs.append((0, 1))
    dirs.append((0, -1))
    # bfs
    while len(openlist) != 0:
        current = openlist.pop(0)
        if current == end:
            break
        for dir in dirs:
            x = current[0] + dir[0]
            y = current[1] + dir[1]
            if (x >= 0 and x < rows and y >=0 and y < cols 
                and maze[x][y] != settings.wall_char):
                openlist.append((x, y))
                maze[current[0]][current[1]] = settings.wall_char
                prev[x][y] = current
    return prev
