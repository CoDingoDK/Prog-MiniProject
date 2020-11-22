import random

red_kills = 0
red_towers = 4
red_nexus_alive = True
red_tower_health = 1500
red_top = 100
red_jungle = 100
red_mid = 100
red_bot = 100
red_support = 100

blue_kills = 0
blue_towers = 4
blue_nexus_alive = True
blue_tower_health = 1500
blue_top = 100
blue_jungle = 100
blue_mid = 100
blue_bot = 100
blue_support = 100

minutes = 0

combat_log = []


def start_match(blue_team, red_team):
    global red_kills, red_towers, red_nexus_alive, red_tower_health, red_top, red_jungle, red_mid, red_bot, red_support
    red_top, red_mid, red_jungle, red_bot, red_support = red_team.get_player_power_from_lanes("TOP", "MID", "JUNGLE",
                                                                                              "ADC", "SUPPORT")

    global blue_kills, blue_towers, blue_nexus_alive, blue_tower_health, blue_top, blue_jungle, blue_mid, blue_bot, blue_support
    blue_top, blue_mid, blue_jungle, blue_bot, blue_support = blue_team.get_player_power_from_lanes("TOP", "MID",
                                                                                                    "JUNGLE", "ADC",
                                                                                                    "SUPPORT")

    global minutes, combat_log

    while check_win_else_powerup():
        red_jungle_event = random.randint(0, 9)
        red_gank = 0

        blue_jungle_event = random.randint(0, 9)
        blue_gank = 0

        top_event = random.randint(0, 9)
        mid_event = random.randint(0, 9)
        bot_event = random.randint(0, 9)

        team_fight = random.randint(0, 4)

        if red_jungle_event > 4:
            red_gank = random.randint(1, 3)

        if blue_jungle_event > 4:
            blue_gank = random.randint(1, 3)

        if minutes > 15:
            if team_fight == 4:
                fight_number = random.randint(0, (blue_top + blue_jungle + blue_mid + blue_bot + blue_support + red_top + red_jungle + red_mid + red_bot + red_support))
                if fight_number > (red_top + red_jungle + red_mid + red_bot + red_support):
                    combat_log.append("Blue team won a teamfight")
                    blue_top += 30
                    blue_jungle += 30
                    blue_mid += 30
                    blue_bot += 30
                    blue_support += 30
                    red_tower_health -= (blue_top + blue_jungle + blue_mid + blue_bot + blue_support)
                    blue_kills += 5
                else:
                    combat_log.append("Red team won a teamfight")
                    red_top += 30
                    red_jungle += 30
                    red_mid += 30
                    red_bot += 30
                    red_support += 30
                    blue_tower_health -= (red_top + red_jungle + red_mid + red_bot + red_support)
                    red_kills += 5

        if top_event > 6:
            if blue_gank == 1 and red_gank != 1:
                fight_number = random.randint(0, (blue_top + blue_jungle + red_top))
                if fight_number > red_top:
                    combat_log.append("Blue side jungler ganked top and got a kill.")
                    blue_top += 15
                    blue_jungle += 15
                    red_tower_health -= blue_top + blue_jungle
                    blue_kills += 1
                else:
                    combat_log.append("Blue side jungler ganked top, but did not get a kill.")
            elif blue_gank != 1 and red_gank == 1:
                fight_number = random.randint(0, (blue_top + red_jungle + red_top))
                if fight_number > blue_top:
                    combat_log.append("Red side jungler ganked top and got a kill.")
                    red_top += 15
                    red_jungle += 15
                    blue_tower_health -= red_top + red_jungle
                    red_kills += 1
                else:
                    combat_log.append("Red side jungler ganked top, but did not get a kill.")
            elif blue_gank == 1 and red_gank == 1:
                fight_number = random.randint(0, (blue_top + blue_jungle + red_jungle + red_top))
                if fight_number > (red_top + red_jungle):
                    blue_top += 15
                    blue_jungle += 15
                    red_tower_health -= blue_top + blue_jungle
                    combat_log.append("Both junglers ganked top, but blue side got the kill.")
                    blue_kills += 1
                else:
                    red_top += 15
                    red_jungle += 15
                    blue_tower_health -= red_top + red_jungle
                    combat_log.append("Both junglers ganked top, but red side got the kill.")
                    red_kills += 1
            else:
                fight_number = random.randint(0, (blue_top + red_top))
                if fight_number > red_top:
                    blue_top += 15
                    red_tower_health -= blue_top
                    combat_log.append("Blue side top got a kill.")
                    blue_kills += 1
                else:
                    red_top += 15
                    blue_tower_health -= red_top
                    combat_log.append("Red side top got a kill.")
                    red_kills += 1

        if mid_event > 6:
            if blue_gank == 2 and red_gank != 2:
                fight_number = random.randint(0, (blue_mid + blue_jungle + red_mid))
                if fight_number > red_mid:
                    combat_log.append("Blue side jungler ganked mid and got a kill.")
                    blue_mid += 15
                    blue_jungle += 15
                    red_tower_health -= blue_mid + blue_jungle
                    blue_kills += 1
                else:
                    combat_log.append("Blue side jungler ganked mid, but did not get a kill.")
            elif blue_gank != 2 and red_gank == 2:
                fight_number = random.randint(0, (blue_mid + red_jungle + red_mid))
                if fight_number > blue_mid:
                    combat_log.append("Red side jungler ganked mid and got a kill.")
                    red_mid += 15
                    red_jungle += 15
                    blue_tower_health -= red_mid + red_jungle
                    red_kills += 1
                else:
                    combat_log.append("Red side jungler ganked mid, but did not get a kill.")
            elif blue_gank == 2 and red_gank == 2:
                fight_number = random.randint(0, (blue_mid + blue_jungle + red_jungle + red_mid))
                if fight_number > (red_mid + red_jungle):
                    blue_mid += 15
                    blue_jungle += 15
                    red_tower_health -= blue_mid + blue_jungle
                    combat_log.append("Both junglers ganked mid, but blue side got the kill.")
                    blue_kills += 1
                else:
                    red_mid += 15
                    red_jungle += 15
                    blue_tower_health -= red_mid + red_jungle
                    combat_log.append("Both junglers ganked mid, but red side got the kill.")
                    red_kills += 1
            else:
                fight_number = random.randint(0, (blue_mid + red_mid))
                if fight_number > red_mid:
                    blue_mid += 15
                    red_tower_health -= blue_mid
                    combat_log.append("Blue side mid got a kill.")
                    blue_kills += 1
                else:
                    red_mid += 15
                    blue_tower_health -= red_mid
                    combat_log.append("Red side mid got a kill.")
                    red_kills += 1

        if bot_event > 6:
            if blue_gank == 3 and red_gank != 3:
                fight_number = random.randint(0, (blue_bot + blue_support + blue_jungle + red_bot + red_support))
                if fight_number > (red_bot + red_support):
                    combat_log.append("Blue side jungler ganked bot and got a kill.")
                    blue_bot += 15
                    blue_support += 15
                    blue_jungle += 15
                    red_tower_health -= (blue_bot + blue_support + blue_jungle)
                    blue_kills += 1
                else:
                    combat_log.append("Blue side jungler ganked bot, but did not get a kill.")
            elif blue_gank != 3 and red_gank == 3:
                fight_number = random.randint(0, (blue_bot + blue_support + red_jungle + red_bot + red_support))
                if fight_number > (blue_bot + blue_support):
                    combat_log.append("Red side jungler ganked bot and got a kill.")
                    red_bot += 15
                    red_support += 15
                    red_jungle += 15
                    blue_tower_health -= (red_bot + red_support + red_jungle)
                    red_kills += 1
                else:
                    combat_log.append("Red side jungler ganked bot, but did not get a kill.")
            elif blue_gank == 3 and red_gank == 3:
                fight_number = random.randint(0, (blue_bot + blue_support + blue_jungle + red_jungle + red_bot + red_support))
                if fight_number > (red_bot + red_support + red_jungle):
                    blue_bot += 15
                    blue_support += 15
                    blue_jungle += 15
                    red_tower_health -= (blue_bot + blue_support + blue_jungle)
                    combat_log.append("Both junglers ganked bot, but blue side got the kill.")
                    blue_kills += 1
                else:
                    red_bot += 15
                    red_support += 15
                    red_jungle += 15
                    blue_tower_health -= (red_bot + red_support + red_jungle)
                    combat_log.append("Both junglers ganked bot, but red side got the kill.")
                    red_kills += 1
            else:
                fight_number = random.randint(0, (blue_bot + blue_support + red_bot + red_support))
                if fight_number > (red_bot + red_support):
                    blue_bot += 15
                    blue_support += 15
                    red_tower_health -= (blue_bot + blue_support)
                    combat_log.append("Blue side bot got a kill.")
                    blue_kills += 1
                else:
                    red_bot += 15
                    red_support += 15
                    blue_tower_health -= (red_bot + red_support)
                    combat_log.append("Red side bot got a kill.")
                    red_kills += 1
    if not red_nexus_alive:
        combat_log.append("Blue team has won the game!")
    elif not blue_nexus_alive:
        combat_log.append("Red team has won the game!")

    combat_log.append("Blue team had a total of " + str(blue_kills) + " kills" + " and red team had a total of " +
                      str(red_kills) + " kills")
    return combat_log

