from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_filter_keyboard():
    """
    Создает клавиатуру для фильтрации взносов по различным параметрам.
    :return: InlineKeyboardMarkup
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="Фильтр по пользователю", callback_data="filter_user"),
        InlineKeyboardButton(text="Фильтр по статусу", callback_data="filter_status"),
        InlineKeyboardButton(text="Фильтр по месяцу", callback_data="filter_month"),
        InlineKeyboardButton(text="Фильтр по году", callback_data="filter_year")
    )
    return keyboard
