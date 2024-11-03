from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from LEXICON import *


#назад к выбору вида
back_to_select_species_button = InlineKeyboardButton(
    text ="Назад ◀️",
    callback_data = "back_to_select_species_button_pressed",
)

#в самое начало помощи
back_to_beginning_button = InlineKeyboardButton(
    text ="В начало ⏪",
    callback_data = "back_to_beginning_button_pressed",
)

back_to_beginning_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[back_to_beginning_button]]
)

#к главному меню
back_to_menu_button = InlineKeyboardButton(
    text ="В главное меню ⏪",
    callback_data = "back_to_menu_button_pressed",
)
back_to_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[back_to_menu_button]]
)

#назад к выбору темы
back_to_select_theme_button = InlineKeyboardButton(
    text = "Назад ◀️",
    callback_data = "back_to_select_theme_button_pressed",

)
in_menu = InlineKeyboardButton(
    text="В меню 📖",
    callback_data="in_menu_pressed"
)
in_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[in_menu]]
)
#menu
start_button = InlineKeyboardButton(
    text="Начать ▶️",
    callback_data = "start_button_pressed",
)
message_support = InlineKeyboardButton(
    text="Поддержка ✉️",
    callback_data = "message_support_button_pressed",
)
info_button = InlineKeyboardButton(
    text="Инфо ℹ️",
    callback_data = "info_button_pressed",
)
desiese_photo_button = InlineKeyboardButton(
    text="Определить болезнь по фото ✨",
    callback_data = "desiese_photo_pressed",
)
buy_pass_button = InlineKeyboardButton(
    text="Подписка ✨",
    callback_data = "buy_pass_pressed",
)
social_networks_button = InlineKeyboardButton(
    text="Соц Сети 📱",
    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
)

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[start_button],[message_support,info_button],[buy_pass_button,social_networks_button],[desiese_photo_button]]
)



#Кнопки выбора вида растения

select_fruits_button = InlineKeyboardButton(
    text="🔒 Фрукты 🍐",
    # callback_data = "select_fruits_button_pressed",
    callback_data="inactive1"
)
select_berries_button = InlineKeyboardButton(
    text="Ягоды 🍇",
    callback_data = "select_berries_button_pressed",

)
select_vegetables_button = InlineKeyboardButton(
    text="🔒 Овощи 🥒",
    # callback_data = "select_vegetables_button_pressed",
    callback_data="inactive2"

)

select_species_plant = InlineKeyboardMarkup(
    inline_keyboard=[[select_fruits_button],[select_vegetables_button],[select_berries_button],[back_to_menu_button]]

)



#кнопки выбора фруктов
select_apple_button = InlineKeyboardButton(
    text="Яблоки 🍎",
    callback_data = "apple_button_pressed",
)
select_pear_button = InlineKeyboardButton(
    text="Груши 🍐",
    callback_data = "pear_button_pressed",
)
select_apricots_button = InlineKeyboardButton(
    text="Абрикосы 🟠",
    callback_data = "apricots_button_pressed",
)
select_pomegranate_button = InlineKeyboardButton(
    text="Гранат 🔴",
    callback_data = "pomegranate_button_pressed",
)
select_plums_button = InlineKeyboardButton(
    text="Сливы 🟣",
    callback_data = "plums_button_pressed",
)
select_tangerines_button = InlineKeyboardButton(
    text="Мандарины 🍊",
    callback_data = "tangerines_button_pressed",
)
select_peaches_button = InlineKeyboardButton(
    text="Персики 🍑",
    callback_data = "peaches_button_pressed",
)
select_banana_button = InlineKeyboardButton(
    text="Бананы 🍌",
    callback_data = "banana_button_pressed",
)



select_fruit_plants = InlineKeyboardMarkup(

    inline_keyboard=[[select_apple_button , select_pear_button],[select_apricots_button,select_pomegranate_button],[select_plums_button,select_tangerines_button],[select_peaches_button,select_banana_button],[back_to_select_species_button]]
)


#кнопки выбора овощей
select_cabbage_button = InlineKeyboardButton(
    text="Капуста 🌿",
    callback_data = "cabbage_button_pressed",
)
select_cucumbers_button = InlineKeyboardButton(
    text="Огурцы 🥒",
    callback_data = "cucumbers_button_pressed",
)
select_tomato_button = InlineKeyboardButton(
    text="Помидоры 🔴",
    callback_data = "tomato_button_pressed",
)
select_potato_button = InlineKeyboardButton(
    text="Картофель 🥔",
    callback_data = "potato_button_pressed",
)
select_corn_button = InlineKeyboardButton(
    text="Кукуруза 🌽",
    callback_data = "corn_button_pressed",
)
select_beets_button = InlineKeyboardButton(
    text="Свекла 🌿",
    callback_data = "beets_button_pressed",
)
select_wheat_button = InlineKeyboardButton(
    text="Пшеница 🌾",
    callback_data = "wheat_button_pressed",
)
select_oats_button = InlineKeyboardButton(
    text="Овес 🌱",
    callback_data = "oats_button_pressed",
)

select_vegetables_plants = InlineKeyboardMarkup(

    inline_keyboard=[[select_oats_button,select_corn_button],[select_cabbage_button,select_cucumbers_button],[select_tomato_button,select_potato_button],[select_beets_button,select_wheat_button],[back_to_select_species_button]]
)



