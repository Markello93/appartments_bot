from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.reply.main_menu import food_menu, leisure_menu, place_menu
from .addresses import ChooseAddress
from .responses import PLACES, RESTORAUNTS

router = Router()

leisure = ["Куда сходить в Иркутске?", "Где вкусно покушать?", "Вернуться"]


@router.message(ChooseAddress.choosing_questions, F.text.casefold() == "досуг")
async def question_irkutsk(message: Message, state: FSMContext) -> None:
    await state.update_data(question=message.text.lower())
    await state.set_state(ChooseAddress.leisure)
    await message.answer(
        "Вы выбрали Досуг, что Вас интересует?",
        reply_markup=leisure_menu,
    )


@router.message(ChooseAddress.leisure, F.text.casefold() == "куда сходить в иркутске?")
async def question_irkutsk(message: Message, state: FSMContext) -> None:
    await state.update_data(question_leisure=message.text.lower())
    await state.set_state(ChooseAddress.place)
    await message.answer(
        "Вас интересует куда можно сходить в Иркутске",
        reply_markup=place_menu,
    )


@router.message(ChooseAddress.leisure, F.text.casefold() == "где вкусно покушать?")
async def question_irkutsk(message: Message, state: FSMContext) -> None:
    await state.update_data(question_leisure=message.text.lower())
    await state.set_state(ChooseAddress.food)
    await message.answer(
        "Вас интересует где можно покушать в Иркутске",
        reply_markup=food_menu,
    )


@router.message(ChooseAddress.food)
async def handle_food_choice(message: Message, state: FSMContext):
    restaurant_name = message.text
    restaurants = [r for r in RESTORAUNTS if r["name"] == restaurant_name]
    if not restaurants:
        await message.answer("Извините, я не знаю такого места.")
        return
    else:
        restaurant = restaurants[0]
        text = f"{restaurant['name']}\n\n{restaurant['description']}\n\nАдрес: {restaurant['location']}\n\nМеню: {restaurant['menu']}\n\nГугл: {restaurant['google']}"
        await message.answer(text=text)
        await message.answer_photo(restaurant["photo"], parse_mode="HTML")
        await state.update_data(previous_state=ChooseAddress.food)


@router.message(ChooseAddress.place)
async def handle_place_choice(message: Message, state: FSMContext):
    place_name = message.text
    places = [r for r in PLACES if r["name"] == place_name]

    if not places:
        await message.answer("Извините, я не знаю такого места.")
        return
    else:
        place = places[0]
        text = f"{place['name']}\n\n{place['description']}\n\nАдрес: {place['location']}\n\nГугл: {place['google']}"
        await message.answer(text=text)
        await message.answer_photo(place["photo"], parse_mode="HTML")
