import os

from dotenv import load_dotenv

# если есть .env - подгружаем окружение
load_dotenv()

# подбираем из окружения переменные для доступа к БД
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
