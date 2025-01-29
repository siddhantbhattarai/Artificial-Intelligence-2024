### Exercise 1: Breadth-First Search (BFS)

**Task 1: Change the starting and ending point and observe the problem solution.**

To change the starting and ending points, you simply need to modify the `start_node` and `goal_node` variables in the script. For example:

```python
start_node = 'B'  # Change the starting node
goal_node = 'F'   # Change the goal node
result = bfs(graph, start_node, goal_node)
if result:
    print("Path found:", result)
else:
    print("No path found.")
```

**Task 2: Use the time library to calculate how long it takes to solve the problem using three different starting points and ending points.**

You can use the `time` module to measure the time taken by the BFS algorithm. Here's an example:

```python
import time

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Define different starting and ending points
start_goals = [('A', 'E'), ('B', 'F'), ('C', 'D')]

for start, goal in start_goals:
    start_time = time.time()
    result = bfs(graph, start, goal)
    end_time = time.time()
    if result:
        print(f"Path found from {start} to {goal}: {result}, Time taken: {end_time - start_time:.6f} seconds")
    else:
        print(f"No path found from {start} to {goal}, Time taken: {end_time - start_time:.6f} seconds")
```

**Task 3: Change the script to model the following graph:**

To model the new graph, update the `graph` dictionary:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'H'],
    'G': ['D'],
    'H': ['F']
}

# Now you can run BFS on this new graph
start_node = 'A'
goal_node = 'H'
result = bfs(graph, start_node, goal_node)
if result:
    print("Path found:", result)
else:
    print("No path found.")
```

### Exercise 2: Depth-First Search (DFS)

**Task 1: Compare the time to find the solution using both algorithms and graphs.**

You can use the same approach as in Exercise 1 to measure the time taken by DFS. Here's an example:

```python
import time

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Define different starting and ending points
start_goals = [('A', 'E'), ('B', 'F'), ('C', 'D')]

for start, goal in start_goals:
    start_time = time.time()
    result = dfs(graph, start, goal)
    end_time = time.time()
    if result:
        print(f"Path found from {start} to {goal}: {result}, Time taken: {end_time - start_time:.6f} seconds")
    else:
        print(f"No path found from {start} to {goal}, Time taken: {end_time - start_time:.6f} seconds")
```

**Task 2: Change the starting and ending point and observe the problem solution.**

You can change the `start_node` and `goal_node` variables as shown in Exercise 1.

### Exercise 3: Limited Depth DFS (LDS)

**Task 1: Change the max depth and find how to break the algorithm.**

You can experiment with different values of `max_depth` to see how it affects the algorithm. For example:

```python
max_depth = 2  # Change the max depth
result = dls(graph, start_node, goal_node, max_depth)
if result:
    print("Path found:", result)
else:
    print("No path found.")
```

**Task 2: Make your own graph with many layers and compare the different algorithms.**

You can create a more complex graph and compare the performance of BFS, DFS, and LDS. Here's an example:

```python
# Define a more complex graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J'],
    'G': ['C', 'K'],
    'H': ['D'],
    'I': ['E'],
    'J': ['F'],
    'K': ['G']
}

# Compare BFS, DFS, and LDS
start_node = 'A'
goal_node = 'K'

# BFS
start_time = time.time()
result = bfs(graph, start_node, goal_node)
end_time = time.time()
print(f"BFS Path found: {result}, Time taken: {end_time - start_time:.6f} seconds")

# DFS
start_time = time.time()
result = dfs(graph, start_node, goal_node)
end_time = time.time()
print(f"DFS Path found: {result}, Time taken: {end_time - start_time:.6f} seconds")

# LDS
max_depth = 5
start_time = time.time()
result = dls(graph, start_node, goal_node, max_depth)
end_time = time.time()
print(f"LDS Path found: {result}, Time taken: {end_time - start_time:.6f} seconds")
```

### Exercise 4: Maze Problem

**Task 1: Compare BFS and DFS for the maze problem.**

You can use the provided `bfs_maze` and `dfs_maze` functions to solve the maze and compare their performance:

```python
import time

# Define the maze
maze = [
    ['S', '.', '.', '.', '.', '.', '#', '.', '.'],
    ['#', '#', '#', '#', '#', '.', '#', '#', '#'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'G'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#']
]

# Starting and goal positions
start_position = (0, 0)
goal_position = (2, 8)

# BFS
start_time = time.time()
result = bfs_maze(maze, start_position, goal_position)
end_time = time.time()
print(f"BFS Result: {result}, Time taken: {end_time - start_time:.6f} seconds")

# DFS
start_time = time.time()
result = dfs_maze(maze, start_position, goal_position)
end_time = time.time()
print(f"DFS Result: {result}, Time taken: {end_time - start_time:.6f} seconds")
```

**Task 2: Try different starting and ending points and calculate the number of steps needed to solve the problem.**

You can change the `start_position` and `goal_position` variables and run the algorithms again.

**Task 3: Change the maze map to make it much larger and repeat the comparison.**

You can create a larger maze and repeat the comparison:

```python
# Define a larger maze
maze = [
    ['S', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['#', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'G']
]

# Starting and goal positions
start_position = (0, 0)
goal_position = (4, 9)

# BFS
start_time = time.time()
result = bfs_maze(maze, start_position, goal_position)
end_time = time.time()
print(f"BFS Result: {result}, Time taken: {end_time - start_time:.6f} seconds")

# DFS
start_time = time.time()
result = dfs_maze(maze, start_position, goal_position)
end_time = time.time()
print(f"DFS Result: {result}, Time taken: {end_time - start_time:.6f} seconds")
```

### Conclusion

By following these steps, you should be able to complete all the exercises in the assignment. Make sure to test your code thoroughly and document your findings. Good luck!
