
# Telegram Contribution Bot

Telegram-бот для учета пользовательских взносов и отслеживания их истории. Бот позволяет пользователям создавать и просматривать свои взносы, а администраторам управлять ими и подтверждать.

## Возможности

- Создание и просмотр взносов.
- Подтверждение или отклонение взносов администраторами.
- Уведомления о статусе взносов.
- Просмотр истории всех изменений взносов.
- Инлайн-клавиатура для удобного взаимодействия.
- Реактивная архитектура на основе событий.

## Установка

1. **Клонировать репозиторий**:
    ```bash
    git clone https://github.com/Zuglus/telegram-contribution-bot.git
    cd telegram-contribution-bot
    ```
2. **Настроить переменные окружения**:

    В файле config.yaml или docker-compose.yml установите значения для переменных:
    - BOT_TOKEN: Токен вашего Telegram-бота.
    - DATABASE_URL: URL для подключения к PostgreSQL.

Пример **config.yaml**:

    ```yaml
    BOT_TOKEN=ваш_токен
    DATABASE_URL=postgresql://user:password@db:5432/telegram_bot_db
    ```

## Запуск
### Через Docker:
    ```bash
    docker-compose up --build
    ```

### Без Docker:
Установите зависимости и запустите бот вручную:
    ```bash
    pip install -r requirements.txt
    python bot/main.py
    ```

### Тестирование
Запуск тестов:
    ```bash
    pytest tests/
    ```

## Лицензия
Проект распространяется под лицензией MIT.
