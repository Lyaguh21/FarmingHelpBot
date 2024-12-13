from aiogram import Router, F
from aiogram.types import Message, InputMediaPhoto, FSInputFile, CallbackQuery

from FHB_TEST.button import select_theme, all_button_plant, select_berries_plants, select_vegetables_plants, select_fruit_plants

# Инициализируем роутер уровня модуля
router = Router()


@router.callback_query(F.data == "select_fruits_button_pressed")
async def process_fruits_press(callback: CallbackQuery):
    await callback.message.edit_media(
        InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/plant.png")),
        reply_markup=select_fruit_plants
    )

#выбор овоща
@router.callback_query(F.data == "select_vegetables_button_pressed")
async def process_fruits_press(callback: CallbackQuery):
    await callback.message.edit_media(
        InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/plant.png")),
        reply_markup=select_vegetables_plants
    )


#выбор ягоды
@router.callback_query(F.data == "select_berries_button_pressed")
async def process_berries_press(callback: CallbackQuery):
    await callback.message.edit_media(
        InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/plant.png")),
        reply_markup=select_berries_plants
    )

#------------------------------------------------------------------------------------------------

