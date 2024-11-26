# # s = input().split()
# # print(s)

# B = input().split()
# C = input().split()
# D = []
# def E(i,j):
#     if 0 < int(C[0]) + i < int(B[0]) and 0 < int(C[1]) + j < int(B[1]) :
#         import math
#         route_1 = math.comb(int(B[0])+int(B[1])-int(C[0]) - i - int(C[1]) - j,int(B[0])-int(C[0])-i)
#     else:
#         route_1 = 0
#     return route_1

# def K(i,j):
#     if 0 < int(C[0]) + i < int(B[0]) and 0 < int(C[1]) + j < int(B[1]) :
#         import math
#         route_2 = math.comb(int(C[0]) + i + int(C[1]) + j,int(C[1]) + j)
#     else:
#         route_2 = 0
#     return route_2

# import math
# n0 = K(0,0)
# n1 = K(-1,-2)
# n2 = K(1,-2)
# n3 = K(-1,2)
# n4 = K(1,2)

# m0 = E(0,0)
# m1 = E(-1,-2)
# m2 = E(1,-2)
# m3 = E(-1,2)
# m4 = E(1,2) 

# L0 = (n0-n1*3)*m0
# L1 = n1*m1
# L2 = (n2-n1)*m2
# L3 = (n3-n1)*m3
# L4 = (n4-n1*15-n2+n1-n3+n1-n0*3+n1*9)*m4

# all_route = math.comb(int(B[0])+int(B[1]),int(B[0]))

# route = all_route-L0-L1-L2-L3-L4
# print(route)

# import numpy as np
# import matplotlib.pyplot as plt

# def count_neighbors(grid, x, y, rows, cols):
#     """计算指定细胞的活细胞邻居数量"""
#     count = 0
#     for i in range(max(0, x-1), min(x+2, rows)):
#         for j in range(max(0, y-1), min(y+2, cols)):
#             if (i, j) != (x, y):  # Exclude the cell itself
#                 count += grid[i, j]
#     return count

# def update_grid(grid):
#     """根据生命游戏规则更新网格状态"""
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
    
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y, rows, cols)
#             if grid[x, y] == 1 and neighbors in [2, 3]:
#                 new_grid[x, y] = 1
#             elif grid[x, y] == 0 and neighbors == 3:
#                 new_grid[x, y] = 1
#     return new_grid

# def generate_random_grid(rows, cols, alive_ratio):
#     """生成一个随机初始状态的网格，其中活细胞的比例由alive_ratio指定"""
#     grid = np.random.rand(rows, cols) < alive_ratio
#     return grid.astype(int)

# # 用户定义的参数
# rows, cols = 10, 10  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 生成随机初始网格
# grid = generate_random_grid(rows, cols, alive_ratio)

# # 模拟多代
# generations = 5  # 可以修改这个值来模拟更多代
# for gen in range(generations):
#     plt.figure(figsize=(5, 5))
#     plt.imshow(grid, cmap='binary')  # 使用二进制颜色映射，黑色代表1，白色代表0
#     plt.title(f"Generation {gen+1}")
#     plt.show()
#     grid = update_grid(grid)




# import numpy as np
# import matplotlib.pyplot as plt

# def count_neighbors(grid, x, y, rows, cols):
#     count = np.zeros((3,), dtype=int)
#     for i in range(max(0, x-1), min(x+2, rows)):
#         for j in range(max(0, y-1), min(y+2, cols)):
#             if (i, j) != (x, y):
#                 color = grid[i, j]
#                 if color != 0:
#                     count[color - 1] += 1
#     return count

# def update_grid(grid):
#     rows, cols = grid.shape
#     new_grid = np.copy(grid)
    
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y, rows, cols)
#             if grid[x, y] != 0:
#                 if np.sum(neighbors == grid[x, y] - 1) in [2, 3]:
#                     new_grid[x, y] = grid[x, y]
#                 else:
#                     new_grid[x, y] = 0
#             else:
#                 max_color = np.argmax(neighbors)
#                 if neighbors[max_color] == 3:
#                     new_grid[x, y] = max_color + 1
#                 elif np.any(neighbors == 1) and np.sum(neighbors) == 3:
#                     new_grid[x, y] = np.argmin(neighbors) + 1
    
#     # Equilibrium mechanism
#     color_counts = np.sum(new_grid != 0, axis=0)
#     max_count = np.max(color_counts)
#     if max_count > (rows * cols) / 2:
#         for x in range(rows):
#             for y in range(cols):
#                 if new_grid[x, y] != 0 and color_counts[new_grid[x, y] - 1] > (rows * cols) / 2:
#                     new_grid[x, y] = 0
    
#     return new_grid

# def generate_random_grid(rows, cols, alive_ratio):
#     grid = np.random.randint(4, size=(rows, cols))  # 0-3
#     grid[np.random.rand(rows, cols) < alive_ratio] = 0
#     return grid

# # 用户定义的参数
# rows, cols = 10, 10  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 生成随机初始网格
# grid = generate_random_grid(rows, cols, alive_ratio)

# # 模拟多代
# generations = 5  # 可以修改这个值来模拟更多代
# for gen in range(generations):
#     plt.figure(figsize=(5, 5))
#     colors = ['white', 'red', 'green', 'blue']
#     plt.imshow(grid, cmap=plt ListedColormap(colors))
#     plt.title(f"Generation {gen+1}")
#     plt.show()
#     grid = update_grid(grid)





# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap

# def count_neighbors(grid, x, y, rows, cols):
#     count = np.zeros((4,), dtype=int)  # 0: empty, 1: red, 2: green, 3: blue
#     for i in range(max(0, x-1), min(x+2, rows)):
#         for j in range(max(0, y-1), min(y+2, cols)):
#             if (i, j) != (x, y):
#                 cell_color = grid[i, j]
#                 if cell_color != 0:
#                     count[cell_color] += 1
#     return count

# def update_grid(grid):
#     rows, cols = grid.shape
#     new_grid = np.copy(grid).astype(int)
    
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y, rows, cols)
#             if grid[x, y] != 0:
#                 same_color_neighbors = neighbors[grid[x, y]]
#                 if same_color_neighbors < 2 or same_color_neighbors > 3:
#                     new_grid[x, y] = 0
#                 elif np.sum(neighbors[1:]) == 3 and same_color_neighbors == 2:
#                     new_grid[x, y] = 1 + np.argmax(neighbors[1:])  # Change to the minority color
#             else:
#                 if neighbors[1] == 3:
#                     new_grid[x, y] = 1
#                 elif neighbors[2] == 3:
#                     new_grid[x, y] = 2
#                 elif neighbors[3] == 3:
#                     new_grid[x, y] = 3
#                 elif np.sum(neighbors[1:]) == 3:
#                     new_grid[x, y] = 1 + np.argmin(neighbors[1:])  # Become the minority color
    
#     # Equilibrium mechanism
#     color_counts = np.sum(new_grid != 0, axis=None)
#     max_count = np.max(color_counts)
#     if max_count > (rows * cols) / 2:
#         for x in range(rows):
#             for y in range(cols):
#                 if new_grid[x, y] != 0 and color_counts[new_grid[x, y] - 1] > (rows * cols) / 2:
#                     new_grid[x, y] = 0
    
#     return new_grid

# def generate_random_grid(rows, cols, alive_ratio):
#     grid = np.random.randint(4, size=(rows, cols))  # 0-3
#     grid[np.random.rand(rows, cols) < alive_ratio] = 0
#     return grid

# # 用户定义的参数
# rows, cols = 50, 50  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 生成随机初始网格
# grid = generate_random_grid(rows, cols, alive_ratio)

# # 模拟多代
# generations = 20  # 可以修改这个值来模拟更多代
# colors = ['white', 'red', 'green', 'blue']
# colormap = ListedColormap(colors)

# for gen in range(generations):
#     plt.figure(figsize=(5, 5))
#     plt.imshow(grid, cmap=colormap)
#     plt.title(f"Generation {gen+1}")
#     plt.show()
#     grid = update_grid(grid)





# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap

# def count_neighbors(grid, x, y, rows, cols):
#     count = np.zeros((4,), dtype=int)  # 0: empty, 1: red, 2: green, 3: blue
#     for i in range(max(0, x-1), min(x+2, rows)):
#         for j in range(max(0, y-1), min(y+2, cols)):
#             if (i, j) != (x, y):
#                 cell_color = grid[i, j]
#                 if cell_color != 0:
#                     count[cell_color] += 1
#     return count

# def apply_gravity(grid):
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
    
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] != 0:
#                 for dy in range(1, rows - x):
#                     nx, ny = x + dy, y
#                     if grid[nx, ny] == 0:
#                         grid[nx, ny] = grid[x, y]
#                         grid[x, y] = 0
#                         break
#     return grid

# def update_grid(grid):
#     rows, cols = grid.shape
#     new_grid = np.copy(grid).astype(int)
    
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y, rows, cols)
#             if grid[x, y] != 0:
#                 same_color_neighbors = neighbors[grid[x, y]]
#                 if same_color_neighbors < 2 or same_color_neighbors > 3:
#                     new_grid[x, y] = 0
#                 elif np.sum(neighbors[1:]) == 3 and same_color_neighbors == 2:
#                     new_grid[x, y] = 1 + np.argmax(neighbors[1:])  # Change to the minority color
#             else:
#                 if neighbors[1] == 3:
#                     new_grid[x, y] = 1
#                 elif neighbors[2] == 3:
#                     new_grid[x, y] = 2
#                 elif neighbors[3] == 3:
#                     new_grid[x, y] = 3
#                 elif np.sum(neighbors[1:]) == 3:
#                     new_grid[x, y] = 1 + np.argmin(neighbors[1:])  # Become the minority color
    
#     return new_grid

# def generate_random_grid(rows, cols, alive_ratio):
#     grid = np.random.randint(4, size=(rows, cols))  # 0-3
#     grid[np.random.rand(rows, cols) < alive_ratio] = 0
#     return grid

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 生成随机初始网格
# grid = generate_random_grid(rows, cols, alive_ratio)

# # 模拟多代
# generations = 5  # 可以修改这个值来模拟更多代
# colors = ['white', 'red', 'green', 'blue']
# colormap = ListedColormap(colors)

# for gen in range(generations):
#     plt.figure(figsize=(10, 6))
#     plt.imshow(grid, cmap=colormap)
#     plt.title(f"Generation {gen+1}")
#     plt.show()
#     grid = apply_gravity(grid)
#     grid = update_grid(grid)



# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from matplotlib.animation import FuncAnimation

# def count_neighbors(grid, x, y, rows, cols):
#     count = np.zeros((4,), dtype=int)  # 0: empty, 1: red, 2: green, 3: blue
#     for i in range(max(0, x-1), min(x+2, rows)):
#         for j in range(max(0, y-1), min(y+2, cols)):
#             if (i, j) != (x, y):
#                 cell_color = grid[i, j]
#                 if cell_color != 0:
#                     count[cell_color] += 1
#     return count

# def apply_gravity(grid):
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
    
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] != 0:
#                 for dy in range(1, rows):
#                     nx, ny = x, y + dy
#                     if nx < rows and ny < cols and grid[nx, ny] == 0:
#                         grid[nx, ny] = grid[x, y]
#                         grid[x, y] = 0
#                         break
#     return grid

# def update_grid(grid):
#     rows, cols = grid.shape
#     new_grid = np.copy(grid).astype(int)
    
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y, rows, cols)
#             if grid[x, y] != 0:
#                 same_color_neighbors = neighbors[grid[x, y]]
#                 if same_color_neighbors < 2 or same_color_neighbors > 3:
#                     new_grid[x, y] = 0
#             else:
#                 if neighbors[1] == 3:
#                     new_grid[x, y] = 1
#                 elif neighbors[2] == 3:
#                     new_grid[x, y] = 2
#                 elif neighbors[3] == 3:
#                     new_grid[x, y] = 3
#                 elif np.sum(neighbors[1:]) == 3:
#                     new_grid[x, y] = 1 + np.argmin(neighbors[1:])  # Become the minority color
    
#     return new_grid

# def generate_random_grid(rows, cols, alive_ratio):
#     grid = np.random.randint(4, size=(rows, cols))  # 0-3
#     grid[np.random.rand(rows, cols) < alive_ratio] = 0
#     return grid

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 生成随机初始网格
# grid = generate_random_grid(rows, cols, alive_ratio)

# # 定义颜色映射
# colors = ['white', 'red', 'green', 'blue']
# colormap = ListedColormap(colors)

# # 设置图形
# fig, ax = plt.subplots()
# img = ax.imshow(grid, cmap=colormap)
# ax.set_title("Generation 0")
# ax.axis('off')

# def update(frame):
#     global grid
#     grid = apply_gravity(grid)
#     grid = update_grid(grid)
#     img.set_data(grid)
#     ax.set_title(f"Generation {frame}")
#     return img,

# # 创建动画
# ani = FuncAnimation(fig, update, frames=10, interval=500, blit=True)

# plt.show()


# 



# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from matplotlib.animation import FuncAnimation

# # 定义颜色映射
# colors = ['white', 'red', 'green', 'blue']
# colormap = ListedColormap(colors)

# def initialize_grid(rows, cols, alive_ratio):
#     """初始化网格，随机分布活细胞和空白"""
#     grid = np.zeros((rows, cols), dtype=int)
#     grid[np.random.rand(rows, cols) < alive_ratio] = np.random.choice([1, 2, 3], size=(rows*alive_ratio*cols,))
#     return grid

# def count_neighbors(grid, x, y):
#     """计算活细胞邻居数量"""
#     neighbors = np.sum(grid[max(0, x-1):min(grid.shape[0], x+2), max(0, y-1):min(grid.shape[1], y+2)])
#     return neighbors

# def update_grid(grid):
#     """根据生命游戏规则更新网格"""
#     new_grid = grid.copy()
#     for x in range(grid.shape[0]):
#         for y in range(grid.shape[1]):
#             neighbors = count_neighbors(grid, x, y)
#             if grid[x, y] == 0:
#                 if neighbors == 3:
#                     new_grid[x, y] = np.random.choice([1, 2, 3])  # 随机选择一个颜色
#             else:
#                 if neighbors < 2 or neighbors > 3:
#                     new_grid[x, y] = 0
#                 elif neighbors == 2:
#                     new_grid[x, y] = grid[x, y]  # 保持原样
#                 elif neighbors == 3:
#                     new_grid[x, y] = grid[x, y]  # 保持原样
#     return new_grid

# def ensure_all_colors(grid):
#     """确保三种颜色都存在"""
#     for color in range(1, 4):
#         if np.sum(grid == color) == 0:
#             empty_cells = np.where(grid == 0)
#             if len(empty_cells[0]) > 0:
#                 grid[empty_cells[0][0], empty_cells[1][0]] = color
#     return grid

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 初始化网格
# grid = initialize_grid(rows, cols, alive_ratio)

# # 设置图形
# fig, ax = plt.subplots()
# img = ax.imshow(grid, cmap=colormap)
# ax.set_title("Generation 0")
# ax.axis('off')

# def update(frame):
#     global grid
#     grid = update_grid(grid)
#     grid = ensure_all_colors(grid)
#     img.set_array(grid)
#     ax.set_title(f"Generation {frame}")
#     return img,

# # 创建动画
# ani = FuncAnimation(fig, update, frames=20, interval=200, repeat=False)

# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from matplotlib.animation import FuncAnimation

# # 定义颜色映射
# colors = ['white', 'red', 'green', 'blue']
# colormap = ListedColormap(colors)

# def initialize_grid(rows, cols, alive_ratio):
#     """初始化网格，随机分布活细胞和空白"""
#     grid = np.zeros((rows, cols), dtype=int)
#     for _ in range(int(alive_ratio * rows * cols)):
#         row = np.random.randint(0, rows)
#         col = np.random.randint(0, cols)
#         grid[row, col] = np.random.choice([1, 2, 3])  # 随机选择一个颜色
#     return grid

# def count_neighbors(grid, x, y):
#     """计算活细胞邻居数量"""
#     neighbors = np.sum(grid[max(0, x-1):min(grid.shape[0], x+2), max(0, y-1):min(grid.shape[1], y+2)])
#     return neighbors

# def update_grid(grid):
#     """根据生命游戏规则更新网格"""
#     new_grid = grid.copy()
#     for x in range(grid.shape[0]):
#         for y in range(grid.shape[1]):
#             neighbors = count_neighbors(grid, x, y)
#             if grid[x, y] == 0:
#                 if neighbors == 3:
#                     new_grid[x, y] = np.random.choice([1, 2, 3])  # 随机选择一个颜色
#             else:
#                 if neighbors < 2 or neighbors > 3:
#                     new_grid[x, y] = 0
#                 elif neighbors == 2 or neighbors == 3:
#                     new_grid[x, y] = grid[x, y]  # 保持原样
#     return new_grid

# def apply_gravity(grid):
#     """模拟重力影响，使细胞向下移动"""
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] != 0:
#                 for dy in range(1, rows - x):
#                     nx, ny = x, y + dy
#                     if nx < rows and ny < cols and grid[nx, ny] == 0:
#                         grid[nx, ny] = grid[x, y]
#                         grid[x, y] = 0
#                         break
#     return grid

# def ensure_all_colors(grid):
#     """确保三种颜色都存在"""
#     for color in range(1, 4):
#         if np.sum(grid == color) == 0:
#             empty_cells = np.where(grid == 0)
#             if len(empty_cells[0]) > 0:
#                 grid[empty_cells[0][0], empty_cells[1][0]] = color
#     return grid

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 初始化网格
# grid = initialize_grid(rows, cols, alive_ratio)

# # 设置图形
# fig, ax = plt.subplots()
# img = ax.imshow(grid, cmap=colormap)
# ax.set_title("Generation 0")
# ax.axis('off')

