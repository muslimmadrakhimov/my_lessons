
# Создаем пользовательский класс исключения StepValueError
# Он нужен для того, чтобы выбрасывать ошибку, если шаг (step) итерации равен 0.
# Этот класс наследуется от стандартного класса исключений ValueError
class StepValueError(ValueError):
    pass  # Этот класс пустой, но наследует поведение ValueError. Мы будем использовать его для обработки ошибок.

# Создаем основной класс Iterator
class Iterator:
    # Конструктор __init__ вызывается при создании объекта класса.
    # Он принимает параметры start, stop и step, инициализируя их как атрибуты объекта.
    def __init__(self, start, stop, step=1):
        """
        Конструктор принимает три параметра:
        - start: начальное значение для итерации.
        - stop: конечное значение, на котором итерация завершится.
        - step: шаг итерации, по умолчанию равен 1 (если его не указали).

        Важное условие: если step равен 0, выбрасывается исключение StepValueError.
        """
        if step == 0:  # Проверяем, чтобы шаг не был равен 0
            # Если шаг 0, вызываем наше пользовательское исключение StepValueError с сообщением.
            raise StepValueError('Шаг не может быть равен 0')

        # Сохраняем параметры как атрибуты объекта
        self.start = start  # Это начальное значение, с которого начинается итерация
        self.stop = stop    # Это конечное значение, на котором итерация завершится
        self.step = step    # Шаг, с которым мы будем двигаться по значениям
        self.pointer = start  # Указатель на текущее значение итерации, изначально равное start

    # Метод __iter__ делает объект итерируемым, т.е. позволяет его использовать в циклах for.
    def __iter__(self):
        """
        Метод __iter__ сбрасывает указатель (pointer) на начальное значение (start)
        и возвращает сам объект. Это позволяет использовать его в цикле for.
        """
        self.pointer = self.start  # Возвращаем указатель на начальное значение
        return self  # Возвращаем сам объект. Это позволяет использовать объект в итерациях.

    # Метод __next__ описывает поведение при каждом шаге итерации.
    def __next__(self):
        """
        Метод __next__ отвечает за выполнение каждого шага итерации.
        Он увеличивает текущее значение на step, а если текущее значение выходит за пределы stop,
        он выбрасывает исключение StopIteration, чтобы завершить итерацию.
        """
        # Проверяем, не закончил ли итератор свою работу
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            # Если шаг положительный и текущее значение больше конечного,
            # или если шаг отрицательный и текущее значение меньше конечного,
            # итерация завершена, выбрасываем StopIteration
            raise StopIteration

        # Сохраняем текущее значение указателя, чтобы вернуть его перед увеличением
        current_value = self.pointer

        # Увеличиваем (или уменьшаем) текущее значение указателя на шаг (step)
        self.pointer += self.step

        # Возвращаем текущее значение до его изменения
        return current_value


# Пример использования нашего итератора с разными параметрами

# Используем блок try-except для обработки исключения StepValueError
try:
    # Создаем объект итератора с шагом 0. Это вызовет исключение StepValueError.
    iter1 = Iterator(100, 200, 0)  # Шаг равен 0, что запрещено
    for i in iter1:
        print(i, end=' ')  # Этот код не выполнится, потому что шаг 0 вызовет ошибку
except StepValueError:
    # Если поймали исключение, выводим сообщение "Шаг указан неверно"
    print('Шаг указан неверно')

# Создаем несколько итераторов с корректными параметрами
# Эти итераторы будут использоваться в циклах for

# Итератор с шагом по умолчанию (1), двигаемся от -5 до 1
iter2 = Iterator(-5, 1)

# Итератор с шагом 2, двигаемся от 6 до 15 (только четные числа будут выведены)
iter3 = Iterator(6, 15, 2)

# Итератор с отрицательным шагом -1, двигаемся от 5 до 1
iter4 = Iterator(5, 1, -1)

# Итератор с шагом по умолчанию (1), двигаемся от 10 до 1, но не включаем 1
iter5 = Iterator(10, 1)

# Для каждого итератора запускаем цикл for, который будет использовать методы __iter__ и __next__

print("Итерация iter2 (от -5 до 1):")
for i in iter2:
    print(i, end=' ')  # Выведет значения от -5 до 1 с шагом 1
print()  # Печатаем пустую строку для новой линии

print("Итерация iter3 (от 6 до 15 с шагом 2):")
for i in iter3:
    print(i, end=' ')  # Выведет значения: 6 8 10 12 14 (с шагом 2)
print()

print("Итерация iter4 (от 5 до 1 с шагом -1):")
for i in iter4:
    print(i, end=' ')  # Выведет значения: 5 4 3 2 1 (с шагом -1)
print()

print("Итерация iter5 (от 10 до 1 с шагом по умолчанию 1):")
for i in iter5:
    print(i, end=' ')  # Выведет значения: 10 9 8 7 6 5 4 3 2 (не включаем 1)
print()
