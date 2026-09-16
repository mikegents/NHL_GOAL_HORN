import subprocess
from pathlib import Path
import nhlpy
from nhlpy import NHLClient
import time
from bluetooth import connect_speaker

client=NHLClient(
        debug=True,
        timeout=10,
        ssl_verify=True,
        follow_redirects=True,
        )

game_id = None
mtl_score = 0

def setup_todays_game():
    global game_id

    schedule = client.schedule.daily_schedule()

    for game in schedule["games"]:
        home_team = game["homeTeam"]["abbrev"]
        away_team = game["awayTeam"]["abbrev"]

        if home_team == "MTL" or away_team == "MTL":
             game_id = game["id"]

        print("Habs game found")
        print("Game ID:", game_id)

        return
    print("No Habs Game Found")


def update_game():
    global mtl_score

    boxscore = client.game_center.boxscore(game_id)

    home_team = game["homeTeam"]["abbrev"]
    away_team = game["awayTeam"]["abbrev"]

    home_score = boxscore["homeTeam"]["score"]
    away_score = boxscore["awayTeam"]["score"]

    if home_team == "MTL":
        new_mtl_score = home_score

    elif away_team == "MTL":
        new_mtl_score = away_score

    else:
        return
    print("Current Habs Score:", new_mtl_score)

    if new_mtl_score > mtl_score:
        print("SCOREEEEEEE")
        handle_goal()



#TODO maybe fix so goal_horn file is not hard coded but doesnt really matter
def play_goal_sound():
    goal_sound = Path(__file__).parent / "goal-horn-short.mp3"
    subprocess.run([ "ffplay",
                   "-autoexit",
                str(goal_sound)])


#TODO
def turn_on_light():
    pass


def handle_goal():
    play_goal_sound()
    #TODO
    #turn_on_light()


def main():
    connect_speaker()

    setup_todays_game()

    if game_id == None:
        return

    while True:
        update_game()
        time.sleep(10)

if __name__ == "__main__":
    main()