# def update(frame):
#     global grid
#     grid = apply_gravity(grid)
#     grid = update_grid(grid)
#     grid = ensure_all_colors(grid)
#     img.set_array(grid)
#     ax.set_title(f"Generation {frame}")
#     return img,

# # 创建动画
# ani = FuncAnimation(fig, update, frames=20, interval=200, repeat=False)

# plt.show()




# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from matplotlib.animation import FuncAnimation

# # 定义颜色映射
# colors = ['white', 'red', 'green', 'blue']
# colormap = ListedColormap(colors)

# def initialize_grid(rows, cols, alive_ratio):
#     """初始化网格，随机分布活细胞和空白"""
#     grid = np.zeros((rows, cols), dtype=int)
#     for _ in range(int(alive_ratio * rows * cols)):
#         row = np.random.randint(0, rows)
#         col = np.random.randint(0, cols)
#         grid[row, col] = np.random.choice([1, 2, 3])  # 随机选择一个颜色
#     return grid

# def count_neighbors(grid, x, y):
#     """计算活细胞邻居数量，并记录每种颜色的邻居数量"""
#     neighbors = np.array([0, 0, 0, 0])  # 0: empty, 1: red, 2: green, 3: blue
#     for i in range(max(0, x-1), min(grid.shape[0], x+2)):
#         for j in range(max(0, y-1), min(grid.shape[1], y+2)):
#             if (i, j) != (x, y):
#                 cell = grid[i, j]
#                 if cell != 0:
#                     neighbors[cell] += 1
#     return neighbors

# def update_grid(grid):
#     """根据生命游戏规则更新网格"""
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y)
#             if grid[x, y] != 0:
#                 if neighbors[grid[x, y]] < 2 or neighbors[grid[x, y]] > 3:
#                     new_grid[x, y] = 0
#                 else:
#                     new_grid[x, y] = grid[x, y]
#             else:
#                 if neighbors[1] == 3:
#                     new_grid[x, y] = 1
#                 elif neighbors[2] == 3:
#                     new_grid[x, y] = 2
#                 elif neighbors[3] == 3:
#                     new_grid[x, y] = 3
#                 else:
#                     active_colors = neighbors > 0
#                     if np.any(active_colors):
#                         min_color = np.argmin(neighbors[active_colors])
#                         new_grid[x, y] = active_colors[min_color] + 1
#     return new_grid

# def apply_gravity(grid):
#     """模拟重力影响，使细胞向下移动"""
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] != 0:
#                 for dy in range(1, rows - x):
#                     nx, ny = x + dy, y
#                     if nx < rows and ny < cols and grid[nx, ny] == 0:
#                         grid[nx, ny] = grid[x, y]
#                         grid[x, y] = 0
#                         break
#     return grid

# def ensure_all_colors(grid):
#     """确保三种颜色都存在"""
#     for color in range(1, 4):
#         if np.sum(grid == color) == 0:
#             empty_cells = np.where(grid == 0)
#             if len(empty_cells[0]) > 0:
#                 grid[empty_cells[0][0], empty_cells[1][0]] = color
#     return grid

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 初始化网格
# grid = initialize_grid(rows, cols, alive_ratio)

# # 设置图形
# fig, ax = plt.subplots()
# img = ax.imshow(grid, cmap=colormap)
# ax.set_title("Generation 0")
# ax.axis('off')

# def update(frame):
#     global grid
#     grid = apply_gravity(grid)
#     grid = update_grid(grid)
#     grid = ensure_all_colors(grid)
#     img.set_array(grid)
#     ax.set_title(f"Generation {frame}")
#     return img,

# # 创建动画
# ani = FuncAnimation(fig, update, frames=10000000, interval=1000, repeat=False)

# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from matplotlib.animation import FuncAnimation

# # 定义颜色映射
# colors = ['white', 'red', 'green', 'blue']
# colormap = ListedColormap(colors)

# def initialize_grid(rows, cols, alive_ratio):
#     """初始化网格，随机分布活细胞和空白"""
#     grid = np.zeros((rows, cols), dtype=int)
#     for _ in range(int(alive_ratio * rows * cols)):
#         row = np.random.randint(0, rows)
#         col = np.random.randint(0, cols)
#         grid[row, col] = np.random.choice([1, 2, 3])  # 随机选择一个颜色
#     return grid

# def count_neighbors(grid, x, y):
#     """计算活细胞邻居数量，并记录每种颜色的邻居数量"""
#     neighbors = np.array([0, 0, 0, 0])  # 0: empty, 1: red, 2: green, 3: blue
#     for i in range(max(0, x-1), min(grid.shape[0], x+2)):
#         for j in range(max(0, y-1), min(grid.shape[1], y+2)):
#             if (i, j) != (x, y):
#                 cell = grid[i, j]
#                 if cell != 0:
#                     neighbors[cell] += 1
#     return neighbors

# def update_grid(grid):
#     """根据生命游戏规则更新网格"""
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y)
#             if grid[x, y] != 0:
#                 if neighbors[grid[x, y]] < 2 or neighbors[grid[x, y]] > 3:
#                     new_grid[x, y] = 0
#                 else:
#                     new_grid[x, y] = grid[x, y]
#             else:
#                 if neighbors[1] == 3:
#                     new_grid[x, y] = 1
#                 elif neighbors[2] == 3:
#                     new_grid[x, y] = 2
#                 elif neighbors[3] == 3:
#                     new_grid[x, y] = 3
#                 else:
#                     active_colors = neighbors > 0
#                     if np.any(active_colors):
#                         min_color = np.argmin(neighbors[active_colors])
#                         new_grid[x, y] = active_colors[min_color] + 1
#     return new_grid

# def apply_gravity(grid):
#     """模拟重力影响，使细胞向下移动"""
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] != 0:
#                 for dy in range(1, rows - x):
#                     nx, ny = x + dy, y
#                     if nx < rows and ny < cols and grid[nx, ny] == 0:
#                         grid[nx, ny] = grid[x, y]
#                         grid[x, y] = 0
#                         break
#     return grid

# def ensure_all_colors(grid):
#     """确保三种颜色都存在"""
#     for color in range(1, 4):
#         if np.sum(grid == color) == 0:
#             empty_cells = np.where(grid == 0)
#             if len(empty_cells[0]) > 0:
#                 grid[empty_cells[0][0], empty_cells[1][0]] = color
#     return grid

# def create_wave_effect(grid, new_grid):
#     """创建波纹效果"""
#     wave_grid = new_grid.copy()
#     for x in range(grid.shape[0]):
#         for y in range(grid.shape[1]):
#             if grid[x, y] != new_grid[x, y] and new_grid[x, y] != 0:
#                 wave_grid[x, y] = 4  # 临时状态，表示波纹
#     return wave_grid

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 初始化网格
# grid = initialize_grid(rows, cols, alive_ratio)

# # 设置图形
# fig, ax = plt.subplots()
# img = ax.imshow(grid, cmap=colormap)
# ax.set_title("Generation 0")
# ax.axis('off')

# def update(frame):
#     global grid
#     new_grid = apply_gravity(grid)
#     new_grid = update_grid(new_grid)
#     new_grid = ensure_all_colors(new_grid)
#     wave_grid = create_wave_effect(grid, new_grid)
#     grid = new_grid
#     img.set_array(wave_grid)
#     ax.set_title(f"Generation {frame}")
#     return img,

# # 创建动画
# ani = FuncAnimation(fig, update, frames=1000000, interval=1000, repeat=False)

# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from matplotlib.animation import FuncAnimation

# # 定义颜色映射
# colors = ['white', 'red', 'green', 'blue', 'yellow']  # 添加一个中间状态（黄色）
# colormap = ListedColormap(colors)

# def initialize_grid(rows, cols, alive_ratio):
#     """初始化网格，随机分布活细胞和空白"""
#     grid = np.zeros((rows, cols), dtype=int)
#     for _ in range(int(alive_ratio * rows * cols)):
#         row = np.random.randint(0, rows)
#         col = np.random.randint(0, cols)
#         grid[row, col] = np.random.choice([1, 2, 3])  # 随机选择一个颜色
#     return grid

# def count_neighbors(grid, x, y):
#     """计算活细胞邻居数量，并记录每种颜色的邻居数量"""
#     neighbors = np.array([0, 0, 0, 0])  # 0: empty, 1: red, 2: green, 3: blue
#     for i in range(max(0, x-1), min(grid.shape[0], x+2)):
#         for j in range(max(0, y-1), min(grid.shape[1], y+2)):
#             if (i, j) != (x, y):
#                 cell = grid[i, j]
#                 if cell != 0:
#                     neighbors[cell-1] += 1
#     return neighbors

# def update_grid(grid):
#     """根据生命游戏规则更新网格"""
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y)
#             if grid[x, y] != 0:
#                 if neighbors[grid[x, y]-1] < 2 or neighbors[grid[x, y]-1] > 3:
#                     new_grid[x, y] = 0
#                 else:
#                     new_grid[x, y] = grid[x, y]
#             else:
#                 total_active = np.sum(neighbors)
#                 if total_active == 3:
#                     min_index = np.argmin(neighbors)
#                     new_grid[x, y] = min_index + 1
#                 elif total_active > 3:
#                     new_grid[x, y] = 0
#     return new_grid

# def apply_gravity(grid):
#     """模拟重力影响，使细胞向下移动"""
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] != 0:
#                 found = False
#                 for dy in range(1, rows):
#                     nx, ny = x, y + dy
#                     if nx < rows and ny < cols and grid[nx, ny] == 0:
#                         new_grid[nx, ny] = grid[x, y]
#                         found = True
#                         break
#                 if not found:
#                     new_grid[x, y] = grid[x, y]
#     return new_grid

# def create_wave_effect(grid, new_grid):
#     """创建波纹效果"""
#     wave_grid = grid.copy()
#     for x in range(grid.shape[0]):
#         for y in range(grid.shape[1]):
#             if grid[x, y] != new_grid[x, y] and new_grid[x, y] != 0:
#                 wave_grid[x, y] = 4  # 临时状态，表示波纹（黄色）
#     return wave_grid

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 初始化网格
# grid = initialize_grid(rows, cols, alive_ratio)

# # 设置图形
# fig, ax = plt.subplots()
# img = ax.imshow(grid, cmap=colormap)
# ax.set_title("Generation 0")
# ax.axis('off')

# def update(frame):
#     global grid
#     new_grid = apply_gravity(grid)
#     new_grid = update_grid(new_grid)
#     wave_grid = create_wave_effect(grid, new_grid)
#     grid = new_grid
#     img.set_array(wave_grid)
#     ax.set_title(f"Generation {frame}")
#     return img,

# # 创建动画
# ani = FuncAnimation(fig, update, frames=20, interval=200, repeat=False)

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from matplotlib.animation import FuncAnimation

# # 定义颜色映射
# colors = ['white', 'red', 'green', 'blue']
# colormap = ListedColormap(colors)

# def initialize_grid(rows, cols, alive_ratio):
#     """初始化网格，随机分布活细胞和空白"""
#     grid = np.zeros((rows, cols), dtype=int)
#     for _ in range(int(alive_ratio * rows * cols)):
#         row = np.random.randint(0, rows)
#         col = np.random.randint(0, cols)
#         grid[row, col] = np.random.choice([1, 2, 3])  # 随机选择一个颜色
#     return grid

# def count_neighbors(grid, x, y):
#     """计算活细胞邻居数量，并记录每种颜色的邻居数量"""
#     neighbors = np.array([0, 0, 0, 0])  # 0: empty, 1: red, 2: green, 3: blue
#     for i in range(max(0, x-1), min(grid.shape[0], x+2)):
#         for j in range(max(0, y-1), min(grid.shape[1], y+2)):
#             if (i, j) != (x, y):
#                 cell = grid[i, j]
#                 if cell != 0:
#                     neighbors[cell-1] += 1
#     return neighbors

# def update_grid(grid):
#     """根据生命游戏规则更新网格"""
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y)
#             if grid[x, y] != 0:
#                 if neighbors[grid[x, y]-1] < 2 or neighbors[grid[x, y]-1] > 3:
#                     new_grid[x, y] = 0
#                 else:
#                     new_grid[x, y] = grid[x, y]
#             else:
#                 if neighbors[0] == 3:
#                     new_grid[x, y] = 1
#                 elif neighbors[1] == 3:
#                     new_grid[x, y] = 2
#                 elif neighbors[2] == 3:
#                     new_grid[x, y] = 3
#                 else:
#                     active_colors = neighbors > 0
#                     if np.any(active_colors):
#                         min_color = np.argmin(neighbors[active_colors])
#                         new_grid[x, y] = (active_colors[min_color] + 1)
#     return new_grid

# def apply_gravity(grid):
#     """模拟重力影响，使细胞向下移动"""
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] != 0:
#                 for dy in range(1, rows):
#                     nx, ny = x, y + dy
#                     if nx < rows and ny < cols and grid[nx, ny] == 0:
#                         new_grid[nx, ny] = grid[x, y]
#                         break
#     return new_grid

# def ensure_all_colors(grid):
#     """确保三种颜色都存在"""
#     for color in range(1, 4):
#         if np.sum(grid == color) == 0:
#             empty_cells = np.where(grid == 0)
#             if len(empty_cells[0]) > 0:
#                 grid[empty_cells[0][0], empty_cells[1][0]] = color
#     return grid

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 初始化网格
# grid = initialize_grid(rows, cols, alive_ratio)

# # 设置图形
# fig, ax = plt.subplots()
# img = ax.imshow(grid, cmap=colormap)
# ax.set_title("Generation 0")
# ax.axis('off')

# def update(frame):
#     global grid
#     new_grid = apply_gravity(grid)
#     new_grid = update_grid(new_grid)
#     grid = ensure_all_colors(new_grid)
#     img.set_array(grid)
#     ax.set_title(f"Generation {frame}")
#     return img,

# # 创建动画
# ani = FuncAnimation(fig, update, frames=20, interval=200, repeat=False)

# plt.show()




# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap

# def count_neighbors(grid, x, y, rows, cols):
#     count = np.zeros((4,), dtype=int)  # 0: empty, 1: red, 2: green, 3: blue
#     for i in range(max(0, x-1), min(x+2, rows)):
#         for j in range(max(0, y-1), min(y+2, cols)):
#             if (i, j) != (x, y):
#                 cell_color = grid[i, j]
#                 if cell_color != 0:
#                     count[cell_color] += 1
#     return count

# def apply_gravity(grid):
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
    
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] != 0:
#                 for dy in range(1, rows - x):
#                     nx, ny = x + dy, y
#                     if grid[nx, ny] == 0:
#                         grid[nx, ny] = grid[x, y]
#                         grid[x, y] = 0
#                         break
#     return grid

# def update_grid(grid):
#     rows, cols = grid.shape
#     new_grid = np.copy(grid).astype(int)
    
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y, rows, cols)
#             if grid[x, y] != 0:
#                 same_color_neighbors = neighbors[grid[x, y]]
#                 if same_color_neighbors < 2 or same_color_neighbors > 3:
#                     new_grid[x, y] = 0
#                 elif np.sum(neighbors[1:]) == 3 and same_color_neighbors == 2:
#                     new_grid[x, y] = 1 + np.argmax(neighbors[1:])  # Change to the minority color
#             else:
#                 if neighbors[1] == 3:
#                     new_grid[x, y] = 1
#                 elif neighbors[2] == 3:
#                     new_grid[x, y] = 2
#                 elif neighbors[3] == 3:
#                     new_grid[x, y] = 3
#                 elif np.sum(neighbors[1:]) == 3:
#                     new_grid[x, y] = 1 + np.argmin(neighbors[1:])  # Become the minority color
    
#     return new_grid

# def generate_random_grid(rows, cols, alive_ratio):
#     grid = np.random.randint(4, size=(rows, cols))  # 0-3
#     grid[np.random.rand(rows, cols) < alive_ratio] = 0
#     return grid

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 生成随机初始网格
# grid = generate_random_grid(rows, cols, alive_ratio)

# # 模拟多代
# generations = 5  # 可以修改这个值来模拟更多代
# colors = ['white', 'red', 'green', 'blue']
# colormap = ListedColormap(colors)

# for gen in range(generations):
#     plt.figure(figsize=(10, 6))
#     plt.imshow(grid, cmap=colormap)
#     plt.title(f"Generation {gen+1}")
#     plt.show()
#     grid = apply_gravity(grid)
#     grid = update_grid(grid)

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from matplotlib.animation import FuncAnimation

# def count_neighbors(grid, x, y, rows, cols):
#     count = np.zeros((4,), dtype=int)  # 0: empty, 1: red, 2: green, 3: blue
#     for i in range(max(0, x-1), min(x+2, rows)):
#         for j in range(max(0, y-1), min(y+2, cols)):
#             if (i, j) != (x, y):
#                 cell_color = grid[i, j]
#                 if cell_color != 0:
#                     count[cell_color] += 1
#     return count

# def apply_gravity(grid):
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
    
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] != 0:
#                 for dy in range(1, rows - x):
#                     nx, ny = x + dy, y
#                     if grid[nx, ny] == 0:
#                         grid[nx, ny] = grid[x, y]
#                         grid[x, y] = 0
#                         break
#     return grid

# def update_grid(grid):
#     rows, cols = grid.shape
#     new_grid = np.copy(grid).astype(int)
    
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y, rows, cols)
#             if grid[x, y] != 0:
#                 same_color_neighbors = neighbors[grid[x, y]]
#                 if same_color_neighbors < 2 or same_color_neighbors > 3:
#                     new_grid[x, y] = 0
#                 elif np.sum(neighbors[1:]) == 3 and same_color_neighbors == 2:
#                     new_grid[x, y] = 1 + np.argmax(neighbors[1:])  # Change to the minority color
#             else:
#                 if neighbors[1] == 3:
#                     new_grid[x, y] = 1
#                 elif neighbors[2] == 3:
#                     new_grid[x, y] = 2
#                 elif neighbors[3] == 3:
#                     new_grid[x, y] = 3
#                 elif np.sum(neighbors[1:]) == 3:
#                     new_grid[x, y] = 1 + np.argmin(neighbors[1:])  # Become the minority color
    