#кнопки выбора ягод
select_cherry_button = InlineKeyboardButton(
    text="Вишня 🍒",
    callback_data = "cherry_button_pressed",
)
select_watermelon_button = InlineKeyboardButton(
    text="Арбузы 🍉",
    callback_data = "watermelon_button_pressed",
)
select_strawberry_button = InlineKeyboardButton(
    text="Клубника 🍓",
    callback_data = "strawberry_button_pressed",
)
select_raspberry_button = InlineKeyboardButton(
    text="Малина 🍓",
    callback_data = "raspberry_button_pressed",
)
select_grapes_button = InlineKeyboardButton(
    text="Виноград 🍇",
    callback_data = "grapes_button_pressed",
)
select_gooseberries_button = InlineKeyboardButton(
    text="Крыжовник 🌿",
    callback_data = "gooseberries_button_pressed",
)
select_blueberries_button = InlineKeyboardButton(
    text="Голубика 🫐",
    callback_data = "blueberries_button_pressed",
)
select_melon_button = InlineKeyboardButton(
    text="Дыня 🍈",
    callback_data = "melon_button_pressed",
)


select_berries_plants = InlineKeyboardMarkup(
    inline_keyboard=[[select_cherry_button,select_watermelon_button],[select_strawberry_button,select_raspberry_button],[select_grapes_button,select_gooseberries_button],[select_blueberries_button,select_melon_button],[back_to_select_species_button]]
)
#Выбор темы запроса
select_bugs_button = InlineKeyboardButton(
    text= "Помощь с вредителями 🪲",
    callback_data = "bugs_button_pressed",

)
select_disease_button = InlineKeyboardButton(
    text="Помощь с болезнями 🦠",
    callback_data="disease_button_pressed",

)
select_fertilizer_button = InlineKeyboardButton(
    text="Помощь с удобрениями 📦",
    callback_data="fertilizer_button_pressed",
)
select_theme = InlineKeyboardMarkup(
    inline_keyboard=[[select_disease_button],[select_bugs_button],[select_fertilizer_button]]
)

#--------------------------------------------------- БОЛЕЗНИ--------------------------------------------------------------------------------\\\\\
#------------------ФРУКТЫ--------------------------------------------
#Выбор болезней
diseise_apple_first = InlineKeyboardButton(
    text= "Болезнь яблони №1 🦠",
    callback_data = "diseise_apple_first_pressed",
)
diseise_apple_second = InlineKeyboardButton(
    text= "Болезнь яблони №2 🦠",
    callback_data = "diseise_apple_second_pressed",
)
diseise_apple_third = InlineKeyboardButton(
    text= "Болезнь яблони №3 🦠",
    callback_data = "diseise_apple_third_pressed",
)
desiese_apple = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_apple_first],[diseise_apple_second],[diseise_apple_third]]
)


diseise_pear_first = InlineKeyboardButton(
    text= "Болезнь груши №1 🦠",
    callback_data = "diseise_pear_first_pressed",
)
diseise_pear_second = InlineKeyboardButton(
    text= "Болезнь груши №2 🦠",
    callback_data = "diseise_pear_second_pressed",
)
diseise_pear_third = InlineKeyboardButton(
    text= "Болезнь груши №3 🦠",
    callback_data = "diseise_pear_third_pressed",
)
desiese_pear = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_pear_first],[diseise_pear_second],[diseise_pear_third]]
)


diseise_apricots_first = InlineKeyboardButton(
    text= "Болезнь абрикос №1 🦠",
    callback_data = "diseise_apricots_first_pressed",
)
diseise_apricots_second = InlineKeyboardButton(
    text= "Болезнь абрикос №2 🦠",
    callback_data = "diseise_apricots_second_pressed",
)
diseise_apricots_third = InlineKeyboardButton(
    text= "Болезнь абрикос №3 🦠",
    callback_data = "diseise_apricots_third_pressed",
)
desiese_apricots = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_apricots_first],[diseise_apricots_second],[diseise_apricots_third]]
)


diseise_pomegranate_first = InlineKeyboardButton(
    text= "Болезнь граната №1 🦠",
    callback_data = "diseise_pomegranate_first_pressed",
)
diseise_pomegranate_second = InlineKeyboardButton(
    text= "Болезнь граната №2 🦠",
    callback_data = "diseise_pomegranate_second_pressed",
)
diseise_pomegranate_third = InlineKeyboardButton(
    text= "Болезнь граната №3 🦠",
    callback_data = "diseise_pomegranate_third_pressed",
)
desiese_pomegranate = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_pomegranate_first],[diseise_pomegranate_second],[diseise_pomegranate_third]]
)


diseise_plums_first = InlineKeyboardButton(
    text= "Болезнь слив №1 🦠",
    callback_data = "diseise_plums_first_pressed",
)
diseise_plums_second = InlineKeyboardButton(
    text= "Болезнь слив №2 🦠",
    callback_data = "diseise_plums_second_pressed",
)
diseise_plums_third = InlineKeyboardButton(
    text= "Болезнь слив №3 🦠",
    callback_data = "diseise_plums_third_pressed",
)
desiese_plums = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_plums_first],[diseise_plums_second],[diseise_plums_third]]
)


diseise_tangerines_first = InlineKeyboardButton(
    text= "Болезнь мандаринов №1 🦠",
    callback_data = "diseise_tangerines_first_pressed",
)
diseise_tangerines_second = InlineKeyboardButton(
    text= "Болезнь мандаринов №2 🦠",
    callback_data = "diseise_tangerines_second_pressed",
)
diseise_tangerines_third = InlineKeyboardButton(
    text= "Болезнь мандаринов №3 🦠",
    callback_data = "diseise_tangerines_third_pressed",
)
desiese_tangerines = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_tangerines_first],[diseise_tangerines_second],[diseise_tangerines_third]])


