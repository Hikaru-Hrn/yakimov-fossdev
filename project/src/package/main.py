# src/package/main.py


def is_cyrillic(text: str) -> bool:
    """Проверяет, содержит ли строка только кириллицу."""
    return all("\u0400" <= char <= "\u04ff" or char.isspace() for char in text)


def greet(name: str) -> str:
    """Простая приветственная функция."""
    if is_cyrillic(name):
        return f"Привет, {name}!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("perforator"))
    print(greet("разработчик"))