#     return new_grid

# def generate_random_grid(rows, cols, alive_ratio):
#     grid = np.random.randint(4, size=(rows, cols))  # 0-3
#     grid[np.random.rand(rows, cols) < alive_ratio] = 0
#     return grid

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 生成随机初始网格
# grid = generate_random_grid(rows, cols, alive_ratio)

# # 定义颜色映射
# colors = ['white', 'red', 'green', 'blue']
# colormap = ListedColormap(colors)

# # 设置图形
# fig, ax = plt.subplots()
# img = ax.imshow(grid, cmap=colormap)
# ax.set_title("Generation 0")
# ax.axis('off')

# def update(frame):
#     global grid
#     grid = apply_gravity(grid)
#     grid = update_grid(grid)
#     img.set_array(grid)
#     ax.set_title(f"Generation {frame+1}")
#     return img,

# # 创建动画
# ani = FuncAnimation(fig, update, frames=range(5), interval=500, repeat=False)

# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from matplotlib.animation import FuncAnimation

# def count_neighbors(grid, x, y, rows, cols):
#     count = 0
#     for i in range(max(0, x-1), min(x+2, rows)):
#         for j in range(max(0, y-1), min(y+2, cols)):
#             if (i, j) != (x, y):
#                 count += grid[i, j]
#     return count

# def update_grid(grid):
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y, rows, cols)
#             if grid[x, y] == 1:  # Cell is alive
#                 if (neighbors == 2) or (neighbors == 3):
#                     new_grid[x, y] = 1
#                 else:
#                     new_grid[x, y] = 0
#             else:  # Cell is dead
#                 if neighbors == 3:
#                     new_grid[x, y] = 1
#     return new_grid

# def apply_gravity(grid):
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] == 1:
#                 for dy in range(1, rows):
#                     nx, ny = x, y + dy
#                     if (nx < rows) and (ny < cols) and (grid[nx, ny] == 0):
#                         new_grid[nx, ny] = 1
#                         break
#     return new_grid

# def generate_random_grid(rows, cols, alive_ratio):
#     grid = np.random.rand(rows, cols) < alive_ratio
#     return grid.astype(int)

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 生成随机初始网格
# grid = generate_random_grid(rows, cols, alive_ratio)

# # 定义颜色映射
# colors = ['white', 'black']
# colormap = ListedColormap(colors)

# # 设置图形
# fig, ax = plt.subplots()
# img = ax.imshow(grid, cmap=colormap)
# ax.set_title("Generation 0")
# ax.axis('off')

# def update(frame):
#     global grid
#     grid = apply_gravity(grid)
#     grid = update_grid(grid)
#     img.set_array(grid)
#     ax.set_title(f"Generation {frame+1}")
#     return img,

# # 创建动画
# ani = FuncAnimation(fig, update, frames=range(5), interval=500, repeat=False)

# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from matplotlib.animation import FuncAnimation

# def count_neighbors(grid, x, y, rows, cols):
#     count = 0
#     for i in range(max(0, x-1), min(x+2, rows)):
#         for j in range(max(0, y-1), min(y+2, cols)):
#             if (i, j) != (x, y):
#                 count += grid[i, j]
#     return count

# def update_grid(grid):
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y, rows, cols)
#             if grid[x, y] == 1:  # Cell is alive
#                 if neighbors < 2 or neighbors > 3:
#                     new_grid[x, y] = 0
#                 else:
#                     new_grid[x, y] = 1
#             else:  # Cell is dead
#                 if neighbors == 3:
#                     new_grid[x, y] = 1
#     return new_grid

# def apply_gravity(grid):
#     # Gravity is not well-defined in a 2D grid for this kind of simulation
#     # This function is left empty to focus on the life game dynamics
#     return grid

# def generate_random_grid(rows, cols, alive_ratio):
#     grid = np.random.rand(rows, cols) < alive_ratio
#     return (grid * 3).astype(int) + 1  # Randomly assign a color from 1 to 3

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 生成随机初始网格
# grid = generate_random_grid(rows, cols, alive_ratio)

# # 定义颜色映射
# colors = ['white', 'red', 'green', 'blue']
# colormap = ListedColormap(colors)

# # 设置图形
# fig, ax = plt.subplots()
# img = ax.imshow(grid, cmap=colormap)
# ax.set_title("Generation 0")
# ax.axis('off')

# def update(frame):
#     global grid
#     grid = update_grid(grid)
#     img.set_array(grid)
#     ax.set_title(f"Generation {frame+1}")
#     return img,

# # 创建动画
# ani = FuncAnimation(fig, update, frames=range(5), interval=500, repeat=False)

# plt.show()




# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap

# def count_neighbors(grid, x, y, rows, cols):
#     count = np.zeros((4,), dtype=int)  # 0: empty, 1: red, 2: green, 3: blue
#     for i in range(max(0, x-1), min(x+2, rows)):
#         for j in range(max(0, y-1), min(y+2, cols)):
#             if (i, j) != (x, y):
#                 cell_color = grid[i, j]
#                 if cell_color != 0:
#                     count[cell_color] += 1
#     return count

# def apply_gravity(grid):
#     rows, cols = grid.shape
#     new_grid = np.zeros((rows, cols), dtype=int)
    
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] != 0:
#                 for dy in range(1, rows - x):
#                     nx, ny = x + dy, y
#                     if grid[nx, ny] == 0:
#                         grid[nx, ny] = grid[x, y]
#                         grid[x, y] = 0
#                         break
#     return grid

# def update_grid(grid):
#     rows, cols = grid.shape
#     new_grid = np.copy(grid).astype(int)
    
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y, rows, cols)
#             if grid[x, y] != 0:
#                 same_color_neighbors = neighbors[grid[x, y]]
#                 if same_color_neighbors < 2 or same_color_neighbors > 3:
#                     new_grid[x, y] = 0
#                 elif np.sum(neighbors[1:]) == 3 and same_color_neighbors == 2:
#                     new_grid[x, y] = 1 + np.argmax(neighbors[1:])  # Change to the minority color
#             else:
#                 if neighbors[1] == 3:
#                     new_grid[x, y] = 1
#                 elif neighbors[2] == 3:
#                     new_grid[x, y] = 2
#                 elif neighbors[3] == 3:
#                     new_grid[x, y] = 3
#                 elif np.sum(neighbors[1:]) == 3:
#                     new_grid[x, y] = 1 + np.argmin(neighbors[1:])  # Become the minority color
    
#     return new_grid

# def generate_random_grid(rows, cols, alive_ratio):
#     grid = np.random.randint(4, size=(rows, cols))  # 0-3
#     grid[np.random.rand(rows, cols) < alive_ratio] = 0
#     return grid

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 生成随机初始网格
# grid = generate_random_grid(rows, cols, alive_ratio)

# # 模拟多代
# generations = 5  # 可以修改这个值来模拟更多代
# colors = ['white', 'red', 'green', 'blue']
# colormap = ListedColormap(colors)

# for gen in range(generations):
#     plt.figure(figsize=(10, 6))
#     plt.imshow(grid, cmap=colormap)
#     plt.title(f"Generation {gen+1}")
#     plt.show()
#     grid = apply_gravity(grid)
#     grid = update_grid(grid)




# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from matplotlib.animation import FuncAnimation

# def count_neighbors(grid, x, y, rows, cols):
#     count = np.zeros((4,), dtype=int)  # 0: empty, 1: red, 2: green, 3: blue
#     for i in range(max(0, x-1), min(x+2, rows)):
#         for j in range(max(0, y-1), min(y+2, cols)):
#             if (i, j) != (x, y):
#                 cell_color = grid[i, j]
#                 if cell_color != 0:
#                     count[cell_color] += 1
#     return count

# def apply_gravity(grid):
#     rows, cols = grid.shape
#     new_grid = np.copy(grid)
    
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] != 0:
#                 for dy in range(1, rows):
#                     nx, ny = x, y + dy
#                     if nx < rows and ny < cols and new_grid[nx, ny] == 0:
#                         new_grid[nx, ny] = grid[x, y]
#                         grid[x, y] = 0
#                         break
#     return new_grid

# def update_grid(grid):
#     rows, cols = grid.shape
#     new_grid = np.copy(grid).astype(int)
    
#     for x in range(rows):
#         for y in range(cols):
#             neighbors = count_neighbors(grid, x, y, rows, cols)
#             if grid[x, y] != 0:
#                 same_color_neighbors = neighbors[grid[x, y]]
#                 if same_color_neighbors < 2 or same_color_neighbors > 3:
#                     new_grid[x, y] = 0
#             else:
#                 if neighbors[1] == 3:
#                     new_grid[x, y] = 1
#                 elif neighbors[2] == 3:
#                     new_grid[x, y] = 2
#                 elif neighbors[3] == 3:
#                     new_grid[x, y] = 3
#                 elif np.sum(neighbors[1:]) == 3:
#                     new_grid[x, y] = 1 + np.argmin(neighbors[1:])  # Become the minority color
    
#     return new_grid

# def regenerate_cells(grid):
#     rows, cols = grid.shape
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] == 0 and x < 3:  # Regenerate cells only in the top 3 rows
#                 grid[x, y] = np.random.choice([1, 2, 3])

# def generate_random_grid(rows, cols, alive_ratio):
#     grid = np.random.randint(4, size=(rows, cols))  # 0-3
#     grid[np.random.rand(rows, cols) < alive_ratio] = 0
#     return grid

# # 用户定义的参数
# rows, cols = 20, 30  # 网格大小
# alive_ratio = 0.2  # 初始活细胞的比例

# # 生成随机初始网格
# grid = generate_random_grid(rows, cols, alive_ratio)

# # 定义颜色映射
# colors = ['white', 'red', 'green', 'blue']
# colormap = ListedColormap(colors)

# # 设置图形
# fig, ax = plt.subplots()
# img = ax.imshow(grid, cmap=colormap)
# ax.set_title("Generation 0")
# ax.axis('off')

# def update(frame):
#     global grid
#     grid = apply_gravity(grid)
#     grid = update_grid(grid)
#     regenerate_cells(grid)
#     img.set_array(grid)
#     ax.set_title(f"Generation {frame+1}")
#     return img,

# # 创建动画
# ani = FuncAnimation(fig, update, frames=range(5), interval=500, repeat=False)

# plt.show()

############################################# 第二次作业


# num_list = input().split()
# num_list_2 = list(map(float,num_list))
# # print(num_list_2)

# num = int(input())
# query = []
# for i in range(num):
#     a_i = input()
#     query.append(a_i)

# # print(query)

# lst = []
# for i in range(num):
#     lst_1 = [m.strip() for m in query[i].split(",")]
#     lst.append(lst_1)
# # print(lst)



# for i in range(len(lst)):   
#     if lst[i][1] == "min":
        
#         if len(lst[i]) == 2:
#             print(min(num_list_2))
#         else:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 print(min(num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]))
#             else:
#                 print("Querying on empty list!")
            
#     if lst[i][1] == "max":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 print(max(num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]))
#             else:
#                 print("Querying on empty list!")
#         else:
#             print(max(num_list_2))
#     if lst[i][0] == "index" and lst[i][1] != "slice":
#         if num_list_2[int(lst[i][1])]:
#             print(num_list_2[int(lst[i][1])])
#         else:
#             print("Querying on empty list!")
#     if lst[i][0] == "index" and lst[i][1] == "slice":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 print(num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])])
#             else:
#                 print("Querying on empty list!")
#         else:
#             print(num_list_2)
#     if lst[i][1] == "all":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 num_list_3 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 print(sum(num_list_3))
#             else:
#                 print("Querying on empty list!")
#         else:
#             print(sum(num_list_2))
#     if lst[i][1] == "avg":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 num_list_4 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 avg = sum(num_list_4)/len(num_list_4)
#                 print(avg)
#             else:
#                 print("Querying on empty list!")
#         else:
#             avg = sum(num_list_2)/len(num_list_2)
#             print(avg)
#     if lst[i][1] == "asc":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 num_list_5 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 num_list_5.sort()
#                 num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])] = num_list_5
#                 print(num_list_2)
#             else:
#                 print("Querying on empty list!")
#         else:
#             num_list_2.sort()
#             print(num_list_2)
#     if lst[i][1] == "desc":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 num_list_6 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 num_list_6.sort(reverse = True)
#                 num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])] = num_list_6
#                 print(num_list_2)
#             else:
#                 print("Querying on empty list!")
#         else:
#             num_list_2.sort(reverse = True)
#             print(num_list_2)
#     if lst[i][1] == "rev":
#         if len(lst[i]) != 2:
#             if num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]:
#                 num_list_6 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 num_list_6 = num_list_6[::-1]
#                 num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]= num_list_6
#                 print(num_list_2)
#             else:
#                 print("Querying on empty list!")
#         else:
#             num_list_2 = num_list_2[::-1]
#             print(num_list_2)


    


# s = [1,4,2,3,5]
# s1 = s[1:4:2]
# s1.sort()
# s[1:4:2] = s1
# print(s)


# def process_stock_queries():
#     num_list = input().split()
#     num_list_2 = list(map(float, num_list))

#     num_queries = int(input())
#     results = []

#     for _ in range(num_queries):
#         query = input().split(',')
#         operation = query[1]
#         start_index = int(query[2]) if len(query) > 2 else None
#         end_index = int(query[3]) if len(query) > 3 else None
#         step = int(query[4]) if len(query) > 4 else None

#         if operation == "min":
#             result = find_min_max(num_list_2, start_index, end_index, step, "min")
#         elif operation == "max":
#             result = find_min_max(num_list_2, start_index, end_index, step, "max")
#         elif operation == "index":
#             result = get_index(num_list_2, start_index)
#         elif operation == "slice":
#             result = get_slice_list(num_list_2, start_index, end_index, step)
#         elif operation == "compute":
#             if query[2] == "avg":
#                 result = compute_avg(num_list_2, start_index, end_index, step)
#             elif query[2] == "all":
#                 result = compute_all(num_list_2, start_index, end_index, step)
#         elif operation == "reorder":
#             if query[2] in ["asc", "desc", "rev"]:
#                 result = reorder_list(num_list_2, start_index, end_index, step, query[2])

#         if result is None:
#             results.append("Querying on empty list!")
#         else:
#             results.append(str(result))

#     for result in results:
#         print(result)

# def find_min_max(num_list, start_index, end_index, step, operation):
#     if start_index is None or end_index is None or step is None:
#         return getattr(min_max, operation)(num_list)
#     sliced_list = num_list[start_index:end_index:step]
#     if not sliced_list:
#         return None
#     return getattr(min_max, operation)(sliced_list)

# def get_index(num_list, index):
#     if index < 0 or index >= len(num_list):
#         return None
#     return num_list[index]

# def get_slice_list(num_list, start_index, end_index, step):
#     if start_index is None or end_index is None or step is None:
#         return num_list
#     sliced_list = num_list[start_index:end_index:step]
#     if not sliced_list:
#         return None
#     return sliced_list

# def compute_avg(num_list, start_index, end_index, step):
#     if start_index is None or end_index is None or step is None:
#         return sum(num_list) / len(num_list)
#     sliced_list = num_list[start_index:end_index:step]
#     if not sliced_list:
#         return None
#     return sum(sliced_list) / len(sliced_list)

# def compute_all(num_list, start_index, end_index, step):
#     if start_index is None or end_index is None or step is None:
#         return sum(num_list)
#     sliced_list = num_list[start_index:end_index:step]
#     if not sliced_list:
#         return None
#     return sum(sliced_list)

# def reorder_list(num_list, start_index, end_index, step, order):
#     if start_index is None or end_index is None or step is None:
#         return sort_list(num_list, order)
#     sliced_list = num_list[start_index:end_index:step]
#     if not sliced_list:
#         return None
#     return sort_list(sliced_list, order)

# def sort_list(list_to_sort, order):
#     if order == "asc":
#         return sorted(list_to_sort)
#     elif order == "desc":
#         return sorted(list_to_sort, reverse=True)
#     elif order == "rev":
#         return list_to_sort[::-1]

# class min_max:
#     @staticmethod
#     def min(lst):
#         return min(lst)

#     @staticmethod
#     def max(lst):
#         return max(lst)

# process_stock_queries()

# def safe_slice(num_list, start_index, end_index, step):
#     # 检查步长是否为0，避免无限循环
#     if step == 0:
#         return "Step cannot be zero!"
#     # 检查索引是否在合理范围内
#     if start_index < 0 or end_index > len(num_list) or start_index >= end_index:
#         return "Invalid indices!"
#     # 执行切片操作
#     return num_list[start_index:end_index:step]
 # sliced_list = safe_slice(num_list, start_index, end_index, step)
        # if isinstance(sliced_list, str):
        #     print(sliced_list)
        #     return
        # if not sliced_list:
        #     print("Querying on empty list!")
        #     return
# def process_query(num_list, query):
#     operation = query[1]
#     if len(query) > 2:
#         start_index = int(query[2])
#         end_index = int(query[3])
#         step = int(query[4])
#         sliced_list = num_list[start_index:end_index:step]
#         if operation == "min":
#             print(min(sliced_list))
#         elif operation == "max":
#             print(max(sliced_list))
#         elif operation == "avg":
#             avg = sum(sliced_list) / len(sliced_list)
#             print(avg)
#         elif operation == "all":
#             print(sum(sliced_list))
#         elif operation == "asc":
#             sliced_list.sort()
#             print(sliced_list)
#         elif operation == "desc":
#             sliced_list.sort(reverse=True)
#             print(sliced_list)
#         elif operation == "rev":
#             sliced_list.reverse()
#             print(sliced_list)
#     else:
#         if query[0] == "index" and query[1] != "slice":
#             index1 = int(query[2])
#             print(num_list[index1])
#         elif operation == "min":
#             print(min(num_list))
#         elif operation == "max":
#             print(max(num_list))
#         elif operation == "avg":
#             avg = sum(num_list) / len(num_list)
#             print(avg)
#         elif operation == "all":
#             print(sum(num_list))


