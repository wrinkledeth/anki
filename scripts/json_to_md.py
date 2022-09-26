import json
from pprint import pprint

with open("./deck.json", "r") as json_file:
    deck = json.load(json_file)

deck_name = deck.get("name")
notes = deck.get("notes")

with open("./deck.md", "w") as md_file:
    md_file.write(f"# {deck_name}")
    for card in notes:
        # print(card)
        front = card["fields"][0]
        back = card["fields"][1]
        md_file.write(f"\n\n## {front}\n\n{back}")
