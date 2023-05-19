from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура для главного меню
address_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Юбилейный 117/1,кв 126"),
        KeyboardButton(text="Свердлова 8,кв 44"),
        KeyboardButton(text="Сибиряков")
    ]
])


main_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Вопросы по квартире"),
        KeyboardButton(text="Досуг")
    ],
    [
        KeyboardButton(text="Прочие вопросы"),
        KeyboardButton(text="Назад")
    ]
])

# Клавиатура для раздела "Досуг"
leisure_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Куда сходить в Иркутске?")
    ],
    [
        KeyboardButton(text="Где вкусно покушать?")
    ],
    [
        KeyboardButton(text="Назад")
    ]
])

# Клавиатура для раздела "Вопросы по квартире"
flat_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Где взять постельное белье?")
    ],
    [
        KeyboardButton(text="Дополнительный комплект белья")
    ],
    [
        KeyboardButton(text="Куда выкинуть мусор?")
    ],
    [
        KeyboardButton(text="Пароль от вайфая?")
    ],
    [
        KeyboardButton(text="Где ближайший магазин?")
    ],
    [
        KeyboardButton(text="Назад")
    ]
])

# Клавиатура для раздела "Прочие вопросы"
other_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Хотим продлить бронь")
    ],
    [
        KeyboardButton(text="Возникли трудности")
    ],
    [
        KeyboardButton(text="Назад")
    ]
])

food_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Кочевник")
    ],
    [
        KeyboardButton(text="Позная 38")
    ],
    [
        KeyboardButton(text="Марко Поло")
    ],
    [
        KeyboardButton(text="The Library Bar")
    ],
    [
        KeyboardButton(text="Назад")
    ]
])

place_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="130 квартал")
    ],
    [
        KeyboardButton(text="Нижняя набережная Ангары")
    ],
    [
        KeyboardButton(text="Музей-ледокол 'Ангара'")
    ],
    [
        KeyboardButton(text="Кайская роща")
    ],
    [
        KeyboardButton(text="Иркутский областной краеведческий музей")
    ],
    [
        KeyboardButton(text="Иркутский областной художественный музей")
    ],
    [
        KeyboardButton(text="Назад")
    ]
])


