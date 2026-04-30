# Переменные
VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

# Создание окружения
$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	touch $(VENV)/bin/activate

# Установка (просто вызываем создание venv)
install: $(VENV)/bin/activate

# Проверка типов
typecheck: $(VENV)/bin/activate
	$(PYTHON) -m mypy src/calc.py

# Проверка стилей (линтер)
lint: $(VENV)/bin/activate
	$(PYTHON) -m flake8 src/

# Форматирование (исправление кода)
format: $(VENV)/bin/activate
	$(PYTHON) -m black src/

# ПРОВЕРКА ЗАВИСИМОСТЕЙ (добавлено по заданию)
# Используем инструмент pip-check-reqs (нужно добавить в requirements.txt)
check-requirements: $(VENV)/bin/activate
	$(PYTHON) -m pip_check_reqs.find_missing_reqs src/

# Составной таргет (исправлено имя check-deps -> check-requirements)
check: lint typecheck check-requirements
	@echo "All checks passed!"

# Запуск приложения
run: $(VENV)/bin/activate
	$(PYTHON) src/app.py

# Очистка
clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +

BUILD_DIR = dist
TWINE = $(VENV)/bin/twine
BUILD = $(VENV)/bin/python3 -m build

# 1. Сборка проекта
build: $(VENV)/bin/activate
	rm -rf $(BUILD_DIR)
	$(PIP) install build twine  # Доставляем инструменты сборки
	$(BUILD)

# 2. Публикация на TestPyPI
publish: build
	$(TWINE) upload --repository testpypi $(BUILD_DIR)/*