diseise_peach_first = InlineKeyboardButton(
    text= "Болезнь персиков №1 🦠",
    callback_data = "diseise_peach_first_pressed",
)
diseise_peach_second = InlineKeyboardButton(
    text= "Болезнь персиков №2 🦠",
    callback_data = "diseise_peach_second_pressed",
)
diseise_peach_third = InlineKeyboardButton(
    text= "Болезнь персиков №3 🦠",
    callback_data = "diseise_peach_third_pressed",
)
desiese_peach = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_peach_first],[diseise_peach_second],[diseise_peach_third]]
)

diseise_banana_first = InlineKeyboardButton(
    text= "Болезнь бананов №1 🦠",
    callback_data = "diseise_banana_first_pressed",
)
diseise_banana_second = InlineKeyboardButton(
    text= "Болезнь бананов №2 🦠",
    callback_data = "diseise_banana_second_pressed",
)
diseise_banana_third = InlineKeyboardButton(
    text= "Болезнь бананов №3 🦠",
    callback_data = "diseise_banana_third_pressed",
)
desiese_banana = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_banana_first],[diseise_banana_second],[diseise_banana_third]]
)
#------------------БОЛЕЗНИ_ОВОЩЕЙ------------------------

#------------------БОЛЕЗНИ_ЯГОД---------------------------\\\
diseise_cherry_first = InlineKeyboardButton(
    text= "Коккомикоз 🦠",
    callback_data = "diseise_cherry_first_pressed",
)
diseise_cherry_second = InlineKeyboardButton(
    text= "Клястероспрориоз 🦠",
    callback_data = "diseise_cherry_second_pressed",
)
diseise_cherry_third = InlineKeyboardButton(
    text= "Монилиозом 🦠",
    callback_data = "diseise_cherry_third_pressed",
)
desiese_cherry = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_cherry_first],[diseise_cherry_second],[diseise_cherry_third]]
)

diseise_watermelon_first = InlineKeyboardButton(
    text= "Антракноз 🦠",
    callback_data = "diseise_watermelon_first_pressed",
)
diseise_watermelon_second = InlineKeyboardButton(
    text= "Склеротиния 🦠",
    callback_data = "diseise_watermelon_second_pressed",
)
diseise_watermelon_third = InlineKeyboardButton(
    text= "Угловая пятнистость 🦠",
    callback_data = "diseise_watermelon_third_pressed",
)
desiese_watermelon = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_watermelon_first],[diseise_watermelon_second],[diseise_watermelon_third]]
)

diseise_strawberry_first = InlineKeyboardButton(
    text= "Бурая пятнистость 🦠",
    callback_data = "diseise_strawberry_first_pressed",
)
diseise_strawberry_second = InlineKeyboardButton(
    text= "Септориоз 🦠",
    callback_data = "diseise_strawberry_second_pressed",
)
diseise_strawberry_third = InlineKeyboardButton(
    text= "Верциллез 🦠",
    callback_data = "diseise_strawberry_third_pressed",
)
desiese_strawberry = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_strawberry_first],[diseise_strawberry_second],[diseise_strawberry_third]]
)

diseise_raspberry_first = InlineKeyboardButton(
    text= "Антракноз 🦠",
    callback_data = "diseise_raspberry_first_pressed",
)
diseise_raspberry_second = InlineKeyboardButton(
    text= "Серая гниль 🦠",
    callback_data = "diseise_raspberry_second_pressed",
)
diseise_raspberry_third = InlineKeyboardButton(
    text= "Ржавчина 🦠",
    callback_data = "diseise_raspberry_third_pressed",
)
desiese_raspberry = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_raspberry_first],[diseise_raspberry_second],[diseise_raspberry_third]]
)

diseise_grape_first = InlineKeyboardButton(
    text= "Краснуха 🦠",
    callback_data = "diseise_grape_first_pressed",
)
diseise_grape_second = InlineKeyboardButton(
    text= "Оидиум 🦠",
    callback_data = "diseise_grape_second_pressed",
)
diseise_grape_third = InlineKeyboardButton(
    text= "Милдью 🦠",
    callback_data = "diseise_grape_third_pressed",
)
desiese_grape = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_grape_first],[diseise_grape_second],[diseise_grape_third]]
)

diseise_gooseberries_first = InlineKeyboardButton(
    text= "Ржавчина 🦠",
    callback_data = "diseise_gooseberries_first_pressed",
)
diseise_gooseberries_second = InlineKeyboardButton(
    text= "Антракноз 🦠",
    callback_data = "diseise_gooseberries_second_pressed",
)
diseise_gooseberries_third = InlineKeyboardButton(
    text= "Септориоз 🦠",
    callback_data = "diseise_gooseberries_third_pressed",
)
desiese_gooseberries = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_gooseberries_first],[diseise_gooseberries_second],[diseise_gooseberries_third]]
)

diseise_blueberry_first = InlineKeyboardButton(
    text= "Рак стебля 🦠",
    callback_data = "diseise_blueberry_first_pressed",
)
diseise_blueberry_second = InlineKeyboardButton(
    text= "Фомопсис 🦠",
    callback_data = "diseise_blueberry_second_pressed",
)
diseise_blueberry_third = InlineKeyboardButton(
    text= "Ботритис 🦠",
    callback_data = "diseise_blueberry_third_pressed",
)
desiese_blueberry = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_blueberry_first],[diseise_blueberry_second],[diseise_blueberry_third]]
)

