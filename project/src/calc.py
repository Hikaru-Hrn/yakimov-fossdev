def add(a: int, b: int) -> int:
    return a + b


# Ошибка: передаем строку "3" вместо числа
result: int = add(2, "3")
