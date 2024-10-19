# Dockerfile

# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем зависимости для Python и необходимые пакеты
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libffi-dev libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска бота
CMD ["python", "src/bot.py"]
