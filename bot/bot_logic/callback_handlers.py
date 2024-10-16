from aiogram import types
from aiogram.dispatcher import Dispatcher
from event_manager.event_publisher import publish_event


def register_callback_handlers(dp: Dispatcher):
    @dp.callback_query_handler(lambda c: c.data == 'create_payment')
    async def process_create_payment(callback_query: types.CallbackQuery):
        user_id = callback_query.from_user.id
        # Публикуем событие для создания взноса
        publish_event("create_payment_clicked", {"user_id": user_id})

    @dp.callback_query_handler(lambda c: c.data == 'view_history')
    async def process_view_history(callback_query: types.CallbackQuery):
        user_id = callback_query.from_user.id
        # Публикуем событие для просмотра истории
        publish_event("view_history_clicked", {"user_id": user_id})
        