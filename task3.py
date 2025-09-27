import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight, directed = False):
        #додаємо ребро u -> v
        if u not in self.adj_list:
            self. adj_list[u] = []
        self.adj_list[u].append((v, weight))

        #якщо граф неорієнтований
        if not directed:
            if v not in self.adj_list:
                self.adj_list[v] = []
            self.adj_list[v].append((u, weight))

    def dijkstra(self, start):
        #ініціалізація відстаней
        distances = {vertex: float("inf") for vertex in self.adj_list}
        distances[start] = 0

        #мін-купа(вага, вершина)
        heap = [(0, start)]

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            #якщо вже знайшли кращий шлях, пропускаємо
            if current_distance > distances[current_vertex]:
                continue

            #перевіряємо сусідів
            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
        return distances
    

# ==== Приклад використання ====
if __name__ == "__main__":
    g = Graph()

    # створюємо граф
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)
    g.add_edge("C", "E", 10)
    g.add_edge("D", "E", 2)
    g.add_edge("D", "Z", 6)
    g.add_edge("E", "Z", 3)

    # запускаємо Дейкстру з вершини A
    start_vertex = "A"
    distances = g.dijkstra(start_vertex)

    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex, dist in distances.items():
        print(f"{start_vertex} -> {vertex}: {dist}")    