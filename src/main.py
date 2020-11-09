import time

from client import Client
from server import Server
from game_classes import *
from const import *
import os


def clear(): os.system('cls')


if __name__ == "__main__":
    port = 56005
    server = Server(port)
    client1 = Client(port)
    client2 = Client(port)
    time.sleep(1)
    client1.send(ACTION=CLIENT_REQUEST_CONNECT)
    client2.send(ACTION=CLIENT_REQUEST_CONNECT)
    client1.send(ACTION=CLIENT_REQUEST_DATABASE)
    client2.send(ACTION=CLIENT_REQUEST_DATABASE)
    time.sleep(1)
    client1.send(ACTION=CLIENT_REQUEST_TEAM_NAME, obj="Name")
    client1.send(ACTION=CLIENT_REQUEST_EXIT)

    time.sleep(1)
    print("kek")
    # if __name__ == "__main__":
#         pickled_db = pickle.dumps(db)
#         db = pickle.loads(pickled_db)
#         teamA = Team(input("Welcome to league manager 2020 - Type your teamname: "))
#         credits = 400
#
#         while teamA.unoccupied_lanes():
#             print(f'You have {credits} credits you can use to purchase pro players.')
#             i = 1
#             for row in teamA.unoccupied_lanes():
#                 print(f' {i}) {row}')
#                 i += 1
#             selected = int(input("Type the number of the lane you want to buy players from: "))
#             clear()
#             if selected > len(teamA.unoccupied_lanes()) or selected <= 0:
#                 continue
#             listoflaners = db.get_players_from_lane(teamA.unoccupied_lanes()[selected - 1])
#
#             i = len(listoflaners)
#             for laner in listoflaners:
#                 laner.price = int(math.floor((len(listoflaners)-i)/len(listoflaners)*100))
#                 print(f'{i.__str__() + ")":<4} {laner}')
#                 i -= 1
#             selectionValid = False
#             while not selectionValid:
#                 lane = listoflaners[0].position
#                 selected = int(input("List of " + lane.lower() + " laners - Type a player number to purchase them for your team roster, type 0 to return: "))
#                 if selected != 0 & isinstance(selected, int):
#                     if credits >= listoflaners[len(listoflaners)-selected].price:
#                         teamA.add_to_roster(listoflaners[len(listoflaners) - selected])
#                         credits -= listoflaners[len(listoflaners)-selected].price
#                         selectionValid = True
#                     else:
#                         print("Not enough credits to purchase this player")
#                         continue
#                 elif selected == 0:
#                     selectionValid = True
#             clear()
#             print(teamA)