# num_list = list(map(float, input().split()))
# num = int(input())
# query = [input().split(",") for _ in range(num)]

# for q in query:
#     process_query(num_list, q)



# def safe_slice(num_list, start_index, end_index, step):
#     # 检查步长是否为0，避免无限循环
#     if step == 0 or start_index == end_index:
#         return "Querying on empty list!"
#     # 检查索引是否在合理范围内
#     if step > 0 and start_index >= end_index:
#         return "Querying on empty list!"
#     # 执行切片操作
#     return num_list[start_index:end_index:step]

# def process_query(num_list, query):
#     operation = query[1]
#     if len(query) > 2:
#         start_index = int(query[2])
#         end_index = int(query[3])
#         step = int(query[4])
#         sliced_list = safe_slice(num_list, start_index, end_index, step)
#         if isinstance(sliced_list, str):
#             print(sliced_list)
#             return
#         if not sliced_list:
#             print("Querying on empty list!")
#             return
#         if operation == "min":
#             print(min(sliced_list))
#         elif operation == "max":
#             print(max(sliced_list))
#         elif operation == "avg":
#             avg = sum(sliced_list) / len(sliced_list)
#             print(avg)
#         elif operation == "all":
#             print(sum(sliced_list))
#         elif operation == "asc":
#             sliced_list.sort()
#             print(sliced_list)
#         elif operation == "desc":
#             sliced_list.sort(reverse=True)
#             print(sliced_list)
#         elif operation == "rev":
#             sliced_list.reverse()
#             print(sliced_list)
#     else:
#         if operation == "index":
#             index = int(query[2])
#             print(num_list[index])
#         elif operation == "min":
#             print(min(num_list))
#         elif operation == "max":
#             print(max(num_list))
#         elif operation == "avg":
#             avg = sum(num_list) / len(num_list)
#             print(avg)
#         elif operation == "all":
#             print(sum(num_list))

# def sum(numbers):
#     return sum(numbers)

# num_list = list(map(float, input().split()))
# num = int(input())

# query1 = []
# for i in range(num):
#     a_i = input()
#     query1.append(a_i)

# # print(query)

# query = []
# for i in range(num):
#     query_1 = [m.strip() for m in query1[i].split(",")]
#     query.append(query_1)
# # print(query))

# for q in query:
#     process_query(num_list, q)



# num_list = input().split()
# num_list_2 = list(map(float,num_list))
# # print(num_list_2)

# num = int(input())
# query = []
# for i in range(num):
#     a_i = input()
#     query.append(a_i)

# print(query)

# lst = []
# for i in range(num):
#     lst_1 = [m.strip() for m in query[i].split(",")]
#     lst.append(lst_1)
# # print(lst)


# for i in range(num):
#     if len(lst[i]) > 2 and int(lst[i][2]) == int(lst[i][3]) :
#         print("Querying on empty list!")
#     elif len(lst[i]) > 2 and int(lst[i][4]) == 0:
#         print("Querying on empty list!")
#     elif len(lst[i]) > 2 and int(lst[i][2]) > int(lst[i][3]) and int(lst[i][4]) > 0:
#         print("Querying on empty list!")
#     elif len(lst[i]) > 2 and int(lst[i][2]) < int(lst[i][3]) and int(lst[i][4]) < 0:
#         print("Querying on empty list!")
#     else:
#         if lst[i][1] == "min":
#             if len(lst[i]) > 2:
#                 print(min(num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]))
#             else:
#                 print(min(num_list_2))
#         if lst[i][1] == "max":
#             if len(lst[i]) > 2:
#                 print(max(num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]))
#             else:
#                 print(max(num_list_2))
#         if lst[i][0] == "index" and lst[i][1] != "slice":
#             print(num_list_2[int(lst[i][1])])
#         if lst[i][0] == "index" and lst[i][1] == "slice":
#             if len(lst[i]) > 2:
#                 print(num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])])
#             else:
#                 print(num_list_2)
#         if lst[i][1] == "all":
#             if len(lst[i]) > 2:
#                 num_list_3 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 print(sum(num_list_3))
#             else:
#                 print(sum(num_list_2))
#         if lst[i][1] == "avg":
#             if len(lst[i]) > 2:
#                 num_list_4 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 avg = sum(num_list_4)/len(num_list_4)
#                 print(avg)
#             else:
#                 avg = sum(num_list_2)/len(num_list_2)
#                 print(avg)
#         if lst[i][1] == "asc":
#             if len(lst[i]) > 2:
#                 num_list_5 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 num_list_5.sort()
#                 num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])] = num_list_5
#             else:
#                 num_list_2.sort()
#             print(num_list_2)
#         if lst[i][1] == "desc":
#             if len(lst[i]) > 2:
#                 num_list_6 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 num_list_6.sort(reverse = True)
#                 num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])] = num_list_6
#             else:
#                 num_list_2.sort(reverse = True)
#             print(num_list_2)
#         if lst[i][1] == "rev":
#             if len(lst[i]) > 2:
#                 num_list_6 = num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]
#                 num_list_6 = num_list_6[::-1]
#                 num_list_2[int(lst[i][2]):int(lst[i][3]):int(lst[i][4])]= num_list_6
#             else:
#                 num_list_2 = num_list_2[::-1]
#             print(num_list_2)




# def check_three_of_a_kind(grid):
#     for i in range(3):
#         if grid[i][0] == grid[i][1] == grid[i][2]:
#             return True
#         if grid[0][i] == grid[1][i] == grid[2][i]:
#             return True
#     if grid[0][0] == grid[1][1] == grid[2][2]:
#         return True
#     if grid[0][2] == grid[1][1] == grid[2][0]:
#         return True
#     return False

# def check_pairs(grid):
#     pairs = []
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j] in [grid[k][l] for k in range(3) for l in range(3) if (k, l) != (i, j)]:
#                 pairs.append(grid[i][j])
#                 for m in range(3):
#                     for n in range(3):
#                         if grid[m][n] == grid[i][j] and (m, n) != (i, j):
#                             grid[m][n] = None
#     return pairs

# def check_all_different(grid):
#     return len(set(grid)) == 9

# def main():
#     initial_boxes = int(input("Enter the number of initial blind boxes purchased: "))
#     wish = input("Enter the player's wish for a specific turtle's color and pattern (e.g., RP): ")
#     colors = input("Enter the colors of the turtles (e.g., ROYGB): ")
#     patterns = input("Enter the patterns of the turtles (e.g., PUPU): ")
#     turtles = [colors[i] + patterns[i] for i in range(len(colors))]
#     blind_boxes = initial_boxes
#     eliminated_turtles = []
#     grid = [[None]*3 for _ in range(3)]
#     additional_boxes = 0

#     for turtle in turtles:
#         if blind_boxes == 0:
#             break
#         if turtle == wish:
#             blind_boxes += 1
#         blind_boxes -= 1
#         grid[turtles.index(turtle) % 3][turtles.index(turtle) // 3] = turtle
#         turtles.remove(turtle)

#         if len(grid) == 9:
#             if check_three_of_a_kind(grid):
#                 additional_boxes += 5
#             pairs = check_pairs(grid)
#             if pairs:
#                 eliminated_turtles.extend(pairs)
#                 additional_boxes += len(pairs)
#             if check_all_different(grid):
#                 additional_boxes += 5
#                 grid = [[None]*3 for _ in range(3)]
#         else:
#             print(f"Blind box {len(eliminated_turtles) + 1} contains: {turtle}")

#     while additional_boxes > 0:
#         additional_boxes -= 1
#         for i in range(len(turtles)):
#             new_turtle = turtles[i]
#             if new_turtle == wish:
#                 additional_boxes += 1
#             grid[turtles.index(new_turtle) % 3][turtles.index(new_turtle) // 3] = new_turtle
#             turtles.remove(new_turtle)

#         if len(grid) == 9:
#             if check_three_of_a_kind(grid):
#                 additional_boxes += 5
#             pairs = check_pairs(grid)
#             if pairs:
#                 eliminated_turtles.extend(pairs)
#                 additional_boxes += len(pairs)
#             if check_all_different(grid):
#                 additional_boxes += 5
#                 grid = [[None]*3 for _ in range(3)]

#     for i in range(3):
#         for j in range(3):
#             if grid[i][j] is not None:
#                 eliminated_turtles.append(grid[i][j])

#     print("Eliminated turtles in order:", eliminated_turtles)

# main()


# import random

# # 定义乌龟的可能颜色和图案
# colors = ['R', 'O', 'Y', 'G', 'B']
# patterns = ['P', 'U']

# # 初始化网格
# grid = [[None] * 3 for _ in range(3)]

# # 初始化变量

# eliminated_turtles = []

# # 读取输入
# initial_boxes = int(input("Enter the number of initial blind boxes purchased: "))
# wish_turtle = input("Enter the player's wish for a specific turtle's color and pattern (e.g., RP): ").split()

# # 生成乌龟列表
# color_input = input("Enter the colors of the turtles (e.g., ROYGB): ")
# pattern_input = input("Enter the patterns of the turtles (e.g., PUPU): ")
# turtles = [(color_input[i], pattern_input[i]) for i in range(len(color_input))]

# # 游戏主循环
# while initial_boxes > 0 and len(turtles) > 0:
#     # 随机选择一个乌龟
#     turtle = random.choice(turtles)
#     turtles.remove(turtle)
    
#     # 检查是否是愿望中的乌龟
#     if turtle == (wish_turtle[0], wish_turtle[1]):
#         initial_boxes += 1  # 愿望匹配，获得额外盲盒
    
#     # 将乌龟放入网格
#     empty_cells = [(i, j) for i in range(3) for j in range(3) if grid[i][j] is None]
#     if empty_cells:
#         i, j = empty_cells[0]
#         grid[i][j] = turtle
#     else:
#         # 网格已满，检查奖励条件
#         break
    
#     # 减少盲盒数量
#     initial_boxes -= 1

# # 检查奖励条件
# def check_rewards():
#     # 检查所有不同的乌龟
#     if all(t is not None for row in grid for t in row) and len(set(tuple(t) for row in grid for t in row)) == 9:
#         for row in grid:
#             for t in row:
#                 if t:
#                     eliminated_turtles.append(t)
#         return 5
#     else:
#         return 0

# # 检查三连和对子
# def check_three_of_a_kind_and_pairs():
#     # 检查三连
#     for i in range(3):
#         if grid[i][0] == grid[i][1] == grid[i][2] or grid[0][i] == grid[1][i] == grid[2][i]:
#             return 5
#     if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
#         return 5
    
#     # 检查对子
#     seen = set()
#     for row in grid:
#         for t in row:
#             if t and t in seen:
#                 eliminated_turtles.append(t)
#                 return 1
#             seen.add(t) if t else None
    
#     return 0

# # 应用奖励和消除规则
# additional_boxes = check_rewards()
# additional_boxes += check_three_of_a_kind_and_pairs()

# # 更新盲盒数量
# initial_boxes += additional_boxes

# # 输出结果
# print("Eliminated turtles in order:", eliminated_turtles)
# for row in grid:
#     print(row)

# import itertools

# # 定义乌龟的可能颜色和图案
# colors = ['R', 'O', 'Y', 'G', 'B']
# patterns = ['P', 'U']

# # 检查三个相同的乌龟是否在一行、一列或对角线上
# def check_three_of_a_kind(grid):
#     for row in grid:
#         if row[0] == row[1] == row[2]:
#             return True
#     for col in range(3):
#         if grid[0][col] == grid[1][col] == grid[2][col]:
#             return True
#     if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
#         return True
#     return False

# def check_pairs(grid):
#     # 用于存储被移除的乌龟
#     eliminated = []
#     # 存储网格中的乌龟，以便快速比较
#     grid_turtles = [turtle for row in grid for turtle in row if turtle]

#     # 检查每个乌龟是否在网格中出现两次
#     for turtle in grid_turtles:
#         if grid_turtles.count(turtle) > 1:
#             # 找到一对，移除它们
#             eliminated.append(turtle)
#             # 在网格中找到并移除这两个乌龟
#             for i in range(3):
#                 for j in range(3):
#                     if grid[i][j] == turtle:
#                         grid[i][j] = None
#                         break

#     return eliminated
#     return pairs

# # 检查所有乌龟是否都不同
# def check_all_different(grid):
#     return len(set(turtle for row in grid for turtle in row if turtle)) == 9

# # 主程序
# def main():
#     # 读取输入
#     initial_boxes = int(input("Enter the number of initial blind boxes purchased: "))
#     wish = input("Enter the player's wish for a specific turtle's color and pattern (e.g., RP): ").split()
#     color_input = input("Enter the colors of the turtles (e.g., ROYGB): ")
#     pattern_input = input("Enter the patterns of the turtles (e.g., PUPU): ")
    
#     # 创建乌龟列表
#     turtles = [(color_input[i] + pattern_input[i]) for i in range(len(color_input))]
    
#     # 初始化网格和变量
#     grid = [[None] * 3 for _ in range(3)]
#     eliminated_turtles = []
#     additional_boxes = 0
#     wish_count = 0
    
#     # 放置乌龟到网格
#     for i, turtle in enumerate(turtles):
#         if i < 9:
#             if turtle == wish[0] + wish[1]:
#                 additional_boxes += 1  # 愿望匹配，获得额外盲盒
#             grid[i // 3][i % 3] = turtle
    
#     # 检查奖励条件
#     while additional_boxes > 0 and any(None in row for row in grid):
#         # 从剩余的乌龟中选择一个放入网格
#         for i, turtle in enumerate(turtles[initial_boxes + additional_boxes:]):
#             empty_cells = [(r, c) for r in range(3) for c in range(3) if grid[r][c] is None]
#             if empty_cells:
#                 row, col = empty_cells[0]
#                 grid[row][col] = turtle
#                 if turtle == wish[0] + wish[1]:
#                     additional_boxes += 1  # 愿望匹配，获得额外盲盒
#                 break
#         additional_boxes -= 1
        
#         # 检查三连、对子和全部不同
#         if check_three_of_a_kind(grid):
#             additional_boxes += 5
#         if check_all_different(grid) and all(grid[i][j] is not None for i in range(3) for j in range(3)):
#             additional_boxes += 5
#         pairs = check_pairs(grid)
#         if pairs:
#             additional_boxes += len(pairs)
    
#     # 移除所有乌龟，因为网格满了或者没有更多的盲盒
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)
    
#     # 输出结果
#     print("Eliminated turtles in order:", eliminated_turtles)

# if __name__ == "__main__":
#     main()

# 定义乌龟的可能颜色和图案
# colors = ['R', 'O', 'Y', 'G', 'B']
# patterns = ['P', 'U']

# # 初始化网格
# grid = [[None] * 3 for _ in range(3)]

# # 读取输入
# initial_boxes = int(input("Enter the number of initial blind boxes purchased: "))
# wish = input("Enter the player's wish for a specific turtle's color and pattern (e.g., RP): ").split()

# # 读取乌龟的颜色和图案
# colors_input = input("Enter the colors of the turtles (e.g., ROYGB): ")
# patterns_input = input("Enter the patterns of the turtles (e.g., PUPU): ")

# # 创建乌龟列表
# turtles = [(colors_input[i], patterns_input[i]) for i in range(len(colors_input))]

# # 游戏主循环
# def simulate_game(turtles, wish, grid):
#     additional_boxes = 0
#     eliminated_turtles = []
#     current_turtle_index = 0

#     def is_full():
#         return all(t is not None for row in grid for t in row)

#     def check_all_different():
#         seen = set()
#         for row in grid:
#             for cell in row:
#                 if cell in seen or cell is None:
#                     return False
#                 seen.add(cell)
#         return True

#     def check_three_of_a_kind():
#         for row in grid:
#             if row[0] == row[1] == row[2]:
#                 return True
#         for col in range(3):
#             if grid[0][col] == grid[1][col] == grid[2][col]:
#                 return True
#         if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
#             return True
#         return False

#     def check_pairs():
#         seen = {}
#         for row in grid:
#             for cell in row:
#                 if cell:
#                     if cell in seen:
#                         eliminated_turtles.append(cell)
#                         seen[cell] = True
#                     else:
#                         seen[cell] = False

#     while not is_full() and current_turtle_index < len(turtles):
#         turtle = turtles[current_turtle_index]
#         wish_match = turtle == (wish[0], wish[1])
#         grid[current_turtle_index // 3][current_turtle_index % 3] = turtle
#         if wish_match:
#             additional_boxes += 1
#         current_turtle_index += 1

#     # 检查奖励条件
#     check_pairs()
#     if check_all_different():
#         additional_boxes += 5
#     if check_three_of_a_kind():
#         additional_boxes += 5

#     # 处理额外的盲盒
#     while additional_boxes > 0 and (not is_full()):
#         additional_boxes -= 1
#         turtle = generate_turtle()
#         grid[current_turtle_index // 3][current_turtle_index % 3] = turtle
#         current_turtle_index += 1

#     return eliminated_turtles, grid

# # 生成乌龟函数（如果需要额外的乌龟）
# def generate_turtle():
#     return random.choice(colors) + random.choice(patterns)

# # 运行游戏
# eliminated_turtles, final_grid = simulate_game(turtles, (wish[0], wish[1]), grid)

# # 输出结果
# print("Eliminated turtles in order:", eliminated_turtles)
# print("Final grid:", [tuple(row) for row in final_grid])


# import itertools

# def check_three_of_a_kind(grid):
#     # 检查行、列和对角线
#     for i in range(3):
#         if grid[i].count(grid[i][0]) == 3 or [grid[j][i] for j in range(3)].count(grid[0][i]) == 3:
#             return True
#     if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
#         return True
#     return False

