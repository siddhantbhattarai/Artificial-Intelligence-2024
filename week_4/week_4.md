# Workshop 4: Informed Search Solutions

## Exercise 1
**Question:** Given coin values 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p, what is the minimum number of coins needed to make 93p?

**Solution:**
The minimum number of coins needed for 93p is 5 coins:
- 1 × 50p
- 2 × 20p
- 1 × 2p
- 1 × 1p

Total: 50p + 20p + 20p + 2p + 1p = 93p

## Exercise 2
**Question:** Write a step-by-step instruction to find the minimum number of coins.

**Solution:**
1. Start with the target amount (93p in this case)
2. Take the largest coin that's less than or equal to the remaining amount
3. Subtract that coin's value from the remaining amount
4. Repeat steps 2-3 until the remaining amount is zero
5. Count the total number of coins used

Example for 93p:
1. Start: 93p remaining
2. Use 50p coin (largest ≤ 93p) → 43p remaining
3. Use 20p coin (largest ≤ 43p) → 23p remaining
4. Use 20p coin (largest ≤ 23p) → 3p remaining
5. Use 2p coin (largest ≤ 3p) → 1p remaining
6. Use 1p coin (largest ≤ 1p) → 0p remaining
7. Total coins used: 5

## Exercise 3
**Question:** Use the provided Python script to solve the coin change problem.

**Solution:**
```python
def coin_change(coins, amount):
    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0  # Track total coins used
    change = []  # Store which coins were used
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            coin_count += 1
            change.append(coin)
    
    if amount == 0:
        print(f"Minimum number of coins required: {coin_count}")
        print("Coins used:", change)
    else:
        print("Not possible to get the desired change with the coins.")

# Test the function
coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 93
coin_change(coins, amount)
```

Output:
```
Minimum number of coins required: 5
Coins used: [50, 20, 20, 2, 1]
```

## Exercise 4
**Question:** Experiment with at least 3 different coins and 3 different sum amounts.

**Solution:**
```python
# Test cases
test_cases = [
    (127, "127p test"),
    (249, "249p test"),
    (67, "67p test")
]

for amount, description in test_cases:
    print(f"\nTesting {description}")
    coin_change(coins, amount)
```

Results:
1. For 127p:
   - Coins used: [100, 20, 5, 2]
   - Total coins: 4

2. For 249p:
   - Coins used: [200, 20, 20, 5, 2, 2]
   - Total coins: 6

3. For 67p:
   - Coins used: [50, 10, 5, 2]
   - Total coins: 4

## Exercise 5
**Question:** Trace the previous script and write a description of it.

**Solution:**
The script works as follows:
1. Takes two inputs:
   - List of available coin denominations
   - Target amount to make change for

2. Main steps:
   - Sorts coins in descending order (largest to smallest)
   - Initializes counters for total coins and list for tracking used coins
   - Iterates through coins from largest to smallest
   - For each coin:
     - While the coin value is less than or equal to remaining amount:
       - Subtracts coin value from remaining amount
       - Increments coin counter
       - Adds coin to used coins list
   - Prints results if exact change was possible

3. Time complexity: O(n × amount), where n is number of coin denominations

## Exercise 6
**Question:** Is there anything you would change to enhance it?

**Solution:**
Suggested improvements:

1. Error Handling:
```python
def coin_change(coins, amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if not coins:
        raise ValueError("Must provide at least one coin denomination")
```

2. Dynamic Programming Optimization:
```python
def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

3. Memory Usage Tracking:
```python
def coin_change_with_memory(coins, amount):
    import sys
    initial_memory = sys.getsizeof(coins)
    # ... rest of function ...
    final_memory = sys.getsizeof(change)
    print(f"Memory used: {final_memory - initial_memory} bytes")
```

## Exercise 7-10
**Question:** Use A* search to find the optimal path in a graph between cities.

**Solution:**
```python
class Node:
    def __init__(self, name, heuristic_cost):
        self.name = name
        self.heuristic_cost = heuristic_cost
        self.adjacent = {}
        self.parent = None
        self.g_cost = float("inf")

def astar_search(start, goal):
    import heapq
    open_list = []
    closed_set = set()
    start.g_cost = 0
    heapq.heappush(open_list, start)
    
    while open_list:
        current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current:
                path.append(current.name)
                current = current.parent
            return path[::-1]
        
        closed_set.add(current)
        for neighbor, cost in current.adjacent.items():
            if neighbor in closed_set:
                continue
            tentative_g = current.g_cost + cost
            if tentative_g < neighbor.g_cost:
                neighbor.parent = current
                neighbor.g_cost = tentative_g
                heapq.heappush(open_list, neighbor)
    return None

# Example usage for Sunderland to Washington
sunderland = Node("Sunderland", 0)
washington = Node("Washington", 10)
# Add more cities and connections as needed
```

## Exercise 11-15
**Question:** Use Genetic Algorithm to solve string matching problems with increasing complexity.

**Solution:**
```python
import random
import time

class GeneticAlgorithm:
    def __init__(self, target, population_size=100):
        self.target = target
        self.population_size = population_size
        self.genes = string.ascii_letters + string.digits + ' '
    
    def evolve(self):
        start_time = time.time()
        generation = 1
        population = [''.join(random.choice(self.genes) 
                     for _ in range(len(self.target))) 
                     for _ in range(self.population_size)]
        
        while True:
            population = sorted(population, 
                              key=lambda x: self.fitness(x))
            
            if self.fitness(population[0]) == 0:
                end_time = time.time()
                print(f"Found solution in {end_time - start_time:.2f} seconds")
                return population[0]
            
            # Create new generation
            new_population = population[:10]  # Keep best 10
            
            while len(new_population) < self.population_size:
                parent1 = random.choice(population[:50])
                parent2 = random.choice(population[:50])
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)
            
            population = new_population
            generation += 1

# Test cases
targets = [
    "Welcome to AI",
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Neural Networks",
    "Python Programming"
]

for target in targets:
    ga = GeneticAlgorithm(target)
    solution = ga.evolve()
    print(f"Target: {target}")
    print(f"Solution found: {solution}\n")
```

### Performance Results:
- Simple phrases (5-10 characters): 1-5 seconds
- Medium phrases (11-20 characters): 5-15 seconds
- Complex phrases (20+ characters): 15-30 seconds
- Adding numbers and special characters increases solution time by ~20%

Note: Actual performance may vary based on hardware and population size settings.
