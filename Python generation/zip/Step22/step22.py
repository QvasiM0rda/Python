import json
from zipfile import ZipFile


def is_correct_json(string: str) -> bool:
    try:
        json.loads(string)
        return True
    except:
        return False


with ZipFile("data.zip") as zip_file:
    files = zip_file.infolist()
    players = list()
    
    for file in files:
        with zip_file.open(file.filename) as json_file:
            try:
                json_file = json_file.read().decode("utf-8")
            except:
                continue
            if is_correct_json(json_file):
                players.append(json.loads(json_file))

players = sorted(players, key=lambda p: (p["first_name"], p["last_name"]))
for player in players:
    if player["team"] == "Arsenal":
        print(player["first_name"], player["last_name"])
