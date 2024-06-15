from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_menu_keyboard():
    registration_button = InlineKeyboardButton(
        text="Registration🔥",
        callback_data="registration"
    )
    profile_button = InlineKeyboardButton(
        text="My Profile🧑🏻‍💻",
        callback_data="my_profile"
    )
    profiles_button = InlineKeyboardButton(
        text="View Profiles🤑",
        callback_data="all_profiles"
    )
    reference_menu_button = InlineKeyboardButton(
        text="Reference Menu💵",
        callback_data="reference_menu"
    )
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [registration_button],
        [profile_button],
        [profiles_button],
        [reference_menu_button],
    ])
    return markup