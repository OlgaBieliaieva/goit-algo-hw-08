import heapq

def min_connection_cost(cables):
    # Створюємо мін-купу з початкового списку кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднуємо їх та додаємо витрати
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад
cables = [4, 3, 2, 6, 1, 12]
print("Мінімальні витрати на з'єднання:", min_connection_cost(cables))