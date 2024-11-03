from aiogram import Router, F
from aiogram.types import Message, InputMediaPhoto, FSInputFile, CallbackQuery

from FHB_TEST.button import desiese_apple, desiese_pear, desiese_apricots, desiese_pomegranate, desiese_plums, \
    desiese_tangerines, desiese_peach, desiese_banana, back_to_beginning_keyboard, desiese_plant, \
    select_theme, desiese_cherry,desiese_watermelon,desiese_strawberry,desiese_raspberry,desiese_grape,desiese_gooseberries,desiese_blueberry,desiese_melon
from FHB_TEST.button import bugs_apple, bugs_pear, bugs_apricots, bugs_pomegranate, bugs_plums, \
    bugs_tangerines, bugs_peach, bugs_banana, back_to_beginning_keyboard, bugs_plant, all_button_plant, \
    select_theme,bugs_cherry,bugs_watermelon,bugs_strawberry,bugs_raspberry,bugs_grape,bugs_gooseberries,bugs_blueberry,bugs_melon
from FHB_TEST.button import fertilizer_apple, fertilizer_pear, fertilizer_apricots, fertilizer_pomegranate, fertilizer_plums, \
    fertilizer_tangerines, fertilizer_peach, fertilizer_banana, back_to_beginning_keyboard, fertilizer_plant, all_button_plant, \
    select_theme,fertilizer_cherry,fertilizer_watermelon,fertilizer_strawberry,fertilizer_raspberry,fertilizer_grape,fertilizer_gooseberries,fertilizer_blueberry,fertilizer_melon,frstfertilizer,scndfertilizer,thrdfertilizer
from LEXICON import *
id_plant = "NONE"
id_theme = "NONE"
id_category = "NONE"

router = Router()

#----------------------------------------------------------------------БОЛЕЗНИ-----------------------------------------------------------------------------------

#Появление списка выбора темы
@router.callback_query(F.data.in_(all_button_plant))
async def process_theme_press(callback: CallbackQuery):
    global id_plant
    id_plant = callback.data                                                             #Регистрация ID Растения

    await callback.message.edit_media(
        InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/theme.png")),
        reply_markup=select_theme

    )
    print(id_plant)

