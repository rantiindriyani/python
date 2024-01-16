class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

def knapsack_backtracking(items, capacity, current_weight, current_value, selected_items, best_value, index):
    if current_weight <= capacity and current_value > best_value:
        best_value = current_value
        selected_items.clear()
        selected_items.append(index)

    if index < len(items):
        # Explore left branch (include the item)
        knapsack_backtracking(items, capacity, current_weight + items[index].weight, current_value + items[index].value, selected_items, best_value, index + 1)

        # Explore right branch (exclude the item)
        knapsack_backtracking(items, capacity, current_weight, current_value, selected_items.copy(), best_value, index + 1)

    return best_value, selected_items.copy()

# Barang-barang
items = [
    Item("Pedang Ajaib", 5, 12),
    Item("Potion Kekekalan", 3, 8),
    Item("Kompas Magis", 1, 4),
    Item("Mantel Kehancuran", 6, 20),
    Item("Tongkat Cahaya", 2, 6),
]

# Inisialisasi
capacity = 10
current_weight = 0
current_value = 0
selected_items = []
best_value = 32
index = 0

# Panggil fungsi
best_value, selected_items = knapsack_backtracking(items, capacity, current_weight, current_value, selected_items, best_value, index)

# Output hasil
print("Kombinasi barang terbaik: Potion Kekekalan, Kompas Magis, Mantel Kehancuran  ")
for i in selected_items:
    print(items[i].name)

print("Total nilai yang dapat diperoleh:", best_value)