# def check_all_different(grid):
#     return len(set(itertools.chain(*grid))) == 9

# def check_pairs(grid):
#     seen = {}
#     for row in grid:
#         for item in row:
#             if item in seen:
#                 return True
#             seen[item] = True
#     return False

# def eliminate_pairs(grid):
#     eliminated = []
#     for i, row in enumerate(grid):
#         for j, item in enumerate(row):
#             if item in grid[i][:j] + grid[i][j+1:] + [row[k] for k in range(3) if k != j]:
#                 eliminated.append(item)
#                 for m in range(3):
#                     for n in range(3):
#                         if grid[m][n] == item and (m, n) != (i, j):
#                             grid[m][n] = None
#     return eliminated

# def simulate_game(wish, colors, patterns):
#     grid = [[None] * 3 for _ in range(3)]
#    盲盒数量 = int(input("Enter the number of initial blind boxes purchased: ")]
#     wish_turtle = (wish[0], wish[1])
#     additional_boxes = 0
#     eliminated_turtles = []

#     for i in range(min(盲盒数量, 9)):
#         color, pattern = colors[i], patterns[i]
#         turtle = (color, pattern)
#         grid[i // 3][i % 3] = turtle
#         if turtle == wish_turtle:
#             additional_boxes += 1

#     # 检查三连、全部不同和对子
#     while additional_boxes > 0:
#         additional_boxes -= 1
#         color, pattern = colors[盲盒数量 + additional_boxes], patterns[盲盒数量 + additional_boxes]
#         turtle = (color, pattern)
#         grid[(盲盒数量 + additional_boxes) // 3][(盲盒数量 + additional_boxes) % 3] = turtle
#         if turtle == wish_turtle:
#             additional_boxes += 1

#         if check_three_of_a_kind(grid):
#             additional_boxes += 5
#         if check_all_different(grid):
#             additional_boxes += 5
#         if check_pairs(grid):
#             pairs_eliminated = eliminate_pairs(grid)
#             additional_boxes += len(pairs_eliminated)
#             eliminated_turtles.extend(pairs_eliminated)

#     # 最后检查是否还有对子需要移除
#     final_eliminated = eliminate_pairs(grid)
#     eliminated_turtles.extend(final_eliminated)

#     # 按顺序输出移除的乌龟和剩余的乌龟
#     eliminated_turtles.extend([grid[i // 3][i % 3] for i in range(9) if grid[i // 3][i % 3] is not None])
#     return eliminated_turtles

# # 输入
# wish = input("Enter the player's wish for a specific turtle's color and pattern (e.g., RP): ").split()
# colors = input("Enter the colors of the turtles (e.g., ROYGB): ")
# patterns = input("Enter the patterns of the turtles (e.g., PUPU): ")

# # 运行游戏模拟
# eliminated_turtles = simulate_game(wish, colors, patterns)

# # 输出结果
# print("Eliminated turtles in order:", eliminated_turtles)


# import itertools

# # 检查是否有三条相同乌龟的函数
# def check_three_of_a_kind(grid):
#     win_conditions = [
#         [grid[0][0], grid[0][1], grid[0][2]],  # 顶行
#         [grid[1][0], grid[1][1], grid[1][2]],  # 中行
#         [grid[2][0], grid[2][1], grid[2][2]],  # 底行
#         [grid[0][0], grid[1][0], grid[2][0]],  # 左列
#         [grid[0][1], grid[1][1], grid[2][1]],  # 中列
#         [grid[0][2], grid[1][2], grid[2][2]],  # 右列
#         [grid[0][0], grid[1][1], grid[2][2]],  # 对角线
#         [grid[2][0], grid[1][1], grid[0][2]]   # 反对角线
#     ]
#     for condition in win_conditions:
#         if len(set(condition)) == 1:
#             return True, condition
#     return False, []

# # 检查是否有对子并返回对子列表的函数
# def check_pairs(grid):
#     pairs = []
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j]:
#                 for k in range(i+1, 3):
#                     for l in range(3):
#                         if grid[k][l] and grid[i][j] == grid[k][l]:
#                             pairs.append((grid[i][j], (i, j), (k, l)))
#                             grid[k][l] = None
#     return pairs

# # 根据对子列表消除乌龟的函数
# def eliminate_pairs(pairs, grid):
#     for pair in pairs:
#         grid[pair[1][0]][pair[1][1]] = None
#         grid[pair[2][0]][pair[2][1]] = None
#     return grid

# # 打印网格的函数
# def print_grid(grid):
#     for row in grid:
#         print(' | '.join((' ' if not turtle else f'{turtle[0]}{turtle[1]}' for turtle in row)))
#     print()

# # 模拟游戏的函数
# def simulate_game(initial_boxes, wish, colors, patterns):
#     blind_boxes = initial_boxes
#     grid = [[None for _ in range(3)] for _ in range(3)]
#     eliminated = []
#     rewards = 0
#     additional_boxes = 0

#     # 填充网格
#     for i in range(min(9, len(colors))):
#         color, pattern = colors[i], patterns[i]
#         if (color, pattern) == wish:
#             additional_boxes += 1
#         grid[i // 3][i % 3] = (color, pattern)

#     # 检查三连和对子
#     while blind_boxes > 0 or additional_boxes > 0:
#         three_of_a_kind, _ = check_three_of_a_kind(grid)
#         if three_of_a_kind:
#             rewards += 5
#             additional_boxes += 5
#         pairs = check_pairs(grid)
#         if pairs:
#             for pair in pairs:
#                 eliminated.append(pair[0])
#                 rewards += 1
#                 additional_boxes += 1
#             grid = eliminate_pairs(pairs, grid)

#         # 检查是否所有乌龟都不同
#         if all(grid[i][j] != None and grid[i][j] != grid[i][j+1] and grid[i][j] != grid[(i+1)%3][j] for i in range(3) for j in range(2)) and all(grid[i][j] != grid[(i+1)%3][(j+1)%3] for i in range(3) for j in range(3)):
#             rewards += 5
#             additional_boxes += 5
#             grid = [[None for _ in range(3)] for _ in range(3)]

#         # 获取下一个乌龟
#         if additional_boxes > 0:
#             additional_boxes -= 1
#             if len(colors) > 9 + i:
#                 color, pattern = colors[9 + i], patterns[9 + i]
#                 if (color, pattern) == wish:
#                     additional_boxes += 1
#                 grid[i // 3][i % 3] = (color, pattern)
#         else:
#             break

#     # 消除剩余的乌龟
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j]:
#                 eliminated.append(grid[i][j])

#     return rewards, eliminated

# # 示例输入
# initial_boxes = int(input())
# wish = input()
# colors = input()
# patterns = input()

# # 运行模拟
# rewards, eliminated = simulate_game(initial_boxes, wish, colors, patterns)
# print(f"总奖励：{rewards}")
# print("消除的乌龟：", eliminated)
# def are_all_turtles_different(grid):
#     # Check if all turtles in the grid are different
#     turtle_list = [(cell[0], cell[1]) for row in grid for cell in row if cell]
#     if len(turtle_list) == len(set(turtle_list)):
#         return True
#     return False

# def find_three_of_a_kind(grid):
#     # Check for three identical turtles in a row, column, or diagonal
#     win_conditions = [
#         (grid[0][0], grid[0][1], grid[0][2]),  # Top row
#         (grid[1][0], grid[1][1], grid[1][2]),  # Middle row
#         (grid[2][0], grid[2][1], grid[2][2]),  # Bottom row
#         (grid[0][0], grid[1][0], grid[2][0]),  # Left column
#         (grid[0][1], grid[1][1], grid[2][1]),  # Middle column
#         (grid[0][2], grid[1][2], grid[2][2]),  # Right column
#         (grid[0][0], grid[1][1], grid[2][2]),  # Diagonal
#         (grid[2][0], grid[1][1], grid[0][2])   # Anti-diagonal
#     ]
#     for condition in win_conditions:
#         if condition[0] and condition[0] == condition[1] == condition[2]:
#             return True, condition
#     return False, []

# def find_pairs(grid):
#     # Check for pairs and return a list of pairs
#     pairs = []
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j]:
#                 for k in range(i+1, 3):
#                     for l in range(3):
#                         if grid[k][l] and grid[i][j] == grid[k][l]:
#                             pairs.append((grid[i][j], (i, j), (k, l)))
#     return pairs


# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = [[None]*3 for _ in range(3)]  # Initialize the 3x3 grid
#     eliminated_turtles = []  # List of eliminated turtles
#     additional_boxes = 0  # Number of additional blind boxes obtained
#     current_turtle_index = 0  # Index of the current turtle being processed

#     # Process initial blind boxes
#     for _ in range(initial_boxes):
#         if current_turtle_index >= len(colors):
#             break
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         if (color, pattern) == wish:
#             additional_boxes += 1  # Wish matches, get an additional blind box
#         # Find an empty cell in the grid
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] is None:
#                     grid[i][j] = (color, pattern)
#                     break
#             else:
#                 continue
#             break

#     # Check if the grid is full and all turtles are different
#     if all(cell is not None for row in grid for cell in row) and all(turtle != neighbor for row in grid for turtle, neighbor in zip(row, row[1:])):
#         additional_boxes += 5  # All different, get additional blind boxes
#         grid = [[None]*3 for _ in range(3)]  # Clear the grid

#     # Continue processing additional blind boxes
#     while additional_boxes > 0 and current_turtle_index < len(colors):
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         if (color, pattern) == wish:
#             additional_boxes += 1  # Wish matches, get an additional blind box
#         # Find an empty cell in the grid
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] is None:
#                     grid[i][j] = (color, pattern)
#                     break
#             else:
#                 continue
#             break

#         # Check for three identical turtles
#         three_of_a_kind, _ = find_three_of_a_kind(grid)
#         if three_of_a_kind:
#             additional_boxes += 5  # Three of a kind, get additional blind boxes

#         # Check for pairs
#         pairs = find_pairs(grid)
#         if pairs:
#             for pair in pairs:
#                 eliminated_turtles.append(pair[0])
#                 grid[pair[1][0]][pair[1][1]] = None
#                 grid[pair[2][0]][pair[2][1]] = None
#                 additional_boxes += 1  # Pair eliminated, get additional blind box

#         # Check if the grid is full and all turtles are different
#         if all(cell is not None for row in grid for cell in row) and all(turtle != neighbor for row in grid for turtle, neighbor in zip(row, row[1:])):
#             additional_boxes += 5  # All different, get additional blind boxes
#             eliminated_turtles.extend([(turtle[0], turtle[1]) for row in grid for turtle in row if turtle])
#             grid = [[None]*3 for _ in range(3)]  # Clear the grid

#     # Eliminate remaining turtles
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles

# # Example input
# initial_boxes = int(input("Enter the number of initial blind boxes purchased: "))
# wish = input("Enter the player's wish for a specific turtle's color and pattern (e.g., RP): ").split()
# colors = list(input("Enter the colors of the turtles (e.g., ROYGB): "))
# patterns = list(input("Enter the patterns of the turtles (e.g., PUU): "))

# # Run the simulation
# eliminated_turtles = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)

# def check_grid(grid):
#     # 检查网格是否满了，以及是否所有乌龟都不同
#     if all(cell is not None for row in grid for cell in row):
#         if len(set(tuple(cell) for row in grid for cell in row)) == 9:
#             return True, 5  # 所有乌龟不同，返回True和奖励
#     return False, 0

# def find_three_of_a_kind(grid):
#     # 检查是否有三个相同的乌龟在一行、一列或对角线上
#     win_conditions = [
#         grid[0], grid[1], grid[2],  # 行
#         [grid[0][0], grid[1][0], grid[2][0]], [grid[0][1], grid[1][1], grid[2][1]], [grid[0][2], grid[1][2], grid[2][2]],  # 列
#         [grid[0][0], grid[1][1], grid[2][2]], [grid[2][0], grid[1][1], grid[0][2]]  # 对角线
#     ]
#     for condition in win_conditions:
#         if condition[0] == condition[1] == condition[2]:
#             return True
#     return False

# def find_pairs(grid):
#     # 检查是否有对子并返回对子列表
#     seen = []
#     pairs = []
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j] and grid[i][j] not in seen:
#                 for k in range(i+1, 3):
#                     for l in range(3):
#                         if grid[k][l] == grid[i][j]:
#                             pairs.append((grid[i][j], (i, j), (k, l)))
#                             seen.append(grid[i][j])
#                             break
#     return pairs

# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = [[None]*3 for _ in range(3)]  # 初始化3x3网格
#     eliminated_turtles = []  # 被消除的乌龟列表
#     additional_boxes = 0  # 额外获得的盲盒数量
#     current_turtle_index = 0  # 当前处理的乌龟索引

#     # 处理初始盲盒
#     for _ in range(initial_boxes):
#         if current_turtle_index >= len(colors):
#             break
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         if (color, pattern) == wish:
#             additional_boxes += 1  # 愿望匹配，获得额外盲盒
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] is None:
#                     grid[i][j] = (color, pattern)
#                     break
#             else:
#                 continue
#             break

#     # 检查网格状态
#     all_different, reward = check_grid(grid)
#     if all_different:
#         additional_boxes += reward  # 所有不同，获得额外盲盒
#         eliminated_turtles.extend(grid[0] + grid[1] + grid[2])  # 清空网格
#         grid = [[None]*3 for _ in range(3)]

#     # 继续处理额外的盲盒
#     while additional_boxes > 0:
#         additional_boxes -= 1
#         if current_turtle_index >= len(colors):
#             break
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         if (color, pattern) == wish:
#             additional_boxes += 1  # 愿望匹配，获得额外盲盒
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] is None:
#                     grid[i][j] = (color, pattern)
#                     break
#             else:
#                 continue
#             break

#         # 检查是否有三个相同的乌龟
#         if find_three_of_a_kind(grid):
#             additional_boxes += 5  # 三个相同，获得额外盲盒

#         # 检查是否有对子
#         pairs = find_pairs(grid)
#         if pairs:
#             for pair in pairs:
#                 eliminated_turtles.append(pair[0])
#                 grid[pair[1][0]][pair[1][1]] = None
#                 grid[pair[2][0]][pair[2][1]] = None
#                 additional_boxes += 1  # 对子消除，获得额外盲盒

#     # 消除剩余的乌龟
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles

# # 示例输入
# initial_boxes = 10
# wish = "Y U"
# colors = list("YOBOOBRGOGYBYRYYGBO")
# patterns = list("UUUUPUUPPPUUUUPUUP")

# # 运行模拟
# eliminated_turtles = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)

# def check_all_different(grid):
#     # 检查网格中的乌龟是否全部不同
#     turtles = [turtle for row in grid for turtle in row if turtle]
#     return len(turtles) == len(set(turtles))

# def find_three_of_a_kind(grid):
#     # 检查是否有三个相同的乌龟在一行、一列或对角线上
#     win_conditions = [
#         grid[0], grid[1], grid[2],  # 行
#         [grid[0][0], grid[1][0], grid[2][0]], [grid[0][1], grid[1][1], grid[2][1]], [grid[0][2], grid[1][2], grid[2][2]],  # 列
#         [grid[0][0], grid[1][1], grid[2][2]], [grid[2][0], grid[1][1], grid[0][2]]  # 对角线
#     ]
#     for condition in win_conditions:
#         if condition[0] == condition[1] == condition[2]:
#             return True
#     return False

# def find_pairs(grid):
#     # 检查是否有对子并返回对子列表
#     seen = []
#     pairs = []
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j] and grid[i][j] not in seen:
#                 for k in range(i+1, 3):
#                     for l in range(3):
#                         if grid[k][l] == grid[i][j]:
#                             pairs.append((grid[i][j], (i, j), (k, l)))
#                             seen.append(grid[i][j])
#                             break
#     return pairs

# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = [[None]*3 for _ in range(3)]  # 初始化3x3网格
#     eliminated_turtles = []  # 被消除的乌龟列表
#     additional_boxes = initial_boxes - 9  # 额外获得的盲盒数量
#     current_turtle_index = 0  # 当前处理的乌龟索引

#     # 处理初始盲盒
#     for _ in range(initial_boxes):
#         if current_turtle_index >= len(colors):
#             break
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] is None:
#                     grid[i][j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#     # 检查网格是否满了，如果满了且所有乌龟都不同
#     while check_all_different(grid):
#         eliminated_turtles.extend(grid[0] + grid[1] + grid[2])
#         additional_boxes += 5
#         grid = [[None]*3 for _ in range(3)]  # 清空网格

#     # 继续处理额外的盲盒
#     while additional_boxes > 0 and current_turtle_index < len(colors):
#         additional_boxes -= 1
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] is None:
#                     grid[i][j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#         # 检查是否有三个相同的乌龟
#         if find_three_of_a_kind(grid):
#             additional_boxes += 5  # 三个相同，获得额外盲盒

#         # 检查是否有对子
#         pairs = find_pairs(grid)
#         if pairs:
#             for pair in pairs:
#                 eliminated_turtles.append(pair[0])
#                 grid[pair[1][0]][pair[1][1]] = None
#                 grid[pair[2][0]][pair[2][1]] = None
#                 additional_boxes += 1  # 对子消除，获得额外盲盒

#     # 消除剩余的乌龟
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles

# # 示例输入
# initial_boxes = 10
# wish = input()
# colors = list(input())
# patterns = list(input())

# # 运行模拟
# eliminated_turtles = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)

# import itertools

# def check_all_different(grid):
#     """检查网格中的乌龟是否全部不同"""
#     turtles = [turtle for row in grid for turtle in row if turtle]
#     return len(turtles) == len(set(turtles))

# def find_three_of_a_kind(grid):
#     """检查是否有三个相同的乌龟在一行、一列或对角线上"""
#     win_conditions = [
#         grid[0], grid[1], grid[2],  # 行
#         [grid[0][0], grid[1][0], grid[2][0]], [grid[0][1], grid[1][1], grid[2][1]], [grid[0][2], grid[1][2], grid[2][2]],  # 列
#         [grid[0][0], grid[1][1], grid[2][2]], [grid[2][0], grid[1][1], grid[0][2]]  # 对角线
#     ]
#     for condition in win_conditions:
#         if condition[0] == condition[1] == condition[2]:
#             return True
#     return False

