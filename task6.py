import matplotlib.pyplot as plt

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"]/x[1]["cost"], reverse=True)
    chosen = []
    total_cost = 0
    total_calories = 0
    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            chosen.append(name)
            total_cost += info["cost"]
            total_calories += info["calories"]
    return chosen, total_calories, total_cost


# Динамічне програмування
def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0]*(budget+1) for _ in range(n+1)]

    for i in range(1, n+1):
        name, info = item_list[i-1]
        cost = info["cost"]
        calories = info["calories"]
        for w in range(budget+1):
            if cost > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)

    # Відновлення вибраних страв
    w = budget
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            name, info = item_list[i-1]
            chosen.append(name)
            w -= info["cost"]
    chosen.reverse()
    total_calories = dp[n][budget]
    total_cost = sum(items[name]["cost"] for name in chosen)
    return chosen, total_calories, total_cost


# Візуалізація результатів
def visualize_results(items, greedy_result, dp_result):
    methods = ["Greedy", "Dynamic Programming"]
    totals_calories = [greedy_result[1], dp_result[1]]
    totals_cost = [greedy_result[2], dp_result[2]]
    
    fig, ax = plt.subplots(1, 2, figsize=(12,5))
    
    # Калорійність
    ax[0].bar(methods, totals_calories, color=['skyblue','lightgreen'])
    ax[0].set_title("Сумарна калорійність")
    ax[0].set_ylabel("Калорії")
    
    # Витрати
    ax[1].bar(methods, totals_cost, color=['salmon','orange'])
    ax[1].set_title("Сумарна вартість")
    ax[1].set_ylabel("Вартість")
    
    plt.show()

    # Виведення деталей
    for method, result in zip(methods, [greedy_result, dp_result]):
        chosen, calories, cost = result
        print(f"\nМетод: {method}")
        print(f"Вибрані страви: {chosen}")
        print(f"Сумарна калорійність: {calories} ккал")
        print(f"Сумарна вартість: {cost} грн")


# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

visualize_results(items, greedy_result, dp_result)
