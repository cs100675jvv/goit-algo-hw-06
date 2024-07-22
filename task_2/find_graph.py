from collections import deque

def bfs_iterative(edges, start):
    # Створюємо словник для представлення графа у вигляді списків суміжності
    graph = {}
    for edge in edges:
        u, v, _ = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited


def dfs_iterative(edges, start_vertex):
    # Створюємо словник для представлення графа у вигляді списків суміжності
    graph = {}
    for edge in edges:
        u, v, _ = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    stack = [start_vertex]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку у зворотному порядку, щоб дотримуватись порядку обходу
            stack.extend(reversed(graph[vertex]))
    
    return visited

# Граф у вигляді списку ребер з вагами
graph = [
    ("Вінниця", "Бар", 60), ("Вінниця", "Бершадь", 120), ("Вінниця", "Гайсин", 90), 
    ("Вінниця", "Іллінці", 50), ("Вінниця", "Калинівка", 25), ("Вінниця", "Козятин", 70),
    ("Вінниця", "Ладижин", 100), ("Вінниця", "Липовець", 40), ("Вінниця", "Могилів-Подільський", 120),
    ("Вінниця", "Немирів", 50), ("Вінниця", "Оратів", 65), ("Вінниця", "Піщанка", 110),
    ("Вінниця", "Погребище", 70), ("Вінниця", "Теплик", 100), ("Вінниця", "Тиврів", 30),
    ("Вінниця", "Томашпіль", 105), ("Вінниця", "Тростянець", 90), ("Вінниця", "Тульчин", 80),
    ("Вінниця", "Хмільник", 60), ("Вінниця", "Чечельник", 120), ("Вінниця", "Шаргород", 90),
    ("Вінниця", "Ямпіль", 130),

    ("Бар", "Бершадь", 120), ("Бар", "Гайсин", 90), ("Бар", "Іллінці", 70),
    ("Бар", "Калинівка", 60), ("Бар", "Козятин", 80), ("Бар", "Ладижин", 130),
    ("Бар", "Липовець", 100), ("Бар", "Могилів-Подільський", 110), ("Бар", "Немирів", 90),
    ("Бар", "Оратів", 110), ("Бар", "Піщанка", 150), ("Бар", "Погребище", 120),
    ("Бар", "Теплик", 140), ("Бар", "Тиврів", 80), ("Бар", "Томашпіль", 160),
    ("Бар", "Тростянець", 110), ("Бар", "Тульчин", 120), ("Бар", "Хмільник", 70),
    ("Бар", "Чечельник", 150), ("Бар", "Шаргород", 70), ("Бар", "Ямпіль", 170),

    ("Бершадь", "Гайсин", 50), ("Бершадь", "Іллінці", 90), ("Бершадь", "Калинівка", 130),
    ("Бершадь", "Козятин", 150), ("Бершадь", "Ладижин", 40), ("Бершадь", "Липовець", 110),
    ("Бершадь", "Могилів-Подільський", 180), ("Бершадь", "Немирів", 70), ("Бершадь", "Оратів", 160),
    ("Бершадь", "Піщанка", 70), ("Бершадь", "Погребище", 140), ("Бершадь", "Теплик", 50),
    ("Бершадь", "Тиврів", 140), ("Бершадь", "Томашпіль", 100), ("Бершадь", "Тростянець", 80),
    ("Бершадь", "Тульчин", 90), ("Бершадь", "Хмільник", 160), ("Бершадь", "Чечельник", 90),
    ("Бершадь", "Шаргород", 140), ("Бершадь", "Ямпіль", 120),

    ("Гайсин", "Іллінці", 40), ("Гайсин", "Калинівка", 80), ("Гайсин", "Козятин", 110),
    ("Гайсин", "Ладижин", 60), ("Гайсин", "Липовець", 70), ("Гайсин", "Могилів-Подільський", 160),
    ("Гайсин", "Немирів", 50), ("Гайсин", "Оратів", 120), ("Гайсин", "Піщанка", 100),
    ("Гайсин", "Погребище", 100), ("Гайсин", "Теплик", 40), ("Гайсин", "Тиврів", 90),
    ("Гайсин", "Томашпіль", 120), ("Гайсин", "Тростянець", 60), ("Гайсин", "Тульчин", 70),
    ("Гайсин", "Хмільник", 130), ("Гайсин", "Чечельник", 110), ("Гайсин", "Шаргород", 120),
    ("Гайсин", "Ямпіль", 150),

    ("Іллінці", "Калинівка", 50), ("Іллінці", "Козятин", 70), ("Іллінці", "Ладижин", 90),
    ("Іллінці", "Липовець", 40), ("Іллінці", "Могилів-Подільський", 150), ("Іллінці", "Немирів", 30),
    ("Іллінці", "Оратів", 60), ("Іллінці", "Піщанка", 130), ("Іллінці", "Погребище", 60),
    ("Іллінці", "Теплик", 80), ("Іллінці", "Тиврів", 70), ("Іллінці", "Томашпіль", 140),
    ("Іллінці", "Тростянець", 100), ("Іллінці", "Тульчин", 90), ("Іллінці", "Хмільник", 50),
    ("Іллінці", "Чечельник", 140), ("Іллінці", "Шаргород", 90), ("Іллінці", "Ямпіль", 160),

    ("Калинівка", "Козятин", 30), ("Калинівка", "Ладижин", 100), ("Калинівка", "Липовець", 20),
    ("Калинівка", "Могилів-Подільський", 140), ("Калинівка", "Немирів", 60), ("Калинівка", "Оратів", 50),
    ("Калинівка", "Піщанка", 140), ("Калинівка", "Погребище", 60), ("Калинівка", "Теплик", 100),
    ("Калинівка", "Тиврів", 50), ("Калинівка", "Томашпіль", 150), ("Калинівка", "Тростянець", 90),
    ("Калинівка", "Тульчин", 80), ("Калинівка", "Хмільник", 50), ("Калинівка", "Чечельник", 140),
    ("Калинівка", "Шаргород", 70), ("Калинівка", "Ямпіль", 160)
]

print ('Виконання BFS з початкової вершини "Вінниця"')
bfs_iterative(graph, "Вінниця")
print ('\nВиконання DFS з початкової вершини "Вінниця"')
dfs_iterative(graph, "Вінниця")