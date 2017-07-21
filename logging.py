import os
import sys
import time
import datetime
import colorama
from colorama import Fore, Back, Style
from settings import Settings

colorama.init(autoreset=True)

LOG_LEVELS = ["ERROR  ", "WARNING", "INFO   ", "LOG    ", "SILLY  "]

def getTime():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('[%Y-%m-%d %H:%M:%S]')
    # '[%Y-%m-%d %H:%M:%S] ' if you want a full timestamp


def out(input: str = "", log_level=2):
    if Settings().get_settings().log_level >= log_level:
        log_level_str = LOG_LEVELS[log_level]
        print("{0}{1}{2} {3}{4} - {5}".format(Style.DIM, getTime(), Style.NORMAL+Fore.LIGHTCYAN_EX, log_level_str,Fore.WHITE, input))
