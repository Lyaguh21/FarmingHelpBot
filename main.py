import asyncio

from aiogram import Bot, Dispatcher
from cfg import TOKEN
import handlers_menu,handlers_plant,handlers_desiese_bugs_fertillizer,handlers_back_button,handlers_bugs



# Функция конфигурирования и запуска бота
async def main():

    # Инициализируем бот и диспетчер
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    #регистрация меню
    dp.startup.register(handlers_menu.set_main_menu)
    # Регистриуем роутеры в диспетчере
    dp.include_router(handlers_menu.router)
    dp.include_router(handlers_plant.router)
    dp.include_router(handlers_desiese_bugs_fertillizer.router)
    dp.include_router(handlers_back_button.router)


    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())