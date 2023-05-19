from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from handlers.addresses import ChooseAddress
from keyboards.reply.main_menu import other_menu
from .responses import tg, phone

router = Router()

book = ["Хотим продлить бронь", "Возникли трудности", "Вернуться"]


@router.message(ChooseAddress.choosing_questions, F.text.casefold() == "прочие вопросы")
async def question_flat(message: Message, state: FSMContext) -> None:
    await state.update_data(question=message.text.lower())
    await state.set_state(ChooseAddress.other)
    await message.answer(
        f"Вы выбрали {message.text} что Вас интересует?",
        reply_markup=other_menu,
    )


@router.message(ChooseAddress.other)
async def handle_flat_questions(message: Message, state: FSMContext):
    await state.update_data(other=message.text.lower())

    if message.text.lower() == "хотим продлить бронь":
        await message.answer(
            f"Свяжитесь с арендодателем  по ссылке {tg}, либо по телефону: {phone}",
            parse_mode="HTML",
        )

    if message.text.lower() == "возникли трудности":
        await message.answer(
            f"Свяжитесь с арендодателем  по ссылке {tg}", parse_mode="HTML"
        )
