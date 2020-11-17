import csv
import os
from threading import Lock

from game_classes import Database, Player

s_print_lock = Lock()


def s_print(*a, **b):
    """Thread safe print func"""
    with s_print_lock:
        print(*a, **b)


def clear(): os.system('cls')

def setup_database():
    with open('res/data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        array = []
        for row in csv_reader:
            array.append(
                Player(row["Player"], row["Position"], row["Games"], row["Win rate"], row["KDA"], row["CSM"],
                       row["GPM"],
                       row["KP%"], row["DMG%"]))
        return Database(array)