#Выбор Болезней растений
@router.callback_query(F.data == "disease_button_pressed")
async def process_disease_press(callback: CallbackQuery):
    global id_theme
    id_theme = callback.data                                                             #Регистрация ID Темы
    print(id_theme)
    if id_plant == "apple_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь яблони"),
            reply_markup= desiese_apple
        )
    elif id_plant == "pear_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь груши"),
            reply_markup= desiese_pear
        )
    elif id_plant == "apricots_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь абрикос"),
            reply_markup= desiese_apricots
        )
    elif id_plant == "pomegranate_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь граната"),
            reply_markup= desiese_pomegranate
        )
    elif id_plant == "plums_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь слив"),
            reply_markup= desiese_plums
        )
    elif id_plant == "tangerines_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь мандарин"),
            reply_markup= desiese_tangerines
        )
    elif id_plant == "peaches_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь персиков"),
            reply_markup= desiese_peach
        )
    elif id_plant == "banana_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь бананов"),
            reply_markup= desiese_banana
        )

        #ЯГОДЫ
    elif id_plant == "cherry_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь вишни"),
            reply_markup= desiese_cherry
        )
    elif id_plant == "watermelon_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь арбузов"),
            reply_markup= desiese_watermelon
        )
    elif id_plant == "strawberry_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь клубника"),
            reply_markup= desiese_strawberry
        )
    elif id_plant == "raspberry_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь малины"),
            reply_markup= desiese_raspberry
        )
    elif id_plant == "grapes_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь винограда"),
            reply_markup= desiese_grape
        )
    elif id_plant == "gooseberies_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь крыжовника"),
            reply_markup= desiese_gooseberries
        )
    elif id_plant == "blueberry_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь голубики"),
            reply_markup= desiese_blueberry
        )
    elif id_plant == "melon_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="Выберите Интересующую болезнь Дыни"),
            reply_markup= desiese_melon
        )

    else:
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/desise.png"), caption="EROR"),
            reply_markup=back_to_beginning_keyboard
        )

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Появление ответов на Болезни
@router.callback_query(F.data.in_ (desiese_plant))
async def process_fertilizer_press(callback: CallbackQuery):
    global id_category
    id_category = callback.data
    print(id_category)                                                             #Регистрация ID Категории
    if id_plant == "apple_button_pressed":
        if id_category == "diseise_apple_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 1 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_apple_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 2 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_apple_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 3 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "pear_button_pressed":
        if id_category == "diseise_pear_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 1 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_pear_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 2 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_pear_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 3 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "apricots_button_pressed":
        if id_category == "diseise_apricots_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 1 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_apricots_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 2 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_apricots_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 3 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "pomegranate_button_pressed":
        if id_category == "diseise_pomegranate_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 1 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_pomegranate_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 2 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_pomegranate_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 3 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "pomegranate_button_pressed":
        if id_category == "diseise_pomegranate_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 1 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_pomegranate_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 2 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_pomegranate_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 3 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "plums_button_pressed":
        if id_category == "diseise_plums_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 1 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_plums_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 2 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_plums_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 3 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "tangerines_button_pressed":
        if id_category == "diseise_tangerines_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 1 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_tangerines_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 2 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_tangerines_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 3 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "peaches_button_pressed":
        if id_category == "diseise_peach_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 1 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_peach_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 2 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_peach_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 3 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "banana_button_pressed":
        if id_category == "diseise_banana_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 1 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_banana_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 2 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_banana_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/apple_desiese1.png"), caption="Информация про 3 болезнь"),
                reply_markup=back_to_beginning_keyboard
            )
    #ягоды
    elif id_plant == "cherry_button_pressed":
        if id_category == "diseise_cherry_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/kokkomikoz_cherry.png"), caption=komikoz_desiese_cherry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_cherry_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/klyasterosporioz_cherry.jpg"), caption=klyasterosporioz_desiese_cherry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_cherry_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/moniliziom_cherry.jpg"), caption=moniliozom_desiese_cherry),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "strawberry_button_pressed":
        if id_category == "diseise_strawberry_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/pyatnistot_strawberry.jpg"), caption=buraya_pyatnistost_desiese_strawberry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_strawberry_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/septorioz_strawberry.jpg"), caption=septorioz_desiese_strawberry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_strawberry_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/verticilez_strawberry.jpg"), caption=vertchillez_desiese_strawberry),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "watermelon_button_pressed":
        if id_category == "diseise_watermelon_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/antraknoz_watermelon.jpg"), caption=antraknoz_desiese_watermelon),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_watermelon_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/sklerotiniya_watermelon.jpg"), caption=sklerotiniya_desiese_watermelon),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_watermelon_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/uglovaya_pyatnistost_watermelon.jpg"), caption=pyatnistost_desise_watermelon),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "raspberry_button_pressed":
        if id_category == "diseise_raspberry_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/antraknoz_raspberry.jpg"), caption=antraknoz_desiese_raspberry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_raspberry_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/gray_gnil_raspberry.jpg"), caption=gray_gnil_desiese_raspberry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_raspberry_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/rust_raspberry.jpg"), caption=rust_desiese_raspberry),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "grapes_button_pressed":
        if id_category == "diseise_grape_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/krasnuha_grape.jpg"), caption=krasnuha_desiese_grape),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_grape_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/oidium_grape.jpg"), caption=oidium_desiese_grape),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_grape_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/mildu_grape.jpg"), caption = mildu_desiese_grape1 + mildu_desiese_grape2),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "gooseberries_button_pressed":
        if id_category == "diseise_gooseberries_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/rust_gooseberries.jpg"), caption=rust_desiese_gooseberries),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_gooseberries_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/antraknoz_gooseberries.jpg"), caption=antraknoz_desiese_gooseberries),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_gooseberries_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/septorioz_gooseberries.jpg"), caption=septorioz_desiese_gooseberries),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "blueberry_button_pressed":
        if id_category == "diseise_blueberry_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/rak_blueberry.jpg"), caption=rak_steblya_desiese_blueberry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_blueberry_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/fomopsis_blueberry.jpg"), caption=fomopsis_desiese_blueberry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_blueberry_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/botritis_blueberry.jpg"), caption=botritis_desiese_blueberry),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "melon_button_pressed":
        if id_category == "diseise_melon_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/rosa_melon.jpg"), caption=muchnistaya_rosa_desiese_melon),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_melon_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/fuzarioznoe_melon.jpg"), caption=fuzarioznoe_uvidanie_desiese_melon),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "diseise_melon_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_desiese_plant/antraknoz_melon.jpg"), caption=antraknoz_desiese_melon),
                reply_markup=back_to_beginning_keyboard
            )

