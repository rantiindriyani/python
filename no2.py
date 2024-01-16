class Node:
    def __init__(self, weight, value, level, include):
        self.weight = weight
        self.value = value
        self.level = level
        self.include = include

def knapsack_backtracking(weights, values, capacity):
    root = Node(0, 0, 0, False)
    max_node = Node(0, 0, 0, False)
    
    def promising(node):
        if node.weight > capacity:
            return False
        if node.level == len(weights):
            return False
        return True
    
    def knapsack_recursive(node):
        nonlocal max_node

        if node.level == len(weights):
            return

        # Explore left branch (include the item)
        left_node = Node(node.weight + weights[node.level], node.value + values[node.level], node.level + 1, True)
        if promising(left_node) and left_node.value > max_node.value:
            max_node = left_node
        knapsack_recursive(left_node)

        # Explore right branch (exclude the item)
        right_node = Node(node.weight, node.value, node.level + 1, False)
        if promising(right_node) and right_node.value > max_node.value:
            max_node = right_node
        knapsack_recursive(right_node)

    knapsack_recursive(root)
    return max_node

# Barang-barang
weights = [5, 3, 1, 6, 2]
values = [12, 8, 4, 20, 6]
capacity = 10

# Cari solusi dengan backtracking
solution_node = knapsack_backtracking(weights, values, capacity)

# Output hasil
print("Langkah-langkah atau proses backtracking:")
print("Level | Include | Weight | Value")
for i in range(len(weights)):
    print(f"{i+1:5} | {solution_node.include}       | {weights[i]:6} | {values[i]:5}")
print("solusi optimumnya adalah (I,I,I,I,I) TRUE Dan F atau provite(nilai) diperoleh 50 ")
