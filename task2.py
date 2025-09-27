import matplotlib.pyplot as plt
import numpy as np

def draw_pythagoras_tree(ax, x, y, size, angle, level):
    if level == 0:
        return

    # Вектори для квадрата
    dx = size * np.cos(angle)
    dy = size * np.sin(angle)

    # Вершини квадрата
    x0, y0 = x, y
    x1, y1 = x + dx, y + dy
    x2, y2 = x1 - dy, y1 + dx
    x3, y3 = x0 - dy, y0 + dx

    # Малюємо квадрат контурами (лініями)
    ax.plot([x0, x1, x2, x3, x0],
            [y0, y1, y2, y3, y0],
            color="brown", linewidth=1)

    # Масштаб для наступного рівня
    new_size = size * np.sqrt(2) / 2

    # Рекурсивно малюємо ліву і праву гілку
    draw_pythagoras_tree(ax, x3, y3, new_size, angle + np.pi / 4, level - 1)
    draw_pythagoras_tree(ax, x2, y2, new_size, angle - np.pi / 4, level - 1)


if __name__ == "__main__":
    try:
        max_level = int(input("Введіть рівень рекурсії (наприклад, 8–12): "))
    except ValueError:
        print("Некоректне значення, використано рівень 10.")
        max_level = 10

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect("equal")
    ax.axis("off")

    # Малюємо дерево
    draw_pythagoras_tree(ax, x=0, y=0, size=1, angle=0, level=max_level)

    plt.show()