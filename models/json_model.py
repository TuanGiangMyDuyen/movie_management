import json
import os
from os import makedirs


class JSONHandler:
    def __init__(self, filename):
        self.filepath = os.path.join("datas", filename)

        if not os.path.exists("datas"):
            makedirs("datas")

        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump([], f)

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def write_json(self, data):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)