def generate_password(n):
    result = []
    used = set()  # Множество для отслеживания использованных чисел

    for i in range(1, n):
        for j in range(i + 1, n):
            if (i not in used) and (j not in used):  # Проверяем, что числа ещё не использованы
                if n % (i + j) == 0:  # Проверяем кратность
                    result.append(str(i) + str(j))
                    used.add(i)
                    used.add(j)

    return ''.join(result)

# Пример использования
n = int(input("Введите число n: "))  # Ввод числа от 3 до 20
print("Результат:", generate_password(n))