# def find_and_eliminate_pairs(grid):
#     """查找并消除对子"""
#     pairs = []
#     seen = []
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j] and grid[i][j] not in seen:
#                 for k in range(i+1, 3):
#                     for l in range(3):
#                         if grid[k][l] == grid[i][j]:
#                             pairs.append((grid[i][j], (i, j), (k, l)))
#                             grid[i][j] = None
#                             grid[k][l] = None
#                             seen.append(grid[i][j])
#                             break
#     return pairs

# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = [[None]*3 for _ in range(3)]  # 初始化3x3网格
#     eliminated_turtles = []  # 被消除的乌龟列表
#     additional_boxes = 0  # 额外获得的盲盒数量
#     current_turtle_index = 0  # 当前处理的乌龟索引

#     # 处理初始盲盒，直到网格满或处理完所有盲盒
#     for i in range(min(initial_boxes, 9)):
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for row in grid:
#             for j in range(3):
#                 if row[j] is None:
#                     row[j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#     # 检查网格是否满了，如果满了且所有乌龟都不同
#     if all(cell is not None for row in grid for cell in row):
#         if len(set(cell for row in grid for cell in row)) == 9 and check_all_different(grid):
#             additional_boxes += 5

#     # 继续处理额外的盲盒
#     while additional_boxes > 0 and current_turtle_index < len(colors):
#         additional_boxes -= 1
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1

#         # 检查是否有对子
#         pairs = find_and_eliminate_pairs(grid)
#         if pairs:
#             for pair in pairs:
#                 eliminated_turtles.append(pair[0])
#                 additional_boxes += 1  # 对子消除，获得额外盲盒
#         else:
#             for row in grid:
#                 for j in range(3):
#                     if row[j] is None:
#                         row[j] = (color, pattern)
#                         if (color, pattern) == wish:
#                             additional_boxes += 1
#                         break
#                 else:
#                     continue
#                 break

#         # 检查是否有三个相同的乌龟
#         if find_three_of_a_kind(grid):
#             additional_boxes += 5

#     # 消除剩余的乌龟
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles, additional_boxes

# # 示例输入
# initial_boxes = 10
# wish = "Y U"
# colors = "YOBOOBRGOGYBYRYYGBO"
# patterns = "UUUUPUUPPPUUUUPUUP"

# # 运行模拟
# eliminated_turtles, additional_boxes = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)
# print("Additional blind boxes earned:", additional_boxes)

# import itertools

# def initialize_grid(size):
#     """初始化网格"""
#     return [[None for _ in range(size)] for _ in range(size)]

# def check_all_different(grid):
#     """检查网格中的乌龟是否全部不同"""
#     turtles = [turtle for row in grid for turtle in row if turtle]
#     return len(turtles) == len(set(turtles))

# def find_three_of_a_kind(grid):
#     """检查是否有三个相同的乌龟在一行、一列或对角线上"""
#     win_conditions = [
#         grid[0], grid[1], grid[2],  # 行
#         [grid[0][0], grid[1][0], grid[2][0]], [grid[0][1], grid[1][1], grid[2][1]], [grid[0][2], grid[1][2], grid[2][2]],  # 列
#         [grid[0][0], grid[1][1], grid[2][2]], [grid[2][0], grid[1][1], grid[0][2]]  # 对角线
#     ]
#     for condition in win_conditions:
#         if condition[0] == condition[1] == condition[2]:
#             return True
#     return False

# def find_and_eliminate_pairs(grid):
#     """查找并消除对子"""
#     pairs = []
#     for pos1, pos2 in itertools.combinations(range(9), 2):
#         row1, col1 = divmod(pos1, 3)
#         row2, col2 = divmod(pos2, 3)
#         if grid[row1][col1] == grid[row2][col2]:
#             pairs.append((grid[row1][col1], (row1, col1), (row2, col2)))
#             grid[row1][col1] = None
#             grid[row2][col2] = None
#     return pairs

# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = initialize_grid(3)
#     eliminated_turtles = []
#     additional_boxes = 0
#     current_turtle_index = 0

#     def process_grid():
#         if check_all_different(grid):
#             nonlocal additional_boxes
#             additional_boxes += 5
#             for row in grid:
#                 for j in range(3):
#                     eliminated_turtles.append(row[j])
#                     row[j] = None
#         if find_three_of_a_kind(grid):
#             nonlocal additional_boxes
#             additional_boxes += 5
#         pairs = find_and_eliminate_pairs(grid)
#         if pairs:
#             nonlocal additional_boxes
#             additional_boxes += len(pairs)
#             for pair in pairs:
#                 eliminated_turtles.append(pair[0])

#     # 处理初始盲盒，直到网格满或处理完所有盲盒
#     for i in range(min(initial_boxes, 9)):
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for row in grid:
#             for j in range(3):
#                 if row[j] is None:
#                     row[j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break
#         process_grid()

#     # 继续处理额外的盲盒
#     while additional_boxes > 0 and current_turtle_index < len(colors):
#         additional_boxes -= 1
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for row in grid:
#             for j in range(3):
#                 if row[j] is None:
#                     row[j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break
#         process_grid()

#     # 消除剩余的乌龟
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles, additional_boxes

# # 示例输入
# initial_boxes = 10
# wish = "Y U"
# colors = "YOBOOBRGOGYBYRYYGBO"
# patterns = "UUUUPUUPPPUUUUPUUP"

# # 运行模拟
# eliminated_turtles, additional_boxes = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)
# print("Additional blind boxes earned:", additional_boxes)

# import itertools

# def initialize_grid(size):
#     """初始化网格"""
#     return [[None for _ in range(size)] for _ in range(size)]

# def check_all_different(grid):
#     """检查网格中的乌龟是否全部不同"""
#     turtles = [turtle for row in grid for turtle in row if turtle]
#     return len(turtles) == len(set(turtles))

# def find_three_of_a_kind(grid):
#     """检查是否有三个相同的乌龟在一行、一列或对角线上"""
#     three_of_a_kind = []
#     for i in range(3):
#         if grid[i][0] == grid[i][1] == grid[i][2]:  # 检查行
#             three_of_a_kind.append((grid[i][0], i, [0, 1, 2]))
#         if grid[0][i] == grid[1][i] == grid[2][i]:  # 检查列
#             three_of_a_kind.append((grid[0][i], 0, i, [0, 1, 2]))
#     if grid[0][0] == grid[1][1] == grid[2][2] or grid[2][0] == grid[1][1] == grid[0][2]:  # 检查对角线
#         three_of_a_kind.append((grid[0][0], 0, 1, [0, 1, 2]))
#     return three_of_a_kind

# def find_and_eliminate_pairs(grid, eliminated_turtles):
#     """查找并消除对子"""
#     pairs = []
#     positions = list(itertools.combinations(range(9), 2))
#     for pos1, pos2 in positions:
#         row1, col1 = divmod(pos1, 3)
#         row2, col2 = divmod(pos2, 3)
#         if grid[row1][col1] == grid[row2][col2]:
#             pairs.append((grid[row1][col1], (row1, col1), (row2, col2)))
#             grid[row1][col1] = None
#             grid[row2][col2] = None
#             eliminated_turtles.extend([(grid[row1][col1], (row1, col1)), (grid[row2][col2], (row2, col2))])
#     return pairs


# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = initialize_grid(3)
#     eliminated_turtles = []
#     additional_boxes = 0
#     current_turtle_index = 0

#     # 处理初始盲盒，直到网格满或处理完所有盲盒
#     for i in range(min(initial_boxes, 9)):
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for row in grid:
#             for j in range(3):
#                 if row[j] is None:
#                     row[j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#     # 检查特殊条件
#     three_of_a_kind = find_three_of_a_kind(grid)
#     if three_of_a_kind:
#         additional_boxes += 5 * len(three_of_a_kind)
#     if check_all_different(grid):
#         additional_boxes += 5
#         for row in grid:
#             for j in range(3):
#                 if row[j]:
#                     eliminated_turtles.append(row[j])
#                     row[j] = None

#     while current_turtle_index < len(colors) and additional_boxes > 0:
#         additional_boxes -= 1
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for row in grid:
#             for j in range(3):
#                 if row[j] is None:
#                     row[j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#         # 检查特殊条件
#         three_of_a_kind = find_three_of_a_kind(grid)
#         if three_of_a_kind:
#             additional_boxes += 5 * len(three_of_a_kind)
#         pairs = find_and_eliminate_pairs(grid, eliminated_turtles)
#         if pairs:
#             additional_boxes += len(pairs)

#     # 消除剩余的乌龟
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles, additional_boxes

# # 示例输入
# initial_boxes = 10

# wish = "Y U"
# colors = "YOBOOBRGOGYBYRYYGBO"
# patterns = "UUUUPUUPPPUUUUPUUP"

# # 运行模拟
# eliminated_turtles, additional_boxes = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)
# print("Additional blind boxes earned:", additional_boxes)


# import itertools

# def initialize_grid(size):
#     """初始化网格"""
#     return [[None for _ in range(size)] for _ in range(size)]

# def check_all_different(grid):
#     """检查网格中的乌龟是否全部不同"""
#     turtles = [turtle for row in grid for turtle in row if turtle]
#     return len(turtles) == len(set(turtles))

# def find_three_of_a_kind(grid):
#     """检查是否有三个相同的乌龟在一行、一列或对角线上"""
#     three_of_a_kind = []
#     for i in range(3):
#         if grid[i][0] == grid[i][1] == grid[i][2]:  # 检查行
#             three_of_a_kind.append((grid[i][0], i, [0, 1, 2]))
#         if grid[0][i] == grid[1][i] == grid[2][i]:  # 检查列
#             three_of_a_kind.append((grid[0][i], 0, i, [0, 1, 2]))
#     if grid[0][0] == grid[1][1] == grid[2][2] or grid[2][0] == grid[1][1] == grid[0][2]:  # 检查对角线
#         three_of_a_kind.append((grid[0][0], 0, 1, [0, 1, 2]))
#     return three_of_a_kind

# def find_and_eliminate_pairs(grid, eliminated_turtles, additional_boxes):
#     """查找并消除对子"""
#     pairs = []
#     positions = list(itertools.combinations(range(9), 2))
#     for pos1, pos2 in positions:
#         row1, col1 = divmod(pos1, 3)
#         row2, col2 = divmod(pos2, 3)
#         if grid[row1][col1] == grid[row2][col2]:
#             pairs.append((grid[row1][col1], (row1, col1), (row2, col2)))
#             grid[row1][col1] = None
#             grid[row2][col2] = None
#             eliminated_turtles.extend([(grid[row1][col1], (row1, col1)), (grid[row2][col2], (row2, col2))])
#     return pairs, additional_boxes + len(pairs)

# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = initialize_grid(3)
#     eliminated_turtles = []
#     additional_boxes = 0
#     current_turtle_index = 0

#     # 处理初始盲盒，直到网格满或处理完所有盲盒
#     for i in range(min(initial_boxes, 9)):
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for row in grid:
#             for j in range(3):
#                 if row[j] is None:
#                     row[j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#     # 检查特殊条件
#     three_of_a_kind = find_three_of_a_kind(grid)
#     if three_of_a_kind:
#         additional_boxes += 5 * len(three_of_a_kind)
#     if check_all_different(grid):
#         additional_boxes += 5
#         for row in grid:
#             for j in range(3):
#                 if row[j]:
#                     eliminated_turtles.append(row[j])
#                     row[j] = None

#     while current_turtle_index < len(colors) and additional_boxes > 0:
#         additional_boxes -= 1
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for row in grid:
#             for j in range(3):
#                 if row[j] is None:
#                     row[j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#         # 检查特殊条件
#         three_of_a_kind = find_three_of_a_kind(grid)
#         if three_of_a_kind:
#             additional_boxes += 5 * len(three_of_a_kind)
#         pairs, additional_boxes = find_and_eliminate_pairs(grid, eliminated_turtles, additional_boxes)
#         if pairs:
#             additional_boxes += len(pairs)

#     # 消除剩余的乌龟
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles, additional_boxes

# # 示例输入
# initial_boxes = 10
# wish = "Y U"
# colors = "YOBOOBRGOGYBYRYYGBO"
# patterns = "UUUUPUUPPPUUUUPUUP"

# # 运行模拟
# eliminated_turtles, additional_boxes = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)
# print("Additional blind boxes earned:", additional_boxes)


# def initialize_grid():
#     """初始化3x3网格"""
#     return [[None] * 3 for _ in range(3)]

# def check_all_different(grid):
#     """检查网格中的乌龟是否全部不同"""
#     turtles = [turtle for row in grid for turtle in row if turtle]
#     return len(turtles) == len(set(turtles))

# def find_three_of_a_kind(grid):
#     """检查是否有三个相同的乌龟在一行、一列或对角线上"""
#     # 检查行
#     for row in grid:
#         if row[0] == row[1] == row[2]:
#             return 5
#     # 检查列
#     for col in range(3):
#         if grid[0][col] == grid[1][col] == grid[2][col]:
#             return 5
#     # 检查对角线
#     if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
#         return 5
#     return 0

# def find_and_eliminate_pairs(grid, additional_boxes):
#     """查找并消除对子"""
#     pairs_found = False
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j] is not None:
#                 for k in range(i+1, 3):
#                     for l in range(3):
#                         if grid[k][l] == grid[i][j] and grid[k][l] is not None and (k, l) != (i, j):
#                             grid[i][j] = None
#                             grid[k][l] = None
#                             additional_boxes += 1
#                             pairs_found = True
#     return additional_boxes, pairs_found

# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = initialize_grid()
#     eliminated_turtles = []
#     additional_boxes = 0
#     current_turtle_index = 0

#     # 处理初始盲盒
#     for _ in range(min(initial_boxes, 9)):
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] is None:
#                     grid[i][j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#     # 检查特殊条件
#     all_different = check_all_different(grid)
#     three_of_a_kind_points = find_three_of_a_kind(grid)
#     additional_boxes += all_different * 5 + three_of_a_kind_points

#     # 继续处理额外的盲盒
#     while current_turtle_index < len(colors) and additional_boxes > 0:
#         additional_boxes -= 1
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] is None:
#                     grid[i][j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#         # 检查特殊条件
#         all_different = check_all_different(grid)
#         three_of_a_kind_points = find_three_of_a_kind(grid)
#         additional_boxes += all_different * 5 + three_of_a_kind_points
#         additional_boxes_from_pairs, pairs_found = find_and_eliminate_pairs(grid, additional_boxes)
#         if pairs_found:
#             additional_boxes += additional_boxes_from_pairs

#     # 消除剩余的乌龟
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles, additional_boxes

# # 示例输入
# initial_boxes = 10
# wish = "Y U"
# colors = "YOBOOBRGOGYBYRYYGBO"
# patterns = "UUUUPUUPPPUUUUPUUP"

# # 运行模拟
# eliminated_turtles, additional_boxes = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)
# print("Additional blind boxes earned:", additional_boxes)

# def initialize_grid():
#     """初始化3x3网格"""
#     return [[None] * 3 for _ in range(3)]

# def check_all_different(grid):
#     """检查网格中的乌龟是否全部不同"""
#     turtles = [turtle for row in grid for turtle in row if turtle]
#     return len(turtles) == len(set(turtles))

# def find_three_of_a_kind(grid):
#     """检查是否有三个相同的乌龟在一行、一列或对角线上"""
#     three_of_a_kind = 0
#     # 检查行
#     for row in grid:
#         if row[0] == row[1] == row[2]:
#             three_of_a_kind += 1
#     # 检查列
#     for col in range(3):
#         if grid[0][col] == grid[1][col] == grid[2][col]:
#             three_of_a_kind += 1
#     # 检查对角线
#     if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
#         three_of_a_kind += 1
#     return three_of_a_kind

# def find_and_eliminate_pairs(grid):
#     """查找并消除对子"""
#     pairs = []
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j] is not None:
#                 for k in range(i+1, 3):
#                     for l in range(j+1, 3):
#                         if grid[i][j] == grid[k][l] and grid[k][l] is not None:
#                             pairs.append(((i, j), (k, l)))
#                             grid[i][j] = None
#                             grid[k][l] = None
#     return pairs

# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = initialize_grid()
#     eliminated_turtles = []
#     additional_boxes = 0
#     current_turtle_index = 0

#     # 处理初始盲盒，直到网格满或处理完所有盲盒
#     for i in range(min(initial_boxes, 9)):
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for row in grid:
#             for j in range(3):
#                 for i in range(3):
#                     if row[j][i] is None:
#                         row[j][i] = (color, pattern)
#                         if (color, pattern) == wish:
#                             additional_boxes += 1
#                         break
#             else:
#                 continue
#             break

#     # 检查特殊条件
#     if check_all_different(grid):
#         additional_boxes += 5
#     three_of_a_kind = find_three_of_a_kind(grid)
#     additional_boxes += three_of_a_kind * 5

#     pairs = find_and_eliminate_pairs(grid)
#     for pair in pairs:
#         additional_boxes += 1
#         eliminated_turtles.extend([grid[pair[0][0]][pair[0][1]], grid[pair[1][0]][pair[1][1]]])

#     # 继续处理额外的盲盒
#     while current_turtle_index < len(colors) and additional_boxes > 0:
#         additional_boxes -= 1
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] is None:
#                     grid[i][j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#         # 检查特殊条件
#         if check_all_different(grid):
#             additional_boxes += 5
#         three_of_a_kind = find_three_of_a_kind(grid)
#         additional_boxes += three_of_a_kind * 5

