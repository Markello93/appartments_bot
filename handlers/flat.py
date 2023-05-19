from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.reply.main_menu import flat_menu
from .responses import ADDRESS_ANSWERS
from .addresses import ChooseAddress

router = Router()

flat = [
    "Где взять постельное белье?",
    "Дополнительный комплект белья",
    "Куда выкинуть мусор?",
    "Пароль от вайфая?",
    "Где ближайший магазин?",
    "Вернуться",
]


@router.message(
    ChooseAddress.choosing_questions, F.text.casefold() == "вопросы по квартире"
)
async def question_flat(message: Message, state: FSMContext) -> None:
    await state.update_data(question=message.text.lower())
    await state.set_state(ChooseAddress.flat)
    await state.update_data(previous_state=ChooseAddress.choosing_questions)
    await message.answer(
        f"Вы выбрали {message.text} что Вас интересует?",
        reply_markup=flat_menu,
    )


@router.message(ChooseAddress.flat)
async def handle_flat_questions(message: Message, state: FSMContext):
    data = await state.get_data()
    current_address = data["address"]
    question = message.text.lower()

    if current_address.lower() in ADDRESS_ANSWERS:
        if question in ADDRESS_ANSWERS[current_address]:
            answer = ADDRESS_ANSWERS[current_address][question]
            if isinstance(answer, str):
                await message.answer(text=answer)
            elif isinstance(answer, tuple):
                await message.answer(text=answer[0])
                await message.answer_photo(answer[1], parse_mode="HTML")
        else:
            await message.answer(text="Не могу ответить на этот вопрос")
    else:
        await message.answer(text="Неизвестный адрес")
