from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr
import os
# Загрузка переменных окружения из файла .env
load_dotenv()


class Settings(BaseSettings):
    bot_token: SecretStr = os.getenv('BOT_TOKEN')

    class Config:
        env_file_encoding = 'utf-8'

config = Settings()