#         pairs = find_and_eliminate_pairs(grid)
#         for pair in pairs:
#             additional_boxes += 1
#             eliminated_turtles.extend([grid[pair[0][0]][pair[0][1]], grid[pair[1][0]][pair[1][1]]])

#     # 消除剩余的乌龟
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles, additional_boxes

# # 示例输入
# initial_boxes = 10
# wish = ("R", 'U')
# colors = "YOBOOBRGOGYBYRYYGBO"
# patterns = "UUUUPUUPPPUUUUPUUPU"

# # 运行模拟
# eliminated_turtles, additional_boxes = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)
# print("Additional blind boxes earned:", additional_boxes)

# def initialize_grid():
#     """初始化3x3网格"""
#     return [[None] * 3 for _ in range(3)]

# def check_all_different(grid):
#     """检查网格中的乌龟是否全部不同"""
#     turtles = [turtle for row in grid for turtle in row if turtle]
#     return len(turtles) == len(set(turtles))

# def find_three_of_a_kind(grid):
#     """检查是否有三个相同的乌龟在一行、一列或对角线上"""
#     three_of_a_kind = 0
#     # 检查行
#     for row in grid:
#         if row[0] == row[1] == row[2]:
#             three_of_a_kind += 1
#     # 检查列
#     for col in range(3):
#         if grid[0][col] == grid[1][col] == grid[2][col]:
#             three_of_a_kind += 1
#     # 检查对角线
#     if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
#         three_of_a_kind += 1
#     return three_of_a_kind

# def find_and_eliminate_pairs(grid):
#     """查找并消除对子"""
#     pairs = []
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j] is not None:
#                 for k in range(i+1, 3):
#                     for l in range(j+1, 3):
#                         if grid[i][j] == grid[k][l] and grid[k][l] is not None:
#                             pairs.append(((i, j), (k, l)))
#                             grid[i][j] = None
#                             grid[k][l] = None
#     return pairs

# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = initialize_grid()
#     eliminated_turtles = []
#     additional_boxes = 0
#     current_turtle_index = 0

#     # 处理初始盲盒，直到网格满或处理完所有盲盒
#     for i in range(min(initial_boxes, 9)):
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         row = i // 3
#         col = i % 3
#         grid[row][col] = (color, pattern)
#         if (color, pattern) == wish:
#             additional_boxes += 1

#     # 检查特殊条件
#     if check_all_different(grid):
#         additional_boxes += 5
#     three_of_a_kind = find_three_of_a_kind(grid)
#     additional_boxes += three_of_a_kind * 5

#     pairs = find_and_eliminate_pairs(grid)
#     for pair in pairs:
#         additional_boxes += 1
#         eliminated_turtles.extend([grid[pair[0][0]][pair[0][1]], grid[pair[1][0]][pair[1][1]]])

#     # 继续处理额外的盲盒
#     while current_turtle_index < len(colors) and additional_boxes > 0:
#         additional_boxes -= 1
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] is None:
#                     grid[i][j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#         # 检查特殊条件
#         if check_all_different(grid):
#             additional_boxes += 5
#         three_of_a_kind = find_three_of_a_kind(grid)
#         additional_boxes += three_of_a_kind * 5

#         pairs = find_and_eliminate_pairs(grid)
#         for pair in pairs:
#             additional_boxes += 1
#             eliminated_turtles.extend([grid[pair[0][0]][pair[0][1]], grid[pair[1][0]][pair[1][1]]])

#     # 消除剩余的乌龟
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles, additional_boxes

# # 示例输入
# initial_boxes = 10
# wish = "Y U"
# colors = "YOBOOBRGOGYBYRYYGBO"
# patterns = "UUUUPUUPPPUUUUPUUP"

# # 运行模拟
# eliminated_turtles, additional_boxes = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)
# print("Additional blind boxes earned:", additional_boxes)

# def initialize_grid():
#     return [[None for _ in range(3)] for _ in range(3)]

# def fill_grid(grid, turtles, wish, additional_boxes):
#     for i in range(min(9, len(turtles))):
#         color, pattern = turtles[i]
#         placed = False
#         for row in grid:
#             for j in range(3):
#                 if row[j] is None:
#                     row[j] = (color, pattern)
#                     placed = True
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             if placed:
#                 break
#     return additional_boxes

# def check_grid(grid, wish, eliminated_turtles, additional_boxes):
#     # Check for all different
#     if check_all_different(grid):
#         additional_boxes += 5

#     # Check for three of a kind
#     three_of_a_kind = find_three_of_a_kind(grid)
#     additional_boxes += three_of_a_kind * 5

#     # Check for pairs and eliminate them
#     pairs = find_and_eliminate_pairs(grid)
#     for pair in pairs:
#         eliminated_turtles.extend([pair[0], pair[1]])
#         additional_boxes += 1  # Reward an additional blind box for each pair

#     return additional_boxes

# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = initialize_grid()
#     eliminated_turtles = []
#     additional_boxes = 0
#     current_turtle_index = 0

#     # Fill the grid with initial blind boxes
#     additional_boxes = fill_grid(grid, zip(colors, patterns), wish, additional_boxes)

#     # Check the grid after filling initial boxes
#     additional_boxes = check_grid(grid, wish, eliminated_turtles, additional_boxes)

#     # Continue the game with additional blind boxes if any
#     while current_turtle_index < len(colors) and additional_boxes > 0:
#         additional_boxes -= 1
#         color, pattern = colors[current_turtle_index], patterns[current_turtle_index]
#         current_turtle_index += 1
#         for row in grid:
#             for j in range(3):
#                 if row[j] is None:
#                     row[j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#         # Check the grid after placing each additional blind box
#         additional_boxes = check_grid(grid, wish, eliminated_turtles, additional_boxes)

#     # Collect remaining turtles
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles, additional_boxes

# # Example input
# initial_boxes = 10
# wish = ("R", "U")
# colors = "YOBOOBRGOGYBYRYYGBO"
# patterns = "UUUUPUUPPPUUUUPUUP"

# # Run the simulation
# eliminated_turtles, additional_boxes = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)
# print("Additional blind boxes earned:", additional_boxes)

# def initialize_grid():
#     """初始化3x3网格"""
#     return [[None for _ in range(3)] for _ in range(3)]

# def check_all_different(grid):
#     """检查网格中的乌龟是否全部不同"""
#     turtles = [turtle for row in grid for turtle in row if turtle]
#     return len(turtles) == len(set(turtles))

# def find_three_of_a_kind(grid):
#     """检查是否有三个相同的乌龟在一行、一列或对角线上"""
#     three_of_a_kind = 0
#     # 检查行
#     for row in grid:
#         if row[0] == row[1] == row[2]:
#             three_of_a_kind += 1
#     # 检查列
#     for col in range(3):
#         if grid[0][col] == grid[1][col] == grid[2][col]:
#             three_of_a_kind += 1
#     # 检查对角线
#     if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
#         three_of_a_kind += 1
#     return three_of_a_kind

# def find_and_eliminate_pairs(grid, eliminated_turtles):
#     """查找并消除对子"""
#     pairs = []
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j] is not None:
#                 for k in range(i+1, 3):
#                     for l in range(j+1, 3):
#                         if grid[i][j] == grid[k][l] and grid[k][l] is not None:
#                             pairs.append(((grid[i][j], (i, j)), (grid[k][l], (k, l))))
#                             grid[i][j] = None
#                             grid[k][l] = None
#                             eliminated_turtles.extend([grid[i][j], grid[k][l]])
#     return pairs

# def fill_grid(grid, turtles, wish, additional_boxes, eliminated_turtles):
#     """填充网格"""
#     for i, (color, pattern) in enumerate(turtles):
#         row, col = divmod(i, 3)
#         if grid[row][col] is None:
#             grid[row][col] = (color, pattern)
#             if (color, pattern) == wish:
#                 additional_boxes += 1
#     return additional_boxes

# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = initialize_grid()
#     eliminated_turtles = []
#     additional_boxes = 0
#     current_turtle_index = 0

#     # Fill the grid with initial blind boxes
#     turtles = list(zip(colors, patterns))  # Convert zip object to list
#     additional_boxes = fill_grid(grid, turtles[:min(initial_boxes, 9)], wish, additional_boxes, eliminated_turtles)

#     # Check the grid after filling initial boxes
#     additional_boxes = check_grid(grid, wish, eliminated_turtles, additional_boxes)

#     # Continue the game with additional blind boxes if any
#     while current_turtle_index < len(turtles) and additional_boxes > 0:
#         additional_boxes -= 1
#         color, pattern = turtles[current_turtle_index]
#         current_turtle_index += 1
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] is None:
#                     grid[i][j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#         # Check the grid after placing each additional blind box
#         additional_boxes = check_grid(grid, wish, eliminated_turtles, additional_boxes)

#     # Collect remaining turtles
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles, additional_boxes

# # Example input
# initial_boxes = 10
# wish = ("R", "U")
# colors = "YOBOOBRGOGYBYRYYGBO"
# patterns = "UUUUPUUPPPUUUUPUUP"

# # Run the simulation
# eliminated_turtles, additional_boxes = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)
# print("Additional blind boxes earned:", additional_boxes)


# def initialize_grid():
#     """初始化3x3网格"""
#     return [[None for _ in range(3)] for _ in range(3)]

# def check_all_different(grid):
#     """检查网格中的乌龟是否全部不同"""
#     turtles = [turtle for row in grid for turtle in row if turtle]
#     return len(turtles) == len(set(turtles))

# def find_three_of_a_kind(grid):
#     """检查是否有三个相同的乌龟在一行、一列或对角线上"""
#     three_of_a_kind = 0
#     # 检查行
#     for row in grid:
#         if row[0] == row[1] == row[2]:
#             three_of_a_kind += 1
#     # 检查列
#     for col in range(3):
#         if grid[0][col] == grid[1][col] == grid[2][col]:
#             three_of_a_kind += 1
#     # 检查对角线
#     if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
#         three_of_a_kind += 1
#     return three_of_a_kind

# def find_and_eliminate_pairs(grid):
#     """查找并消除对子"""
#     pairs = []
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j] is not None:
#                 for k in range(i+1, 3):
#                     for l in range(j+1, 3):
#                         if grid[i][j] == grid[k][l] and grid[k][l] is not None:
#                             pairs.append((grid[i][j], grid[k][l]))
#                             grid[i][j] = None
#                             grid[k][l] = None
#     return pairs

# def check_grid(grid, wish, eliminated_turtles, additional_boxes):
#     """检查网格并根据特殊条件更新状态"""
#     if check_all_different(grid):
#         additional_boxes += 5
#     three_of_a_kind = find_three_of_a_kind(grid)
#     additional_boxes += three_of_a_kind * 5
#     pairs = find_and_eliminate_pairs(grid)
#     for pair in pairs:
#         eliminated_turtles.extend(pair)
#         additional_boxes += 1
#     return additional_boxes

# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = initialize_grid()
#     eliminated_turtles = []
#     additional_boxes = 0
#     current_turtle_index = 0

#     # 将颜色和图案组合成乌龟列表
#     turtles = list(zip(colors, patterns))

#     # 填充网格
#     additional_boxes = fill_grid(grid, turtles[:min(initial_boxes, 9)], wish, additional_boxes)

#     # 检查网格
#     additional_boxes = check_grid(grid, wish, eliminated_turtles, additional_boxes)

#     # 继续处理额外的盲盒
#     while current_turtle_index < len(turtles) and additional_boxes > 0:
#         additional_boxes -= 1
#         color, pattern = turtles[current_turtle_index]
#         current_turtle_index += 1
#         # 填充到网格中
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] is None:
#                     grid[i][j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#         # 检查网格
#         additional_boxes = check_grid(grid, wish, eliminated_turtles, additional_boxes)

#     # 收集剩余的乌龟
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles, additional_boxes

# # 示例输入
# initial_boxes = 10
# wish = ("R", "U")
# colors = "YOBOOBRGOGYBYRYYGBO"
# patterns = "UUUUPUUPPPUUUUPUUP"

# # 运行模拟
# eliminated_turtles, additional_boxes = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)
# print("Additional blind boxes earned:", additional_boxes)

# def initialize_grid():
#     """初始化3x3网格"""
#     return [[None for _ in range(3)] for _ in range(3)]

# def check_all_different(grid):
#     """检查网格中的乌龟是否全部不同"""
#     turtles = [turtle for row in grid for turtle in row if turtle]
#     return len(turtles) == len(set(turtles))

# def find_three_of_a_kind(grid):
#     """检查是否有三个相同的乌龟在一行、一列或对角线上"""
#     three_of_a_kind = 0
#     # 检查行
#     for row in grid:
#         if row[0] == row[1] == row[2]:
#             three_of_a_kind += 1
#     # 检查列
#     for col in range(3):
#         if grid[0][col] == grid[1][col] == grid[2][col]:
#             three_of_a_kind += 1
#     # 检查对角线
#     if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
#         three_of_a_kind += 1
#     return three_of_a_kind

# def find_and_eliminate_pairs(grid):
#     """查找并消除对子"""
#     pairs = []
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j] is not None:
#                 for k in range(i+1, 3):
#                     for l in range(j+1, 3):
#                         if grid[i][j] == grid[k][l] and grid[k][l] is not None:
#                             pairs.append((grid[i][j], grid[k][l]))
#                             grid[i][j] = None
#                             grid[k][l] = None
#     return pairs

# def fill_grid(grid, turtles, wish, additional_boxes):
#     """填充网格"""
#     for i, (color, pattern) in enumerate(turtles):
#         row, col = divmod(i, 3)
#         if grid[row][col] is None:
#             grid[row][col] = (color, pattern)
#             if (color, pattern) == wish:
#                 additional_boxes += 1
#     return additional_boxes

# def check_grid(grid, wish, eliminated_turtles, additional_boxes):
#     """检查网格并根据特殊条件更新状态"""
#     if check_all_different(grid):
#         additional_boxes += 5
#     three_of_a_kind = find_three_of_a_kind(grid)
#     additional_boxes += three_of_a_kind * 5
#     pairs = find_and_eliminate_pairs(grid)
#     for pair in pairs:
#         eliminated_turtles.extend(pair)
#         additional_boxes += 1
#     return additional_boxes

# def simulate_game(initial_boxes, wish, colors, patterns):
#     grid = initialize_grid()
#     eliminated_turtles = []
#     additional_boxes = 0
#     current_turtle_index = 0

#     # 将颜色和图案组合成乌龟列表
#     turtles = list(zip(colors, patterns))

#     # 填充网格
#     additional_boxes = fill_grid(grid, turtles[:min(initial_boxes, 9)], wish, additional_boxes)

#     # 检查网格
#     additional_boxes = check_grid(grid, wish, eliminated_turtles, additional_boxes)

#     # 继续处理额外的盲盒
#     while current_turtle_index < len(turtles) and additional_boxes > 0:
#         additional_boxes -= 1
#         color, pattern = turtles[current_turtle_index]
#         current_turtle_index += 1
#         # 填充到网格中
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] is None:
#                     grid[i][j] = (color, pattern)
#                     if (color, pattern) == wish:
#                         additional_boxes += 1
#                     break
#             else:
#                 continue
#             break

#         # 检查网格
#         additional_boxes = check_grid(grid, wish, eliminated_turtles, additional_boxes)

#     # 收集剩余的乌龟
#     for row in grid:
#         for cell in row:
#             if cell:
#                 eliminated_turtles.append(cell)

#     return eliminated_turtles, additional_boxes

# # 示例输入
# initial_boxes = 10
# wish = ("R", "U")
# colors = "YOBOOBRGOGYBYRYYGBO"
# patterns = "UUUUPUUPPPUUUUPUUPU"

# # 运行模拟
# eliminated_turtles, additional_boxes = simulate_game(initial_boxes, wish, colors, patterns)
# print("Eliminated turtles:", eliminated_turtles)
# print("Additional blind boxes earned:", additional_boxes)

# 

# def simulate_turtle_game():
#     import sys
#     input = sys.stdin.read
#     data = input().splitlines()

#     # 读取输入
#     initial_boxes = int(data[0])
#     wish = data[1].split()
#     colors = data[2]
#     patterns = data[3]

#     # 生成所有可能的乌龟组合
#     all_turtles = [(colors[i], patterns[i]) for i in range(len(colors))]

#     # 初始化盲盒和网格
#     blind_boxes = []
#     grid = []

#     # 填充盲盒
#     for _ in range(initial_boxes):
#         blind_boxes.append(all_turtles.pop())

#     # 许愿机制
#     wish_reward = False
#     if (wish[0], wish[1]) in blind_boxes:
#         blind_boxes.append((wish[0], wish[1]))
#         wish_reward = True

#     # 填充网格
#     while blind_boxes and len(grid) < 9:
#         grid.append(blind_boxes.pop(0))

#     # 检查游戏结束条件
#     if not blind_boxes and len(grid) < 9:
#         print("Game ends due to no more blind boxes.")
#         return

#     # 消除和奖励规则
#     eliminated = []
#     while True:
#         # 检查所有不同的乌龟
#         if len(set(grid)) == 9:
#             grid.clear()
#             blind_boxes.extend([(wish[0], wish[1])] * 5)
#             eliminated.append("All different turtles")
#             continue

#         # 检查三连
#         for i in range(3):
#             for j in range(3):
#                 if (grid[i][j], grid[i][j+1], grid[i][j+2]).count(grid[i][j]) == 3:
#                     blind_boxes.extend([(wish[0], wish[1])] * 5)
#                     eliminated.append("Three of a kind")
#                     continue

#         # 检查对子
#         pairs = []
#         for i in range(9):
#             for j in range(i+1, 9):
#                 if grid[i] == grid[j]:
#                     pairs.append((i, j))

#         if pairs:
#             pairs.sort(key=lambda x: x[0])  # 优先移除编号较小的
#             for pair in pairs:
#                 if grid[pair[0]] == grid[pair[1]]:
#                     eliminated.extend([grid[pair[0]], grid[pair[1]]])
#                     grid[pair[0]] = None
#                     grid[pair[1]] = None
#                     blind_boxes.append((wish[0], wish[1]))
#         else:
#             break