diseise_melon_first = InlineKeyboardButton(
    text= "Мучнистая роса 🦠",
    callback_data = "diseise_melon_first_pressed",
)
diseise_melon_second = InlineKeyboardButton(
    text= "Фузариозное увядание 🦠",
    callback_data = "diseise_melon_second_pressed",
)
diseise_melon_third = InlineKeyboardButton(
    text= "Антракноз (Медянка) 🦠",
    callback_data = "diseise_melon_third_pressed",
)
desiese_melon = InlineKeyboardMarkup(
    inline_keyboard=[[diseise_melon_first],[diseise_melon_second],[diseise_melon_third]]
)
#----------------------------------------------------------ВРЕДИТЕЛИ-------------------------------------------------------------------------------------\\\\\
#-------------------------------------------ФРУКТЫ----------------------------------------------

bugs_apple_first = InlineKeyboardButton(
    text= "Вредители яблони №1 🪲",
    callback_data = "bugs_apple_first_pressed",
)
bugs_apple_second = InlineKeyboardButton(
    text= "Вредители яблони №2 🪲",
    callback_data = "bugs_apple_second_pressed",
)
bugs_apple_third = InlineKeyboardButton(
    text= "Вредители яблони №3 🪲",
    callback_data = "bugs_apple_third_pressed",
)
bugs_apple = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_apple_first],[bugs_apple_second],[bugs_apple_third]]
)


bugs_pear_first = InlineKeyboardButton(
    text= "Вредители груши №1 🪲",
    callback_data = "bugs_pear_first_pressed",
)
bugs_pear_second = InlineKeyboardButton(
    text= "Вредители груши №2 🪲",
    callback_data = "bugs_pear_second_pressed",
)
bugs_pear_third = InlineKeyboardButton(
    text= "Вредители груши №3 🪲",
    callback_data = "bugs_pear_third_pressed",
)
bugs_pear = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_pear_first],[bugs_pear_second],[bugs_pear_third]]
)


bugs_apricots_first = InlineKeyboardButton(
    text= "Вредители абрикос №1 🪲",
    callback_data = "bugs_apricots_first_pressed",
)
bugs_apricots_second = InlineKeyboardButton(
    text= "Вредители абрикос №2 🪲",
    callback_data = "bugs_apricots_second_pressed",
)
bugs_apricots_third = InlineKeyboardButton(
    text= "Вредители абрикос №3 🪲",
    callback_data = "bugs_apricots_third_pressed",
)
bugs_apricots = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_apricots_first],[bugs_apricots_second],[bugs_apricots_third]]
)


bugs_pomegranate_first = InlineKeyboardButton(
    text= "Вредители граната №1 🪲",
    callback_data = "bugs_pomegranate_first_pressed",
)
bugs_pomegranate_second = InlineKeyboardButton(
    text= "Вредители граната №2 🪲",
    callback_data = "bugs_pomegranate_second_pressed",
)
bugs_pomegranate_third = InlineKeyboardButton(
    text= "Вредители граната №3 🪲",
    callback_data = "bugs_pomegranate_third_pressed",
)
bugs_pomegranate = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_pomegranate_first],[bugs_pomegranate_second],[bugs_pomegranate_third]]
)


bugs_plums_first = InlineKeyboardButton(
    text= "Вредители слив №1 🪲",
    callback_data = "bugs_plums_first_pressed",
)
bugs_plums_second = InlineKeyboardButton(
    text= "Вредители слив №2 🪲",
    callback_data = "bugs_plums_second_pressed",
)
bugs_plums_third = InlineKeyboardButton(
    text= "Вредители слив №3 🪲",
    callback_data = "bugs_plums_third_pressed",
)
bugs_plums = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_plums_first],[bugs_plums_second],[bugs_plums_third]]
)


bugs_tangerines_first = InlineKeyboardButton(
    text= "Вредители мандаринов №1 🪲",
    callback_data = "bugs_tangerines_first_pressed",
)
bugs_tangerines_second = InlineKeyboardButton(
    text= "Вредители мандаринов №2 🪲",
    callback_data = "bugs_tangerines_second_pressed",
)
bugs_tangerines_third = InlineKeyboardButton(
    text= "Вредители мандаринов №3 🪲",
    callback_data = "bugs_tangerines_third_pressed",
)
bugs_tangerines = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_tangerines_first],[bugs_tangerines_second],[bugs_tangerines_third]])


bugs_peach_first = InlineKeyboardButton(
    text= "Вредители персиков №1 🪲",
    callback_data = "bugs_peach_first_pressed",
)
bugs_peach_second = InlineKeyboardButton(
    text= "Вредители персиков №2 🪲",
    callback_data = "bugs_peach_second_pressed",
)
bugs_peach_third = InlineKeyboardButton(
    text= "Вредители персиков №3 🪲",
    callback_data = "bugs_peach_third_pressed",
)
bugs_peach = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_peach_first],[bugs_peach_second],[bugs_peach_third]]
)

bugs_banana_first = InlineKeyboardButton(
    text= "Вредители бананов №1 🪲",
    callback_data = "bugs_banana_first_pressed",
)
bugs_banana_second = InlineKeyboardButton(
    text= "Вредители бананов №2 🪲",
    callback_data = "bugs_banana_second_pressed",
)
bugs_banana_third = InlineKeyboardButton(
    text= "Вредители бананов №3 🪲",
    callback_data = "bugs_banana_third_pressed",
)
bugs_banana = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_banana_first],[bugs_banana_second],[bugs_banana_third]]
)
#-------------------------------------------ВРЕДИТЕЛИ-ОВОЩЕЙ---------------------------------------------\\\

