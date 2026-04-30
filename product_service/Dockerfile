FROM python:3.14-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Отключаем создание виртуальных окружений внутри контейнера
RUN poetry config virtualenvs.create false

# Копируем только файлы зависимостей для кэширования слоев
COPY pyproject.toml poetry.lock* ./

# Устанавливаем зависимости
RUN poetry install --only main --no-root

# Копируем весь исходный код (папку src)
COPY src/ ./src/

# Запускаем сервис
# Используем 0.0.0.0 и порт 8002
CMD ["poetry", "run", "uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8002"]