#--------------------------------------------------------------------//ВРЕДИТЕЛИ\\---------------------------------------------------------------..//////////

#Выбор Вредителей растений
@router.callback_query(F.data == "bugs_button_pressed")
async def process_disease_press(callback: CallbackQuery):
    global id_plant
    print(id_plant)

    global id_theme
    id_theme = callback.data                                                             #Регистрация ID Темы
    print(id_theme)
    if id_plant == "apple_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"), caption="Выберите Интересующих вредителей яблони"),
            reply_markup= bugs_apple
        )
    elif id_plant == "pear_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"), caption="Выберите Интересующих вредителей груши"),
            reply_markup= bugs_pear
        )
    elif id_plant == "apricots_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"), caption="Выберите Интересующих вредителей абрикос"),
            reply_markup= bugs_apricots
        )
    elif id_plant == "pomegranate_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"), caption="Выберите Интересующих вредителей граната"),
            reply_markup= bugs_pomegranate
        )
    elif id_plant == "plums_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"), caption="Выберите Интересующих вредителей слив"),
            reply_markup= bugs_plums
        )
    elif id_plant == "tangerines_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"), caption="Выберите Интересующих вредителей мандарин"),
            reply_markup= bugs_tangerines
        )
    elif id_plant == "peaches_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"), caption="Выберите Интересующих вредителей персиков"),
            reply_markup= bugs_peach
        )
    elif id_plant == "banana_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"), caption="Выберите Интересующих вредителей бананов"),
            reply_markup= bugs_banana
        )
    #Ягоды

    elif id_plant == "cherry_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"),
                            caption="Выберите Интересующих вредителей вишни"),
            reply_markup=bugs_cherry
        )
    elif id_plant == "watermelon_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"),
                            caption="Выберите Интересующих вредителей арбуза"),
            reply_markup=bugs_watermelon
        )
    elif id_plant == "strawberry_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"),
                            caption="Выберите Интересующих вредителей клубники"),
            reply_markup=bugs_strawberry
        )
    elif id_plant == "raspberry_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"),
                            caption="Выберите Интересующих вредителей малины"),
            reply_markup=bugs_raspberry
        )
    elif id_plant == "grapes_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"),
                            caption="Выберите Интересующих вредителей винограда"),
            reply_markup=bugs_grape
        )
    elif id_plant == "gooseberries_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"),
                            caption="Выберите Интересующих вредителей крыжовника"),
            reply_markup=bugs_gooseberries
        )
    elif id_plant == "blueberry_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"),
                            caption="Выберите Интересующих вредителей голубики"),
            reply_markup=bugs_blueberry
        )
    elif id_plant == "melon_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"),
                            caption="Выберите Интересующих вредителей дыни"),
            reply_markup=bugs_melon
        )
    else:
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/bugs.png"), caption="EROR"),
            reply_markup=back_to_beginning_keyboard
        )




