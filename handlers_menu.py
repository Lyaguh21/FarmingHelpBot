from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, BotCommand, FSInputFile, InputMediaPhoto, CallbackQuery

from FHB_TEST.button import menu_keyboard, back_to_menu_keyboard, select_species_plant,in_menu_keyboard
    
# Инициализируем роутер уровня модуля
router = Router()

#меню команд
async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command="/start", description="Начало общения"),
        BotCommand(command="/menu", description="Открыть главное меню"),

    ]
    await bot.set_my_commands(main_menu_commands)


# Этот хэндлер срабатывает на команду /start
@router.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer_photo(photo= FSInputFile("../FHB_TEST/photo_menu/welcome.jpg"), caption="Добро пожаловать в бота, помощника по ферме! Я могу помочь определиться с выбором удобрений и химикатов 📦. Так же вы можете воспользоваться функцией распознавания болезни по фото ✨.\nЧто бы воспользоваться функционалом перейдите в меню.",reply_markup=in_menu_keyboard)

# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=["menu"]))
async def process_menu_command(message: Message):
    await message.answer_photo(photo = FSInputFile("../FHB_TEST/photo_menu/menu.png"),reply_markup=menu_keyboard,)



#Кнопка в меню
@router.callback_query(F.data == "in_menu_pressed")
async def process_in_menu_press(callback: CallbackQuery):
    await callback.message.edit_media(
        InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/menu.png")),
        reply_markup=menu_keyboard
    )

# хендлеры на меню
@router.callback_query(F.data == "start_button_pressed")
async def process_start_press(callback: CallbackQuery):
    await callback.message.edit_media(
        InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/type.png")),
        reply_markup=select_species_plant
    )
#Привет ВИ13
@router.callback_query(F.data == "message_support_button_pressed")
async def process_message_support_press(callback: CallbackQuery):
    await callback.message.edit_media(
        InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/support.png"),caption="Напишите нам если у вас возникли проблемы, и мы ответим вам в ближайшее время"),
        reply_markup=back_to_menu_keyboard
    )

@router.callback_query(F.data == "info_button_pressed")
async def process_info_press(callback: CallbackQuery):
    await callback.message.edit_media(
        InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/info.png"),caption="Наш бот предоставляет источник информации, в котором вы можете:\n- Узнать как выращивать ту или иную Культуру.\n- Узнать как бороться с вредителями и болезнями.\n- Узнать какие удобрения использовать.\n- Определить болезнь растения по фото.\n- Получить рекомендации по вопросам.\nИ многое другое...  "),
        reply_markup=back_to_menu_keyboard
    )

@router.callback_query(F.data == "desiese_photo_pressed")
async def process_desiese_photo_press(callback: CallbackQuery):
    await callback.answer(
        text="✨ Что бы воспользоваться распознованием по фото приобретите FHB+ ✨",
        show_alert=True
    )

@router.callback_query(F.data == "buy_pass_pressed")
async def process_buy_pass_press(callback: CallbackQuery):
    await callback.answer(
        text="На Данный момент эта функция в разработке ⚙️",
        show_alert=True

    )
@router.callback_query(F.data == "messanger_pressed")
async def process_buy_pass_press(callback: CallbackQuery):
    await callback.answer(
        text="В будущем тут обязательно что-то будет⚙️",
        show_alert=True

    )
