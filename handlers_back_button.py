from aiogram import Router,F
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto

from FHB_TEST.button import menu_keyboard, select_species_plant, select_theme

router = Router()

#нажатии кнопки назад и перемещение к выбору вида растений
@router.callback_query(F.data == "back_to_select_species_button_pressed")
async def process_back1_press(callback: CallbackQuery):
    await callback.message.edit_media(
        InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/theme.png")),
        reply_markup=select_species_plant
    )

#нажатии кнопки назад и перемещение к выбору темы
@router.callback_query(F.data == "back_to_select_theme_button_pressed")
async def process_back2_press(callback: CallbackQuery):
    await callback.message.edit_media(
        InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/theme.png")),
        reply_markup=select_theme
    )

#нажатии кнопки в начало и переход к выбору типа растения
@router.callback_query(F.data == "back_to_beginning_button_pressed")
async def process_back3_press(callback: CallbackQuery):
    await callback.message.edit_media(
        InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/theme.png")),
        reply_markup=select_species_plant
    )

#нажатии кнопки назад и перемещение к главному меню
@router.callback_query(F.data == "back_to_menu_button_pressed")
async def process_menu_back_press(callback: CallbackQuery):
    await callback.message.edit_media(
        InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/menu.png")),
        reply_markup=menu_keyboard
    )