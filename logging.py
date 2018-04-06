import time
import datetime
import colorama
from colorama import Fore, Style
from settings import Settings

colorama.init(autoreset=True)

LOG_LEVELS = [
    Fore.LIGHTRED_EX        + "ERROR  ",
    Fore.LIGHTYELLOW_EX     + "WARNING",
    Fore.LIGHTCYAN_EX       + "LOG    ",
    Fore.LIGHTMAGENTA_EX    + "INFO   ",
    Fore.LIGHTGREEN_EX      + "SILLY  "
]


def get_time() -> str:
    """Returns a formatted timestamp string
    
    Returns:
        str -- Formatted timestamp string
    """
    
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('[%Y-%m-%d %H:%M:%S]')


def out(str_in: str = "", log_level=2, override_level=False) -> None:
    """Outputs a formatted log of the input string to the console.

    The output is printed in the following format:
        [{timestamp}] {log level} - {string input}
    Example: 
        [2018-04-06 12:24:50] INFO  - This is an example log.
    
    Keyword Arguments:
        str_in {str} -- String to output (default: {""})
        log_level {int} -- Level to log against. See docs. (default: {2})
        override_level {bool} -- Output log regardless of log_level setting. (default: {False})
    """

    log_level_str = LOG_LEVELS[log_level]
    if override_level or Settings(False).get_settings().log_level >= log_level:
        print("{0}{1}{2} {3}{4} - {5}".format(Style.DIM, get_time(), Style.NORMAL, log_level_str, Fore.WHITE, str_in))
