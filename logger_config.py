import logging
from logging.handlers import RotatingFileHandler
import os

# Створюємо папку для логів
os.makedirs("logs", exist_ok=True)

# Формат повідомлення з контекстом користувача
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] [%(name)s] [%(user)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Базовий логер
logger = logging.getLogger("trajectory_logger")
logger.setLevel(logging.DEBUG)

# Консольний обробник
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Файловий обробник з ротацією за розміром
file_handler = RotatingFileHandler("logs/combined.log", maxBytes=500000, backupCount=5)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Функція для створення адаптованого логера з контекстом
def get_logger_with_user(user_id):
    return logging.LoggerAdapter(logger, {"user": user_id})
