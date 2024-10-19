import heapq

def heap_sort(iterable, descending=False):
    # Визначаємо, який знак використовувати залежно від порядку сортування
    sign = -1 if descending else 1

	# Створюємо купу, використовуючи заданий порядок сортування
    h = [sign * el for el in iterable]
    heapq.heapify(h)
    # Витягуємо елементи, відновлюємо їхні оригінальні значення (якщо потрібно) і формуємо відсортований масив
    return [sign * heapq.heappop(h) for _ in range(len(h))]

def calc_min_cost(cables):
    cables = heap_sort(cables)
    total_cost = 0
    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі і видаляємо його з списку
        first = cables.pop(0)
        second = cables.pop(0)
        # Обраховуємо вартість з'єднання
        cost = first + second
        total_cost += cost
        # Додаємо новий кабель у відсортоване місце
        cables.append(cost)
        # Повторно сортуємо список після додавання з'єднаного кабелю
        cables = heap_sort(cables) 

    return total_cost

cables_list = [5, 2, 6, 1, 3]
result = calc_min_cost(cables_list)
print("Мінімальні загальні витрати на з'єднання:", result)
