def get_matrix(n, m, value):
    matrix = []  # создаем пустой список для матрицы
    for i in range(n):  # внешний цикл для строк
        row = []  # создаем пустую строку
        for j in range(m):  # внутренний цикл для столбцов
            row.append(value)  # добавляем значение в строку
        matrix.append(row)  # добавляем строку в матрицу
    return matrix  # возвращаем полученную матрицу

# Пример использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результатов
print(result1)
print(result2)
print(result3)