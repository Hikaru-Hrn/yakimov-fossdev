FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install uvicorn && poetry install --only main --no-root

COPY src/app ./app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]

