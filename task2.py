import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

def draw_square(x, y, size, angle, color="brown", fill=False):
    """Малюємо квадрат, повертаємо координати верхньої сторони"""
    coords = []
    points = []
    for i in range(4):
        x_new = x + size * np.cos(angle + i * np.pi / 2)
        y_new = y + size * np.sin(angle + i * np.pi / 2)
        coords.append((x, y))
        points.append((x, y))
        x, y = x_new, y_new
    points.append(points[0])  # замаємо квадрат

    xs, ys = zip(*points)
    if fill:
        plt.fill(xs, ys, color=color)
    else:
        plt.plot(xs, ys, color=color, linewidth=1)

    return coords[-2], coords[-1]  # верхня сторона

def draw_tree(x, y, size, angle, depth, max_depth):
    """Рекурсивно малюємо дерево Піфагора"""
    if depth == 0:
        return
    
    # Відтінок зеленого для листків
    if depth == 1:
        norm = (max_depth - depth) / max_depth
        green_shade = cm.Greens(0.4 + 0.6 * norm)  # від темно-зеленого до світло-зеленого
        color = green_shade
        is_leaf = True
    else:
        color = "brown"
        is_leaf = False
    
    # Малюємо квадрат
    (x1, y1), (x2, y2) = draw_square(x, y, size, angle, color=color, fill=is_leaf)
    
    if is_leaf:
        return  # далі не йдемо (листок)
    
    # Середина верхньої сторони
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    
    # Вершина трикутника
    dx, dy = x2 - x1, y2 - y1
    hx, hy = mx - dy / 2, my + dx / 2
    
    # Малюємо трикутник (коричневий, як гілки)
    plt.plot([x1, x2], [y1, y2], color="brown", linewidth=1)
    plt.plot([x1, hx], [y1, hy], color="brown", linewidth=1)
    plt.plot([x2, hx], [y2, hy], color="brown", linewidth=1)
    
    # Новий розмір квадрата
    new_size = size / np.sqrt(2)
    
    # Рекурсія: ліва і права гілка
    draw_tree(x1, y1, new_size, angle - np.pi/4, depth - 1, max_depth)
    draw_tree(hx, hy, new_size, angle + np.pi/4, depth - 1, max_depth)

def main():
    depth = int(input("Введіть рівень рекурсії (наприклад, 8–12): "))

    plt.figure(figsize=(10, 10))
    plt.axis("equal")
    plt.axis("off")

    # Початковий квадрат (стовбур)
    start_x, start_y = -50, 0
    initial_size = 100

    draw_tree(start_x, start_y, initial_size, 0, depth, depth)

    plt.show()

if __name__ == "__main__":
    main()