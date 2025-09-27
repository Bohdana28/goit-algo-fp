import random
import matplotlib.pyplot as plt

#Параметри симуляції
num_rolls = 100000 # Кількість імітацій кидання кубиків
sum_counts = {i:0 for i in range(2, 13)} # Підрахунок сум від 2 до 12

# Імітація кидань кубиків методом Монте-Карло
for _ in range(num_rolls):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    sum_counts[total] += 1

# Обчислення ймовірностей
monte_carlo_probs = {s: count/num_rolls for s, count in sum_counts.items()}

# Аналітичні ймовірності
analytical_probs = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Вивід таблиці порівняння
print(f"{'Сума':<5}{'Монте-Карло %':<15}{'Аналітична %':<15}")
for s in range(2, 13):
    mc_prob = monte_carlo_probs[s]*100
    an_prob = analytical_probs[s]*100
    print(f"{s:<5}{mc_prob:<15.2f}{an_prob:<15.2f}")

# Побудова графіку та збереження
sums = list(range(2, 13))
mc_values = [monte_carlo_probs[s]*100 for s in sums]
analytical_values = [analytical_probs[s]*100 for s in sums]

plt.figure(figsize=(10,6))
plt.bar(sums, mc_values, width=0.4, label='Монте-Карло', alpha=0.7, color='skyblue')
plt.bar([s+0.4 for s in sums], analytical_values, width=0.4, label='Аналітична', alpha=0.7, color='orange')
plt.xlabel("Сума на двох кубиках")
plt.ylabel("Ймовірність (%)")
plt.title(f"Ймовірності сум при киданні двох кубиків ({num_rolls} симуляцій)")
plt.xticks([s+0.2 for s in sums], sums)
plt.legend()

# Збереження графіку у файл для readme
plt.savefig("dice_probs.png")
plt.show()
