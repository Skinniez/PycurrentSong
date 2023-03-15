import json
import os

class Config:
    def __init__(self):
        self.save_path = "./data"

    def load_config(self):
        os.makedirs("./data", exist_ok=True)

        try:
            with open("./data/config.json", "r") as file:
                configuration = json.load(file)
                self.save_path = configuration["savePath"]
        except FileNotFoundError:
            pass

    def save(self):
        with open("./data/config.json", "w") as file:
            json.dump({"savePath": self.save_path}, file)


config = Config()
