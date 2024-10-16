from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_payment_keyboard(payment_id):
    """
    Создает клавиатуру для подтверждения или отклонения взноса.
    :param payment_id: ID взноса
    :return: InlineKeyboardMarkup
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="Подтвердить", callback_data=f"confirm_{payment_id}"),
        InlineKeyboardButton(text="Отклонить", callback_data=f"reject_{payment_id}")
    )
    return keyboard