##-------------------------------------------ВРЕДИТЕЛИ-ЯГОД-----------------------------------------------\\\
bugs_cherry_first = InlineKeyboardButton(
    text= "Бурый клещ 🪲",
    callback_data = "bugs_cherry_first_pressed",
)
bugs_cherry_second = InlineKeyboardButton(
    text= "Пилильщик Косточковый 🪲",
    callback_data = "bugs_cherry_second_pressed",
)
bugs_cherry_third = InlineKeyboardButton(
    text= "Побеговая моль 🪲",
    callback_data = "bugs_cherry_third_pressed",
)
bugs_cherry = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_cherry_first],[bugs_cherry_second],[bugs_cherry_third]]
)

bugs_watermelon_first = InlineKeyboardButton(
    text= "Базачевая Тля 🪲",
    callback_data = "bugs_watermelon_first_pressed",
)
bugs_watermelon_second = InlineKeyboardButton(
    text= "Паутинный Клещ 🪲",
    callback_data = "bugs_watermelon_second_pressed",
)
bugs_watermelon_third = InlineKeyboardButton(
    text= "Трипсы 🪲",
    callback_data = "bugs_watermelon_third_pressed",
)
bugs_watermelon = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_watermelon_first],[bugs_watermelon_second],[bugs_watermelon_third]]
)

bugs_strawberry_first = InlineKeyboardButton(
    text= "Тля 🪲",
    callback_data = "bugs_strawberry_first_pressed",
)
bugs_strawberry_second = InlineKeyboardButton(
    text= "Долгоносик 🪲",
    callback_data = "bugs_strawberry_second_pressed",
)
bugs_strawberry_third = InlineKeyboardButton(
    text= "Земляничный клеш 🪲",
    callback_data = "bugs_strawberry_third_pressed",
)
bugs_strawberry = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_strawberry_first],[bugs_strawberry_second],[bugs_strawberry_third]]
)

bugs_raspberry_first = InlineKeyboardButton(
    text= "Стеблевая Галлица 🪲",
    callback_data = "bugs_raspberry_first_pressed",
)
bugs_raspberry_second = InlineKeyboardButton(
    text= "Побеговая Тля 🪲",
    callback_data = "bugs_raspberry_second_pressed",
)
bugs_raspberry_third = InlineKeyboardButton(
    text= "Стеклянница 🪲",
    callback_data = "bugs_raspberry_third_pressed",
)
bugs_raspberry = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_raspberry_first],[bugs_raspberry_second],[bugs_raspberry_third]]
)

bugs_grape_first = InlineKeyboardButton(
    text= "Гроздевая листовертка 🪲",
    callback_data = "bugs_grape_first_pressed",
)
bugs_grape_second = InlineKeyboardButton(
    text= "Паутинный клещ 🪲",
    callback_data = "bugs_grape_second_pressed",
)
bugs_grape_third = InlineKeyboardButton(
    text= "Виноградный червь 🪲",
    callback_data = "bugs_grape_third_pressed",
)
bugs_grape = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_grape_first],[bugs_grape_second],[bugs_grape_third]]
)

bugs_gooseberries_first = InlineKeyboardButton(
    text= "Гусиница Галлица 🪲",
    callback_data = "bugs_gooseberries_first_pressed",
)
bugs_gooseberries_second = InlineKeyboardButton(
    text= "Тля 🪲",
    callback_data = "bugs_gooseberries_second_pressed",
)
bugs_gooseberries_third = InlineKeyboardButton(
    text= "Крыжовникавая огневка 🪲",
    callback_data = "bugs_gooseberries_third_pressed",
)
bugs_gooseberries = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_gooseberries_first],[bugs_gooseberries_second],[bugs_gooseberries_third]]
)

bugs_blueberry_first = InlineKeyboardButton(
    text= "Паутинный клещ 🪲",
    callback_data = "bugs_blueberry_first_pressed",
)
bugs_blueberry_second = InlineKeyboardButton(
    text= "Голубичная тля 🪲",
    callback_data = "bugs_blueberry_second_pressed",
)
bugs_blueberry_third = InlineKeyboardButton(
    text= "Голубичная муха 🪲",
    callback_data = "bugs_blueberry_third_pressed",
)
bugs_blueberry = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_blueberry_first],[bugs_blueberry_second],[bugs_blueberry_third]]
)

bugs_melon_first = InlineKeyboardButton(
    text= "Бахчевая тля🪲",
    callback_data = "bugs_melon_first_pressed",
)
bugs_melon_second = InlineKeyboardButton(
    text= "Паутинный клещ 🪲",
    callback_data = "bugs_melon_second_pressed",
)
bugs_melon_third = InlineKeyboardButton(
    text= "Дынная муха 🪲",
    callback_data = "bugs_melon_third_pressed",
)
bugs_melon = InlineKeyboardMarkup(
    inline_keyboard=[[bugs_melon_first],[bugs_melon_second],[bugs_melon_third]]
)
#--------------------------------------------------------------------УДОБРЕНИЯ---------------------------------------------------------------------------------------------------------\\\
#----------------------------------Удобрения-Фруктов--------------------------------------

fertilizer_apple_first = InlineKeyboardButton(
    text= "Удобрения яблони №1 📦",
    callback_data = "fertilizer_apple_first_pressed",
)
fertilizer_apple_second = InlineKeyboardButton(
    text= "Удобрения яблони №2 📦",
    callback_data = "fertilizer_apple_second_pressed",
)
fertilizer_apple_third = InlineKeyboardButton(
    text= "Удобрения яблони №3 📦",
    callback_data = "fertilizer_apple_third_pressed",
)
fertilizer_apple = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_apple_first],[fertilizer_apple_second],[fertilizer_apple_third]]
)


