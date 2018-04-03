import time
import datetime
import colorama
from colorama import Fore, Style
from settings import Settings

colorama.init(autoreset=True)

LOG_LEVELS = [
    Fore.LIGHTRED_EX +      "ERROR  ",
    Fore.LIGHTYELLOW_EX +   "WARNING",
    Fore.LIGHTCYAN_EX +     "LOG    ",
    Fore.LIGHTMAGENTA_EX +  "INFO   ",
    Fore.LIGHTGREEN_EX +    "SILLY  "
]


def get_time():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('[%Y-%m-%d %H:%M:%S]')


def out(str_in: str = "", log_level=2, override_level=False):
    log_level_str = LOG_LEVELS[log_level]
    if override_level or Settings(False).get_settings().log_level >= log_level:
        print("{0}{1}{2} {3}{4} - {5}".format(Style.DIM, get_time(), Style.NORMAL, log_level_str, Fore.WHITE, str_in))