# Появление ответов на Вредителей
@router.callback_query(F.data.in_ (bugs_plant))
async def process_fertilizer_press(callback: CallbackQuery):
    global id_category
    id_category = callback.data
    print(id_category)                                                             #Регистрация ID Категории

    if id_plant == "apple_button_pressed":
        if id_category == "bugs_apple_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 1 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_apple_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 2 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_apple_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 3 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "pear_button_pressed":
        if id_category == "bugs_pear_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 1 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_pear_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 2 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_pear_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 3 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "apricots_button_pressed":
        if id_category == "bugs_apricots_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 1 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_apricots_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 2 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_apricots_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 3 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "pomegranate_button_pressed":
        if id_category == "bugs_pomegranate_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 1 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_pomegranate_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 2 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_pomegranate_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 3 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "pomegranate_button_pressed":
        if id_category == "bugs_pomegranate_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 1 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_pomegranate_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 2 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_pomegranate_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 3 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "plums_button_pressed":
        if id_category == "bugs_plums_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 1 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_plums_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 2 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_plums_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 3 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "tangerines_button_pressed":
        if id_category == "bugs_tangerines_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 1 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_tangerines_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 2 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_tangerines_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 3 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "peaches_button_pressed":
        if id_category == "bugs_peach_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 1 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_peach_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 2 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_peach_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 3 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "banana_button_pressed":
        if id_category == "bugs_banana_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 1 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_banana_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 2 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_banana_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bugs_apple_1.png"), caption="Информация про 3 Вредителей"),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "cherry_button_pressed":
        if id_category == "bugs_cherry_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/klesh_cherry.jpg"), caption=klesh_buriy_bugs_cherry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_cherry_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/pililshik_cherry.jpg"), caption=pililshik_bugs_cherry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_cherry_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/mol_cherry.jpg"), caption=mol_pobegavaya_bugs_cherry),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "watermelon_button_pressed":
        if id_category == "bugs_watermelon_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/tlya_watermelon.jpg"), caption=bahachevaya_tlya_bugs_watermelon),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_watermelon_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/pautinniy_klesh_watermelon.jpg"), caption=pautinniy_klesh_bugs_watermelon),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_watermelon_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/tripsy_watermelon.jpg"), caption=tripsy_bugs_watermelon),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "strawberry_button_pressed":
        if id_category == "bugs_strawberry_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/tlya_strawberry.png"), caption=klubnichnaya_tlya_bugs_strawberry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_strawberry_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/dolgonosik_strawberry.png"), caption=klubnichniy_dolgonosik_bugs_strawberry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_strawberry_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/klesh_strawberry.jpg"), caption=zemlyanichniy_klesh),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "raspberry_button_pressed":
        if id_category == "bugs_raspberry_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/galica_raspberry.jpg_raspberry.jpg"), caption=galica_bugs_raspberry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_raspberry_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/tlya_raspberry.png"), caption=pobegavaya_tlya_bugs_raspberry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_raspberry_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/steklyannica_raspberry.jpg"), caption=steklyanicca_bugs_raspberry),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "grapes_button_pressed":
        if id_category == "bugs_grape_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/listovertka_grape.jpg"), caption=grozdevaya_listovertka_bugs_grape),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_grape_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/klesh_grape.jpg"), caption=pautinniy_klesh_bugs_grape),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_grape_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/chervec_grape.jpg"), caption=vinogradoviy_chervec_bugs_grape),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "gooseberries_button_pressed":
        if id_category == "bugs_gooseberries_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/galica_gooseberries.jpg"), caption=galica_bugs_gooseberries),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_gooseberries_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/tlya_gooseberris.jpg"), caption=tlya_bugs_gooseberries),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_gooseberries_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/ognevka_gooseberries.jpg"), caption=ognevka_bugs_gooseberries),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "blueberry_button_pressed":
        if id_category == "bugs_blueberry_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/klesh_blueberry.jpg"), caption=pautinniy_klesh_bugs_blueberry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_blueberry_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/tlya_blueberry.jpg"), caption=golubichnaya_tlya_bugs_blueberry),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_blueberry_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/muha_blueberry.jpg"), caption=golubichnaya_muha_bugs_blueberry),
                reply_markup=back_to_beginning_keyboard
            )
    elif id_plant == "melon_button_pressed":
        if id_category == "bugs_melon_first_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/bahchevaya_tlya_melon.jpg"), caption=bahachevaya_tlya_bugs_melon),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_melon_second_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/pautinniy_klesh_melon.jpg"), caption=pautinniy_klesh_bugs_melon),
                reply_markup=back_to_beginning_keyboard
            )
        elif id_category == "bugs_melon_third_pressed":
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_bugs_plant/muha_melon.jpg"), caption=dinnaya_muha_bugs_melon),
                reply_markup=back_to_beginning_keyboard
            )


#--------------------------------------------------------------------УДОБРЕНИЯ----------------------------------------------------------------------------------