fertilizer_pear_first = InlineKeyboardButton(
    text= "Удобрения груши №1 📦",
    callback_data = "fertilizer_pear_first_pressed",
)
fertilizer_pear_second = InlineKeyboardButton(
    text= "Удобрения груши №2 📦",
    callback_data = "fertilizer_pear_second_pressed",
)
fertilizer_pear_third = InlineKeyboardButton(
    text= "Удобрения груши №3 📦",
    callback_data = "fertilizer_pear_third_pressed",
)
fertilizer_pear = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_pear_first],[fertilizer_pear_second],[fertilizer_pear_third]]
)


fertilizer_apricots_first = InlineKeyboardButton(
    text= "Удобрения абрикос №1 📦",
    callback_data = "fertilizer_apricots_first_pressed",
)
fertilizer_apricots_second = InlineKeyboardButton(
    text= "Удобрения абрикос №2 📦",
    callback_data = "fertilizer_apricots_second_pressed",
)
fertilizer_apricots_third = InlineKeyboardButton(
    text= "Удобрения абрикос №3 📦",
    callback_data = "fertilizer_apricots_third_pressed",
)
fertilizer_apricots = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_apricots_first],[fertilizer_apricots_second],[fertilizer_apricots_third]]
)


fertilizer_pomegranate_first = InlineKeyboardButton(
    text= "Удобрения граната №1 📦",
    callback_data = "fertilizer_pomegranate_first_pressed",
)
fertilizer_pomegranate_second = InlineKeyboardButton(
    text= "Удобрения граната №2 📦",
    callback_data = "fertilizer_pomegranate_second_pressed",
)
fertilizer_pomegranate_third = InlineKeyboardButton(
    text= "Удобрения граната №3 📦",
    callback_data = "fertilizer_pomegranate_third_pressed",
)
fertilizer_pomegranate = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_pomegranate_first],[fertilizer_pomegranate_second],[fertilizer_pomegranate_third]]
)


fertilizer_plums_first = InlineKeyboardButton(
    text= "Удобрения слив №1 📦",
    callback_data = "fertilizer_plums_first_pressed",
)
fertilizer_plums_second = InlineKeyboardButton(
    text= "Удобрения слив №2 📦",
    callback_data = "fertilizer_plums_second_pressed",
)
fertilizer_plums_third = InlineKeyboardButton(
    text= "Удобрения слив №3 📦",
    callback_data = "fertilizer_plums_third_pressed",
)
fertilizer_plums = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_plums_first],[fertilizer_plums_second],[fertilizer_plums_third]]
)


fertilizer_tangerines_first = InlineKeyboardButton(
    text= "Удобрения мандаринов №1 📦",
    callback_data = "fertilizer_tangerines_first_pressed",
)
fertilizer_tangerines_second = InlineKeyboardButton(
    text= "Удобрения мандаринов №2 📦",
    callback_data = "fertilizer_tangerines_second_pressed",
)
fertilizer_tangerines_third = InlineKeyboardButton(
    text= "Удобрения мандаринов №3 📦",
    callback_data = "fertilizer_tangerines_third_pressed",
)
fertilizer_tangerines = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_tangerines_first],[fertilizer_tangerines_second],[fertilizer_tangerines_third]])


fertilizer_peach_first = InlineKeyboardButton(
    text= "Удобрения персиков №1 📦",
    callback_data = "fertilizer_peach_first_pressed",
)
fertilizer_peach_second = InlineKeyboardButton(
    text= "Удобрения персиков №2 📦",
    callback_data = "fertilizer_peach_second_pressed",
)
fertilizer_peach_third = InlineKeyboardButton(
    text= "Удобрения персиков №3 📦",
    callback_data = "fertilizer_peach_third_pressed",
)
fertilizer_peach = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_peach_first],[fertilizer_peach_second],[fertilizer_peach_third]]
)

fertilizer_banana_first = InlineKeyboardButton(
    text= "Удобрения бананов №1 📦",
    callback_data = "fertilizer_banana_first_pressed",
)
fertilizer_banana_second = InlineKeyboardButton(
    text= "Удобрения бананов №2 📦",
    callback_data = "fertilizer_banana_second_pressed",
)
fertilizer_banana_third = InlineKeyboardButton(
    text= "Удобрения бананов №3 📦",
    callback_data = "fertilizer_banana_third_pressed",
)
fertilizer_banana = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_banana_first],[fertilizer_banana_second],[fertilizer_banana_third]]
)
#--------------------------------------УДОБРЕНИЯ-ОВОЩЕЙ------------------------------------------------------------------------------------------

#--------------------------------------УДОБРЕНИЯ-ЯГОД--------------------------------------------------------------------------------------------
fertilizer_cherry_first = InlineKeyboardButton(
    text= "Азот 📦",
    callback_data = "fertilizer_cherry_first_pressed",
)
fertilizer_cherry_second = InlineKeyboardButton(
    text= "Фосфор 📦",
    callback_data = "fertilizer_cherry_second_pressed",
)
fertilizer_cherry_third = InlineKeyboardButton(
    text= "Калий 📦",
    callback_data = "fertilizer_cherry_third_pressed",
)
fertilizer_cherry = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_cherry_first],[fertilizer_cherry_second],[fertilizer_cherry_third]]
)

fertilizer_watermelon_first = InlineKeyboardButton(
    text= "Азот 📦",
    callback_data = "fertilizer_watermelon_first_pressed",
)
fertilizer_watermelon_second = InlineKeyboardButton(
    text= "Фосфор 📦",
    callback_data = "fertilizer_watermelon_second_pressed",
)
fertilizer_watermelon_third = InlineKeyboardButton(
    text= "Калий 📦",
    callback_data = "fertilizer_watermelon_third_pressed",
)
fertilizer_watermelon = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_watermelon_first],[fertilizer_watermelon_second],[fertilizer_watermelon_third]]
)