def check_win_else_powerup():
    global red_kills, red_towers, red_nexus_alive, red_tower_health, red_top, red_jungle, red_mid, red_bot, red_support

    global blue_kills, blue_towers, blue_nexus_alive, blue_tower_health, blue_top, blue_jungle, blue_mid, blue_bot, blue_support

    global minutes, combat_log

    combat_log.append(" ")
    minutes += 1
    combat_log.append("Minute " + str(minutes))

    if red_towers == 0:
        if red_tower_health < 0 and red_tower_health < blue_tower_health:
            red_nexus_alive = False
            combat_log.append("Blue team has destroyed the enemy nexus!")
            return False
    if blue_towers == 0:
        if blue_tower_health < 0 and blue_tower_health < red_tower_health:
            blue_nexus_alive = False
            combat_log.append("Red team has destroyed the enemy nexus!")
            return False
    if red_nexus_alive and blue_nexus_alive:

        if red_towers > 0:
            if red_tower_health < 0:
                red_towers -= 1
                red_tower_health = 1500
                combat_log.append("Blue team has destroyed a turret!")
        if blue_towers > 0:
            if blue_tower_health < 0:
                blue_towers -= 1
                blue_tower_health = 1500
                combat_log.append("Red team has destroyed a turret!")
        red_top += 5
        red_jungle += 5
        red_mid += 5
        red_bot += 5
        red_support += 5
        blue_top += 5
        blue_jungle += 5
        blue_mid += 5
        blue_bot += 5
        blue_support += 5

        return True