#Выбор Удобрения растений
@router.callback_query(F.data == "fertilizer_button_pressed")
async def process_disease_press(callback: CallbackQuery):
    global id_plant
    print(id_plant)

    global id_theme
    id_theme = callback.data                                                             #Регистрация ID Темы
    print(id_theme)
    if id_plant == "apple_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения яблони"),
            reply_markup= fertilizer_apple
        )
    elif id_plant == "pear_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения груши"),
            reply_markup= fertilizer_pear
        )
    elif id_plant == "apricots_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения абрикос"),
            reply_markup= fertilizer_apricots
        )
    elif id_plant == "pomegranate_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения граната"),
            reply_markup= fertilizer_pomegranate
        )
    elif id_plant == "plums_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения слив"),
            reply_markup= fertilizer_plums
        )
    elif id_plant == "tangerines_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения мандарин"),
            reply_markup= fertilizer_tangerines
        )
    elif id_plant == "peaches_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения персиков"),
            reply_markup= fertilizer_peach
        )
    elif id_plant == "banana_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения бананов"),
            reply_markup= fertilizer_banana
        )

    elif id_plant == "cherry_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения вишни"),
            reply_markup= fertilizer_cherry
        )
    elif id_plant == "watermelon_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения арбуза"),
            reply_markup= fertilizer_watermelon
        )
    elif id_plant == "strawberry_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения клубники"),
            reply_markup= fertilizer_strawberry
        )
    elif id_plant == "raspberry_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения малины"),
            reply_markup= fertilizer_raspberry
        )
    elif id_plant == "grapes_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения винограда"),
            reply_markup= fertilizer_grape
        )
    elif id_plant == "gooseberries_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения крыжовника"),
            reply_markup= fertilizer_gooseberries
        )
    elif id_plant == "blueberry_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения голубики"),
            reply_markup= fertilizer_blueberry
        )
    elif id_plant == "melon_button_pressed":
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="Выберите Интересующие удобрения дыни"),
            reply_markup= fertilizer_melon
        )

    else:
        await callback.message.edit_media(
            InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_menu/fertilizer.png"), caption="EROR"),
            reply_markup=back_to_beginning_keyboard
        )



# Появление ответов на Вредителей
@router.callback_query(F.data.in_ (fertilizer_plant))
async def process_fertilizer_press(callback: CallbackQuery):
    global id_category
    id_category = callback.data
    print(id_category)  # Регистрация ID Категории
    if id_plant in (all_button_plant):
        if id_category in (frstfertilizer):
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/Azot.jpg"),caption=azot),
                reply_markup=back_to_beginning_keyboard
            )

        if id_category in (scndfertilizer):
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/phosphor.jpg"),caption=phosphor),
                reply_markup=back_to_beginning_keyboard
            )

        if id_category in (thrdfertilizer):
            await callback.message.edit_media(
                InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/kaliy.jpg"),caption=kaliy),
                reply_markup = back_to_beginning_keyboard
            )
    # if id_plant == "apple_button_pressed":
    #     if id_category == "fertilizer_apple_first_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 1 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_apple_second_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 2 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_apple_third_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 3 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    # elif id_plant == "pear_button_pressed":
    #     if id_category == "fertilizer_pear_first_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 1 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_pear_second_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 2 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_pear_third_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 3 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    # elif id_plant == "apricots_button_pressed":
    #     if id_category == "fertilizer_apricots_first_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 1 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_apricots_second_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 2 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_apricots_third_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 3 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    # elif id_plant == "pomegranate_button_pressed":
    #     if id_category == "fertilizer_pomegranate_first_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 1 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_pomegranate_second_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 2 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_pomegranate_third_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 3 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    # elif id_plant == "pomegranate_button_pressed":
    #     if id_category == "fertilizer_pomegranate_first_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 1 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_pomegranate_second_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 2 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_pomegranate_third_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 3 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    # elif id_plant == "plums_button_pressed":
    #     if id_category == "fertilizer_plums_first_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 1 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_plums_second_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 2 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_plums_third_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 3 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    # elif id_plant == "tangerines_button_pressed":
    #     if id_category == "fertilizer_tangerines_first_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 1 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_tangerines_second_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 2 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_tangerines_third_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 3 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    # elif id_plant == "peaches_button_pressed":
    #     if id_category == "fertilizer_peach_first_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 1 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_peach_second_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 2 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_peach_third_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 3 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    # elif id_plant == "banana_button_pressed":
    #     if id_category == "fertilizer_banana_first_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 1 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_banana_second_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 2 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
    #     elif id_category == "fertilizer_banana_third_pressed":
    #         await callback.message.edit_media(
    #             InputMediaPhoto(media=FSInputFile("../FHB_TEST/photo_fertilizer_plant/fertilizer_apple_1.png"),
    #                             caption="Информация про 3 удобрения"),
    #             reply_markup=back_to_beginning_keyboard
    #         )