fertilizer_strawberry_first = InlineKeyboardButton(
    text= "Азот 📦",
    callback_data = "fertilizer_strawberry_first_pressed",
)
fertilizer_strawberry_second = InlineKeyboardButton(
    text= "Фосфор 📦",
    callback_data = "fertilizer_strawberry_second_pressed",
)
fertilizer_strawberry_third = InlineKeyboardButton(
    text= "Калий 📦",
    callback_data = "fertilizer_strawberry_third_pressed",
)
fertilizer_strawberry = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_strawberry_first],[fertilizer_strawberry_second],[fertilizer_strawberry_third]]
)

fertilizer_raspberry_first = InlineKeyboardButton(
    text= "Азот 📦",
    callback_data = "fertilizer_raspberry_first_pressed",
)
fertilizer_raspberry_second = InlineKeyboardButton(
    text= "Фосфор 📦",
    callback_data = "fertilizer_raspberry_second_pressed",
)
fertilizer_raspberry_third = InlineKeyboardButton(
    text= "Калий 📦",
    callback_data = "fertilizer_raspberry_third_pressed",
)
fertilizer_raspberry = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_raspberry_first],[fertilizer_raspberry_second],[fertilizer_raspberry_third]]
)

fertilizer_grape_first = InlineKeyboardButton(
    text= "Азот 📦",
    callback_data = "fertilizer_grape_first_pressed",
)
fertilizer_grape_second = InlineKeyboardButton(
    text= "Фосфор 📦",
    callback_data = "fertilizer_grape_second_pressed",
)
fertilizer_grape_third = InlineKeyboardButton(
    text= "Калий 📦",
    callback_data = "fertilizer_grape_third_pressed",
)
fertilizer_grape = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_grape_first],[fertilizer_grape_second],[fertilizer_grape_third]]
)

fertilizer_gooseberries_first = InlineKeyboardButton(
    text= "Азот 📦",
    callback_data = "fertilizer_gooseberries_first_pressed",
)
fertilizer_gooseberries_second = InlineKeyboardButton(
    text= "Фосфор 📦",
    callback_data = "fertilizer_gooseberries_second_pressed",
)
fertilizer_gooseberries_third = InlineKeyboardButton(
    text= "Калий 📦",
    callback_data = "fertilizer_gooseberries_third_pressed",
)
fertilizer_gooseberries = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_gooseberries_first],[fertilizer_gooseberries_second],[fertilizer_gooseberries_third]]
)

fertilizer_blueberry_first = InlineKeyboardButton(
    text= "Азот 📦",
    callback_data = "fertilizer_blueberry_first_pressed",
)
fertilizer_blueberry_second = InlineKeyboardButton(
    text= "Фосфор 📦",
    callback_data = "fertilizer_blueberry_second_pressed",
)
fertilizer_blueberry_third = InlineKeyboardButton(
    text= "Калий 📦",
    callback_data = "fertilizer_blueberry_third_pressed",
)
fertilizer_blueberry = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_blueberry_first],[fertilizer_blueberry_second],[fertilizer_blueberry_third]]
)

fertilizer_melon_first = InlineKeyboardButton(
    text= "Азот 📦",
    callback_data = "fertilizer_melon_first_pressed",
)
fertilizer_melon_second = InlineKeyboardButton(
    text= "Фосфор 📦",
    callback_data = "fertilizer_melon_second_pressed",
)
fertilizer_melon_third = InlineKeyboardButton(
    text= "Калий 📦",
    callback_data = "fertilizer_melon_third_pressed",
)
fertilizer_melon = InlineKeyboardMarkup(
    inline_keyboard=[[fertilizer_melon_first],[fertilizer_melon_second],[fertilizer_melon_third]]
)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Все растения
all_button_plant = {"apple_button_pressed", "pear_button_pressed","apricots_button_pressed","pomegranate_button_pressed","plums_button_pressed","tangerines_button_pressed","peaches_button_pressed","banana_button_pressed",
                    "cabbage_button_pressed","cucumbers_button_pressed","tomato_button_pressed","potato_button_pressed", "corn_button_pressed","beets_button_pressed","wheat_button_pressed","oats_button_pressed",
                    "cherry_button_pressed","watermelon_button_pressed","strawberry_button_pressed","raspberry_button_pressed","grapes_button_pressed","gooseberries_button_pressed","blueberries_button_pressed","melon_button_pressed"}

desiese_plant = {"diseise_apple_first_pressed","diseise_apple_second_pressed","diseise_apple_third_pressed",
            "diseise_pear_first_pressed","diseise_pear_second_pressed","diseise_pear_third_pressed",
            "diseise_apricots_first_pressed","diseise_apricots_second_pressed","diseise_apricots_third_pressed",
            "diseise_pomegranate_first_pressed","diseise_pomegranate_second_pressed","diseise_pomegranate_third_pressed",
            "diseise_plums_first_pressed","diseise_plums_second_pressed","diseise_plums_third_pressed",
            "diseise_tangerines_first_pressed","diseise_tangerines_second_pressed","diseise_tangerines_third_pressed"
            "diseise_peach_first_pressed","diseise_peach_second_pressed","diseise_peach_third_pressed"
            "diseise_banana_first_pressed","diseise_banana_second_pressed","diseise_banana_third_pressed",

            "diseise_cherry_first_pressed","diseise_cherry_second_pressed","diseise_cherry_third_pressed",
            "diseise_watermelon_first_pressed","diseise_watermelon_second_pressed","diseise_watermelon_third_pressed",
            "diseise_strawberry_first_pressed","diseise_strawberry_second_pressed","diseise_strawberry_third_pressed",
            "diseise_raspberry_first_pressed","diseise_raspberry_second_pressed","diseise_raspberry_third_pressed",
            "diseise_grape_first_pressed","diseise_grape_second_pressed","diseise_grape_third_pressed",
            "diseise_gooseberries_first_pressed","diseise_gooseberries_second_pressed","diseise_gooseberries_third_pressed",
            "diseise_blueberry_first_pressed","diseise_blueberry_second_pressed","diseise_blueberry_third_pressed",
            "diseise_melon_first_pressed","diseise_melon_second_pressed","diseise_melon_third_pressed",
            }

