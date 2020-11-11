import os
from threading import Lock
s_print_lock = Lock()


def s_print(*a, **b):
    """Thread safe print func"""
    with s_print_lock:
        print(*a, **b)


def clear(): os.system('cls')