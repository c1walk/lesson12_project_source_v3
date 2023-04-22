import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)

new_logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("app.log", mode='w', encoding='utf-8')

formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
file_handler.setFormatter(formatter)

new_logger.addHandler(file_handler)