bugs_plant = {"bugs_apple_first_pressed","bugs_apple_second_pressed","bugs_apple_third_pressed",
            "bugs_pear_first_pressed","bugs_pear_second_pressed","diseibugs_third_pressed",
            "bugs_apricots_first_pressed","bugs_apricots_second_pressed","bugs_apricots_third_pressed",
            "bugs_pomegranate_first_pressed","bugs_pomegranate_second_pressed","bugs_pomegranate_third_pressed",
            "bugs_plums_first_pressed","bugs_plums_second_pressed","bugs_plums_third_pressed",
            "bugs_tangerines_first_pressed","bugs_tangerines_second_pressed","bugs_tangerines_third_pressed"
            "bugs_peach_first_pressed","bugs_peach_second_pressed","bugs_peach_third_pressed"
            "bugs_banana_first_pressed","bugs_banana_second_pressed","bugs_banana_third_pressed"
            
            "bugs_cherry_first_pressed","bugs_cherry_second_pressed","bugs_cherry_third_pressed",
            "bugs_watermelon_first_pressed","bugs_watermelon_second_pressed","bugs_watermelon_third_pressed",
            "bugs_strawberry_first_pressed","bugs_strawberry_second_pressed","bugs_strawberry_third_pressed",
            "bugs_raspberry_first_pressed","bugs_raspberry_second_pressed","bugs_raspberry_third_pressed",
            "bugs_grape_first_pressed","bugs_grape_second_pressed","bugs_grape_third_pressed",
            "bugs_gooseberries_first_pressed","bugs_gooseberries_second_pressed","bugs_gooseberries_third_pressed",
            "bugs_blueberry_first_pressed","bugs_blueberry_second_pressed","bugs_blueberry_third_pressed",
            "bugs_melon_first_pressed","bugs_melon_second_pressed","bugs_melon_third_pressed",
            }

fertilizer_plant = {"fertilizer_apple_first_pressed","fertilizer_apple_second_pressed","fertilizer_apple_third_pressed",
                    "fertilizer_pear_first_pressed","fertilizer_pear_second_pressed","fertilizer_pear_third_pressed",
                    "fertilizer_apricots_first_pressed","fertilizer_apricots_second_pressed","fertilizer_apricots_third_pressed",
                    "fertilizer_pomegranate_first_pressed","fertilizer_pomegranate_second_pressed","fertilizer_pomegranate_third_pressed",
                    "fertilizer_plums_first_pressed","fertilizer_plums_second_pressed","fertilizer_plums_third_pressed",
                    "fertilizer_tangerines_first_pressed","fertilizer_tangerines_second_pressed","fertilizer_tangerines_third_pressed",
                    "fertilizer_peach_first_pressed","fertilizer_peach_second_pressed","fertilizer_peach_third_pressed",
                    "fertilizer_banana_first_pressed","fertilizer_banana_second_pressed","fertilizer_banana_third_pressed",

                    "fertilizer_cherry_first_pressed","fertilizer_cherry_second_pressed","fertilizer_cherry_third_pressed",
                    "fertilizer_watermelon_first_pressed","fertilizer_watermelon_second_pressed","fertilizer_watermelon_third_pressed",
                    "fertilizer_strawberry_first_pressed","fertilizer_strawberry_second_pressed","fertilizer_strawberry_third_pressed",
                    "fertilizer_raspberry_first_pressed","fertilizer_raspberry_second_pressed","fertilizer_raspberry_third_pressed",
                    "fertilizer_grape_first_pressed","fertilizer_grape_second_pressed","fertilizer_grape_third_pressed",
                    "fertilizer_gooseberries_first_pressed","fertilizer_gooseberries_second_pressed","fertilizer_gooseberries_third_pressed",
                    "fertilizer_blueberry_first_pressed","fertilizer_blueberry_second_pressed","fertilizer_blueberry_third_pressed",
                    "fertilizer_melon_first_pressed","fertilizer_melon_second_pressed","fertilizer_melon_third_pressed",
                    }
frstfertilizer = {"fertilizer_cherry_first_pressed","fertilizer_watermelon_first_pressed","fertilizer_strawberry_first_pressed","fertilizer_raspberry_first_pressed","fertilizer_grape_first_pressed","fertilizer_gooseberries_first_pressed","fertilizer_blueberry_first_pressed","fertilizer_melon_first_pressed",
}
scndfertilizer = {"fertilizer_cherry_second_pressed", "fertilizer_watermelon_second_pressed", "fertilizer_strawberry_second_pressed", "fertilizer_raspberry_second_pressed", "fertilizer_grape_second_pressed", "fertilizer_gooseberries_second_pressed", "fertilizer_blueberry_second_pressed", "fertilizer_melon_second_pressed",
}
thrdfertilizer = { "fertilizer_cherry_third_pressed", "fertilizer_watermelon_third_pressed", "fertilizer_strawberry_third_pressed", "fertilizer_raspberry_third_pressed", "fertilizer_grape_third_pressed", "fertilizer_gooseberries_third_pressed", "fertilizer_blueberry_third_pressed", "fertilizer_melon_third_pressed",

}
