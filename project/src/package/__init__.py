# Импортируем функцию из файла main.py в пространство имен пакета
from .main import greet, is_cyrillic

# Указываем, какие функции будут доступны при импорте через asterisk (from package import *)
__all__ = ["greet", "is_cyrillic"]
