from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from keyboards.reply import main_menu
from .responses import available_addresses

router = Router()

main_questions = ["Вопросы по квартире", "Досуг", "Прочие вопросы", "Вернуться"]


class ChooseAddress(StatesGroup):
    choosing_address = State()
    choosing_questions = State()
    leisure = State()
    flat = State()
    other = State()
    food = State()
    place = State()


@router.message(ChooseAddress.choosing_address, F.text.in_(available_addresses))
async def address_chosen(message: Message, state: FSMContext):
    await state.update_data(address=message.text.lower())
    await state.set_state(ChooseAddress.choosing_questions)
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, выберите интересующую Вас информацию:",
        reply_markup=main_menu,
    )
