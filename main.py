"""
Создание директории src
"""
from pathlib import Path

src_path = Path(__file__).parent / "src"

src_path.mkdir(exist_ok=True)
print(src_path)

"""
Сумма двух чисел
"""
def sum_a(a: int, b: int) -> int:
    if isinstance(a, str) or isinstance(b, str): raise ValueError("wrong type")
    return a + b

"""
Деление двух чисел
"""
def div(a: int, b: int) -> int:
    if b == 0: raise ValueError("b == 0!")
    if isinstance(a, str) or isinstance(b, str): raise ValueError("wrong type")
    return a / b


"""
Вычитание (лучший вариант)
"""
def sub(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return a.replace(b, '')
    return a - b
