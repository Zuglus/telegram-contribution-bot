FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем переменную окружения PYTHONPATH
ENV PYTHONPATH=/app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libyaml-dev \
    && rm -rf /var/lib/apt/lists/*

# Обновляем pip и setuptools
RUN pip install --upgrade pip setuptools

# Копируем файлы проекта
COPY bot/ ./bot
COPY config.yaml .
COPY requirements.txt .

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска приложения
CMD ["python", "bot/main.py"]
