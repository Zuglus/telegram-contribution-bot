from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_common_buttons(action_confirm, action_reject, entity_id):
    """
    Создает клавиатуру с кнопками подтверждения и отмены.
    :param action_confirm: действие для подтверждения (например, 'confirm')
    :param action_reject: действие для отмены (например, 'reject')
    :param entity_id: ID сущности, к которой привязаны действия
    :return: InlineKeyboardMarkup
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="Подтвердить", callback_data=f"{action_confirm}_{entity_id}"),
        InlineKeyboardButton(text="Отклонить", callback_data=f"{action_reject}_{entity_id}")
    )
    return keyboard
