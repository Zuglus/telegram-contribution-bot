from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Создать взнос", callback_data="create_payment"),
        InlineKeyboardButton(text="История взносов", callback_data="view_history")
    )
    return keyboard