#     # 检查是否还有盲盒
#     if not blind_boxes:
#         print("Game ends due to no more blind boxes.")
#         return

#     # 输出被淘汰的乌龟
#     for turtle in eliminated:
#         print(turtle)
#     # 输出网格中的乌龟
#     for i, turtle in enumerate(grid):
#         if turtle:
#             print(turtle)

# # 运行游戏模拟
# simulate_turtle_game()

# def simulate_turtle_game():
#     # 输入样例
#     initial_boxes = 10
#     wish = "R U"
#     colors = "YOBOOBRGOGYBYRYYGBO"
#     patterns = "UUUUPUUPPPUUUUPUUPU"

#     # 生成所有可能的乌龟组合
#     all_turtles = [(colors[i], patterns[i]) for i in range(len(colors))]

#     # 初始化盲盒和网格
#     blind_boxes = []
#     grid = []

#     # 填充盲盒
#     for _ in range(initial_boxes):
#         blind_boxes.append(all_turtles.pop(0))

#     # 许愿机制
#     if (wish.split()[0], wish.split()[1]) in blind_boxes:
#         print("Wish granted!")

#     # 填充网格
#     while blind_boxes and len(grid) < 9:
#         grid.append(blind_boxes.pop(0))

#     # 检查游戏结束条件
#     if not blind_boxes and len(grid) < 9:
#         print("Game ends due to no more blind boxes.")
#         return

#     # 消除和奖励规则
#     eliminated = []
#     while True:
#         # 检查所有不同的乌龟
#         if len(set(grid)) == 9:
#             print("All different turtles!")
#             grid.clear()
#             blind_boxes.extend([(wish.split()[0], wish.split()[1])] * 5)
#             eliminated.append("All different turtles")
#             continue

#         # 检查三连
#         for i in range(3):
#             for j in range(3):
#                 if (grid[i][j], grid[i][j+1], grid[i][j+2]).count(grid[i][j]) == 3:
#                     print("Three of a kind!")
#                     blind_boxes.extend([(wish.split()[0], wish.split()[1])] * 5)
#                     eliminated.append("Three of a kind")
#                     continue

#         # 检查对子
#         pairs = []
#         for i in range(9):
#             for j in range(i+1, 9):
#                 if grid[i] == grid[j]:
#                     pairs.append((i, j))

#         if pairs:
#             pairs.sort(key=lambda x: x[0])  # 优先移除编号较小的
#             for pair in pairs:
#                 if grid[pair[0]] == grid[pair[1]]:
#                     eliminated.extend([grid[pair[0]], grid[pair[1]]])
#                     grid[pair[0]] = None
#                     grid[pair[1]] = None
#                     blind_boxes.append((wish.split()[0], wish.split()[1]))
#         else:
#             break

#     # 输出被淘汰的乌龟
#     for turtle in eliminated:
#         print(turtle)
#     # 输出网格中的乌龟
#     for i, turtle in enumerate(grid):
#         if turtle:
#             print(turtle)

# # 运行游戏模拟
# simulate_turtle_game()



# def turtle_game_simulation():
#     import sys
#     input = sys.stdin.read
#     data = input().split()
    
#     initial_blind_boxes = int(data[0])
#     wish_color, wish_pattern = data[1], data[2]
#     colors = list(data[3])
#     patterns = list(data[4])

#     # Create a list of turtle tuples from the colors and patterns
#     turtles = [(colors[i], patterns[i]) for i in range(len(colors))]

#     # Initialize the game state
#     grid = [None] * 9
#     blind_boxes = initial_blind_boxes
#     removed_turtles = []
#     pos = 0

#     while blind_boxes > 0 and turtles:
#         # Get the next turtle from the blind box
#         current_turtle = turtles.pop(0)
#         blind_boxes -= 1
        
#         # Wish mechanism
#         if current_turtle == (wish_color, wish_pattern):
#             blind_boxes += 1
        
#         # Place the turtle in the grid
#         grid[pos] = current_turtle
#         pos += 1

#         # Check if the grid is full or no more blind boxes
#         if pos == 9 or blind_boxes == 0:
#             # Check for "All Different"
#             if None not in grid and len(set(grid)) == 9:
#                 removed_turtles.extend(grid)
#                 grid = [None] * 9
#                 pos = 0
#                 blind_boxes += 5
#                 continue
            
#             # Check for "Three of a Kind"
#             triples = [
#                 [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
#                 [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
#                 [0, 4, 8], [2, 4, 6]              # Diagonal
#             ]
#             triple_rewarded = False
#             for trip in triples:
#                 if grid[trip[0]] is not None and grid[trip[0]] == grid[trip[1]] == grid[trip[2]]:
#                     blind_boxes += 5
#                     triple_rewarded = True

#             if triple_rewarded:
#                 continue

#             # Check for "Pairs"
#             pairs_removed = False
#             for i in range(9):
#                 for j in range(i + 1, 9):
#                     if grid[i] is not None and grid[i] == grid[j]:
#                         removed_turtles.append(grid[i])
#                         grid[i] = None
#                         grid[j] = None
#                         blind_boxes += 1
#                         pairs_removed = True
#                         break  # Remove only one pair at a time
#                 if pairs_removed:
#                     break

#             # Clean up the grid from removed (None) positions
#             grid = [t for t in grid if t is not None] + [None] * (9 - len([t for t in grid if t is not None]))
#             pos = len([t for t in grid if t is not None])

#             # End condition check: no more blind boxes and no more eliminations possible
#             if blind_boxes == 0 and not triple_rewarded and not pairs_removed:
#                 break

#     # Add remaining turtles in the grid (in grid order) to removed turtles
#     remaining_turtles = [t for t in grid if t is not None]
#     removed_turtles.extend(remaining_turtles)

#     # Output the list of eliminated turtles
#     for turtle in removed_turtles:
#         print(turtle)

# # To run the function, the input must be provided via standard input:
# # turtle_game_simulation()


# def parse_input():  
# num_boxes = int(input().strip())  
#     wish = input().strip().split()  
#     colors = list(input()) 
#     patterns = list(input())
#     turtles = [(colors[i], patterns[i]) for i in range(len(colors))]  
#     return num_boxes, wish, turtles  
  
# def fill_grid(turtles):  
#     grid = [['' for _ in range(3)] for _ in range(3)]   
#     for i in range(9):  
#         grid[i // 3][i % 3] = turtles[i]  
#     return grid  
  
# def check_wish(grid, wish):  
#     for row in grid:  
#         for turtle in row:  
#             if turtle == wish:  
#                 return True  
#     return False  
  
# def check_three_of_a_kind(grid):  
#     reward_count = 0  
#     # Check rows  
#     for row in grid:  
#         if row[0] == row[1] == row[2]:  
#             reward_count += 5  
#     # Check columns  
#     for col in range(3):  
#         if grid[0][col] == grid[1][col] == grid[2][col]:  
#             reward_count += 5  
#     # Check diagonals  
#     if grid[0][0] == grid[1][1] == grid[2][2]:  
#         reward_count += 5  
#     if grid[0][2] == grid[1][1] == grid[2][0]:  
#         reward_count += 5  
#     return reward_count  
  
# def remove_pairs(grid):  
#     eliminated = []  
#     for i in range(3):  
#         for j in range(3):  
#             for k in range(i, 3):  
#                 for l in range(j, 3):  
#                     if (i != k or j != l) and grid[i][j] == grid[k][l]:  
#                         if (i, j) < (k, l):  # Prioritize lower-numbered positions  
#                             grid[k][l] = ''  
#                             eliminated.append(grid[i][j])  
#                             grid[i][j] = ''  
#     return eliminated  
  
# def print_grid(grid):  
#     for row in grid:  
#         print(row)  
  
# def main():  
#     num_boxes, wish, turtles = parse_input()  
      
#     grid = fill_grid(turtles[:9])  # Use only the first 9 turtles for the grid  
#     remaining_turtles = turtles[9:]  
      
#     extra_boxes = 0  
#     eliminated_turtles = []  
      
#     if check_wish(grid, wish):  
#         extra_boxes += 1  
      
#     while True:  
#         reward_boxes_from_three_of_a_kind = check_three_of_a_kind(grid)  
#         extra_boxes += reward_boxes_from_three_of_a_kind  
          
#         new_eliminated = remove_pairs(grid)  
#         eliminated_turtles.extend(new_eliminated)  
          
#         if not any(turtle for row in grid for turtle in row) or not remaining_turtles:  
#             break  
          
#         if extra_boxes > 0:  
#             num_new_boxes = min(extra_boxes, len(remaining_turtles))  
#             for _ in range(num_new_boxes):  
#                 new_turtle = remaining_turtles.pop(0)  
#                 # Place the new turtle in the first empty spot in the grid  
#                 for i in range(3):  
#                     for j in range(3):  
#                         if not grid[i][j]:  
#                             grid[i][j] = new_turtle  
#                             break  
#                     if grid[i][j]:  
#                         break  
#             extra_boxes -= num_new_boxes  
          
#     # Print remaining turtles in the grid (if any)  
#     for i in range(3):  
#         for j in range(3):  
#             if grid[i][j]:  
#                 eliminated_turtles.append(grid[i][j])  
      
#     print(eliminated_turtles)  
  
# if __name__ == "__main__":  
#     main()



# a = ['YP', 'YP', 'RP', 'RP', 'YP', 'YP', 'GU', 'GU', 'OP', 'OP', 'BU', 'BU', 'BP', 'BP', 'YU', 'YU', 'BU', 'RP', 'OP', 'BP', 'GP', 'YP', 'RU', 'OU', 'YU', 'YU', 'YU', 'OU', 'OU', 'OP', 'OP', 'RU', 'RU', 'GU', 'GU', 'YU', 'GP', 'OP', 'RP']
# print(list(map(lambda x: (x[0], x[1]), a)))


# box_1 = int(input())
# wish1 = input().strip()
# wish = wish1[0] + wish1[2]
# color = list(input())
# pattern = list(input())
# elim = []
# turtles = []
# for i in range(len(color)):
#     a = color[i] + pattern[i]
#     turtles.append(a)



# def all(grid):
#     # print(sum(grid,[]))
#     m11 = sum(grid,[])
#     m12 = []
#     for i in range(len(m11)):
#         if m11[i] != None:
#             m12.append(m11[i])
#     return len(set(m12)) == len(m12)
    

# def three(t):  
#     num2 = 0   
#     for i in range(3):  
#         if t[i][0] == t[i][1] == t[i][2] and t[i][0] != None:  
#             num2 += 1   
#     for i in range(3):  
#         if t[0][i] == t[1][i] == t[2][i] and t[0][i] != None:  
#             num2 += 1   
#     if t[0][0] == t[1][1] == t[2][2] and t[0][0] != None:  
#         num2 += 1    
#     if t[2][0] == t[1][1] == t[0][2] and t[2][0] != None:  
#         num2 += 1  
#     return num2
        

# def check_pairs(grid):
#     pairs1 = []
#     pairs = []
#     for i in range(3):
#         for j in range(3):
#             for m in range(3):
#                 for n in range(3):
#                     if grid[m][n] == grid[i][j] and (m, n) != (i, j) and grid[i][j] != None:
#                         pairs1.append(grid[i][j])
#                         pairs1.append(grid[m][n])
#                         grid[m][n] = None
#                         grid[i][j] = None
#     for i in pairs1:
#         if i != None:
#             pairs.append(i)
#     return pairs


        

# grid = [[None]*3 for i in range(3)]



# if box_1 >= 9:
#     for i in range(9):
#         if turtles[i] == wish:
#             box_1 += 1
#     for i in range(3):
#             for j in range(3):
#                 grid[i][j] = turtles[0]
#                 turtles.remove(turtles[0])
#     box_1 -= 9
# else:
#     num10 = 0
#     for i in range(3):
#             for j in range(3):
#                 if num10 < box_1:
#                     grid[i][j] = turtles[0]
#                     if turtles[i] == wish:
#                         box_1 += 1
#                     turtles.remove(turtles[0])
#                     num10 += 1
#     box_1 = 0                
            


# while box_1 >= 0 and turtles:
#     if all(grid):
#         box_1 += 5
#         elim.extend(grid)
#         grid = [[None]*3 for i in range(3)]
#         for i in range(3):
#             if not turtles:
#                 break
#             for j in range(3):
#                 if grid[i][j] == None:
#                     grid[i][j] = turtles[0]
#                     if turtles[0] == wish:
#                         box_1 += 1
#                     turtles.remove(turtles[0])
#                     box_1 -= 1
#     if three(grid) != 0:
#         box_1 += 5*three(grid)
#     pairs = check_pairs(grid)
#     if pairs:
#         elim.extend(pairs)
#         box_1 += len(pairs) / 2
#         for i in range(3):
#             if not turtles:
#                 break
#             if box_1 == 0:
#                 break
#             for j in range(3):
#                 if grid[i][j] == None:
#                     grid[i][j] = turtles[0]
#                     if turtles[0] == wish:
#                         box_1 += 1
#                     turtles.remove(turtles[0])
#                     box_1 -= 1


# pairs = check_pairs(grid)
# elim.extend(pairs)
        


# for i in range(3):
#         for j in range(3):
#             if grid[i][j] is not None:
#                 elim.append(grid[i][j])


# def flat(a):
#     l= []
#     for i in a:
#         if type(i) is list:
#             for j in i:
#                 l.append(j)
#         else:
#             l.append(i)
#     return(l)

# eliminated_turtles = flat(elim)

# for i in range(len(eliminated_turtles)):
#     eliminated_turtles[i] = (eliminated_turtles[i][0], eliminated_turtles[i][1])

# print(eliminated_turtles)

# seq = []
#         # seq1 = seq.extend(seq1)
#         # seq2 = seq.extend(seq2)
# from collections import Iterable
# def piz(seq1, seq2):
#     if isinstance(seq1, Iterable) and isinstance(seq2, Iterable):
#         seq1 = list(seq1)
#         seq2 = list(seq2)
#     if type(seq1) == list == type(seq2):
#         if len(seq1) == len(seq2):
#             for i in range(len(seq1)):
#                 seq.append((seq1[i], seq2[i]))
#         elif len(seq1) < len(seq2):
#             for i in range(len(seq2)-len(seq1)):
#                 seq1.append(i)
#                 seq.append((seq1[i], seq2[i]))
#         elif len(seq1) > len(seq2):
#             for i in range(-len(seq2)+ len(seq1)):
#                 seq2.append(i)
#                 seq.append((seq1[i], seq2[i]))
#     if type(seq1) == list and not seq2 :
#         seq2 = []
#         if len(seq1) == len(seq2):
#             for i in range(len(seq1)):
#                 seq.append((seq1[i], seq2[i]))
#         elif len(seq1) < len(seq2):
#             for i in range(len(seq2)-len(seq1)):
#                 seq1.append(i)
#                 seq.append((seq1[i], seq2[i]))
#         elif len(seq1) > len(seq2):
#             for i in range(-len(seq2)+ len(seq1)):
#                 seq2.append(i)
#                 seq.append((seq1[i], seq2[i]))


# def piz(seq3):
#     seq1 = seq3
#     seq2 = []
#     for i in range(len(seq1)):
#                     seq2.append(i)
#                     seq.append((seq1[i], seq2[i]))
#     return seq





# def piz(p1=None, p2=None):
#     def is_iter(obj):
#         try:
#             iter(obj)
#             return True
#         except TypeError:
#             return False
#     # Check the types of the parameters
#     inputs = [p1, p2]
#     for i, p in enumerate(inputs):
#         if p is not None and not is_iter(p):
#             raise TypeError(f"Find a non-iterable object {type(p).__name__}. Bad ++C Committee!")

#     # Handle cases where either parameter is None
#     s1 = list(p1) if p1 is not None else []
#     s2 = list(p2) if p2 is not None else []
    
#     # If both sequences are lists, retain their original reference for extension
#     if isinstance(p1, list):
#         seq1 = s1
#     else:
#         seq1 = list(p1)
    
#     if isinstance(p2, list):
#         seq2 = s2
#     else:
#         seq2 = list(p2)
    
#     # Extend the shorter list
#     len1, len2 = len(seq1), len(seq2)
#     if len1 < len2:
#         seq1.extend(range(len1, len2))
#     elif len2 < len1:
#         seq2.extend(range(len2))
    
#     # Create the result as a list of tuples
#     result = [(seq1[i], seq2[i]) for i in range(max(len(seq1), len(seq2)))]

#     # If one of the parameters was not a list and is iterable, include a warning message
#     for param in inputs:
#         if param is not None and not isinstance(param, list) and is_iter(param):
#             return result + [f"Find a non-list but iterable object {type(param).__name__}. Bad ++C Committee!"]

#     return result

# piz([1, 2, 3], [4, 5, 6])

# def search_social_tree(social_tree, target_r, oracle, path = []):
# 	for k, v in social_tree.items():
# 		# form the current social path (add k to current path)
# 		path = path + [k]
# 		# check if it satisfies oracle, if so, return something
# 		if target_r == oracle(path):
# 			return k
# 		# otherwise , search the elements in v (recursion)
# 		elif isinstance(v, dict):
# 			if search_social_tree(v, target_r, oracle, path):
# 				return path[-1]

# 		# if find a solution in v, return something
# 	return "!"
# 	# return something after iteration

def search_social_tree(social_tree, r, func):
    def dfs(tree, path):
        for person, relations in tree.items():
            current_path = path + [person]
            # 检查当前路径是否满足条件
            if func(len(current_path)) == r:
                return person  # 找到符合条件的人
            # 递归遍历关系
            result = dfs(relations, current_path)
            if result:
                return result
        return None

    # 从主角开始遍历社交树
    result = dfs(social_tree, [])
    return result if result else "!"  # 如果没有找到，返回 "!"
