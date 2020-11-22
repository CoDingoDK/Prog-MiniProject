import csv
import os
from threading import Lock
from game_classes import Database, Player

s_print_lock = Lock()


def s_print(*a, **b):
    # Thread safe print func, easier debugging if multiple threads printing at the same time.
    with s_print_lock:
        print(*a, **b)


def clear(): os.system('cls')


def setup_database():
    # open the csv file as a stream
    with open('res/data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        list = []
        for row in csv_reader:
            list.append(
                # Create Player objects based on rows in the csv file.
                Player(row["Player"], row["Position"], row["Games"], row["Win rate"], row["KDA"], row["CSM"],
                       row["GPM"],
                       row["KP%"], row["DMG%"]))
        # Return an object of the Database class, passing it the list of Player objects.
        return Database(list)
