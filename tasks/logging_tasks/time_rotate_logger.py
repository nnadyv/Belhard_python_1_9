"""
Настроить логгирование с модулем logging.

Настроить формат вывода.
Настроить, чтобы вывод шел в файл и в консоль.
Настроить ротацию файла лога по времени (полночь).
"""
import logging
from logging.handlers import TimedRotatingFileHandler

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.txt"
)
my_logger = logging.getLogger(__name__)
write_to_log = logging.StreamHandler()
rotate_my_log = TimedRotatingFileHandler("log.txt", when="midnight")
my_logger.addHandler(write_to_log)
my_logger.addHandler(rotate_my_log)
