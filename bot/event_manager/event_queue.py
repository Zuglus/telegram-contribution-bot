from queue import Queue
from threading import Thread
from event_manager.event_publisher import publish_event

event_queue = Queue()

def add_event_to_queue(event_name, data):
    """
    Добавляет событие в очередь для обработки.
    :param event_name: Название события
    :param data: Данные события
    """
    event_queue.put((event_name, data))

def process_event():
    """
    Обрабатывает события из очереди по мере их поступления.
    """
    while True:
        event_name, data = event_queue.get()
        publish_event(event_name, data)  # Публикуем событие для всех подписчиков
        event_queue.task_done()

# Запускаем обработку событий в отдельном потоке
Thread(target=process_event, daemon=True).start()
