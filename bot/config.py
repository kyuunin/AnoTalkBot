from os.path import isfile
import json
if isfile("config.json"):
    with open("config.json") as f:
        config = json.load(f)   
else:
    print("config.json not found")
    config = {"key":input("Please enter your Telegram API key")}
    with open("config.json","w") as f:
        json.dump(config, f)
