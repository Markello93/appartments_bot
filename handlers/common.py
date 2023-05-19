from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from .addresses import ChooseAddress
from keyboards.reply import main_menu
from keyboards.reply.main_menu import address_menu, leisure_menu

router = Router()


@router.message(Command(commands=["start"]))
@router.message(Text(text="Выбрать другой адрес", ignore_case=True))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Благодарим,что выбрали нас!надеемся,что ваше пребывание в наших апартаментах пройдет максимально комфортно для вас 🧡\n\n"
        "Выберите адрес:",
        reply_markup=address_menu,
    )
    await state.set_state(ChooseAddress.choosing_address)


@router.message(Command(commands=["back"]))
@router.message(Text(text="назад", ignore_case=True))
async def cmd_back(message: Message, state: FSMContext):
    # Получаем предыдущее состояние из данных FSMContext
    current_state = await state.get_state()

    if current_state == "ChooseAddress:choosing_questions":
        await state.set_state(ChooseAddress.choosing_address)
        await message.answer(text="Выберите адрес:", reply_markup=address_menu)

    elif current_state in [
        "ChooseAddress:leisure",
        "ChooseAddress:other",
        "ChooseAddress:flat",
    ]:
        await state.set_state(ChooseAddress.choosing_questions)
        await message.answer(
            text="Спасибо. Теперь, пожалуйста, выберите интересующую Вас информацию:",
            reply_markup=main_menu,
        )
    elif current_state in ["ChooseAddress:place", "ChooseAddress:food"]:
        await state.set_state(ChooseAddress.leisure)
        await message.answer(
            "Вы выбрали Досуг, что Вас интересует?",
            reply_markup=leisure_menu,
        )
    else:
        await message.answer("Не удалось вернуться назад.", reply_markup=address_menu)
