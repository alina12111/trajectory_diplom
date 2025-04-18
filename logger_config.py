import logging
import os

# Створюємо папку для логів, якщо її ще немає
os.makedirs("logs", exist_ok=True)

# Формат повідомлень
log_format = "%(asctime)s [%(levelname)s]: %(message)s"

# Налаштування логера
logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("logs/error.log", mode='w'),
        logging.FileHandler("logs/combined.log", mode='w'),
        logging.StreamHandler()
    ]
)

# Імпортний логер для використання у всіх модулях
logger = logging.getLogger("trajectory_logger")
