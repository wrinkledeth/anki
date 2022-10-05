import json
from pprint import pprint
import os, shutil

## utils


def empty_folder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


### main code here

empty_folder("./All")

with open("./deck.json", "r") as json_file:
    deck = json.load(json_file)

all_decks = deck.get("children")
for folder in all_decks:
    category_name = folder.get("name")
    if category_name == "Mandarin":  # skip this category
        continue
    print(f"{category_name}")
    for deck in folder.get("children"):
        deck_name = deck.get("name")
        if deck_name == "guitar intervals":  # skip this deck
            continue
        print(f"   {deck_name}")
        notes = deck.get("notes")
        target_path = f"./All/{category_name}/{deck_name}"
        create_folder(target_path)
        with open(f"{target_path}/{deck_name}.md", "w") as md_file:
            for card in notes:
                front = card["fields"][0]
                back = card["fields"][1]
                md_file.write(f"\n\n## {front}\n\n{back}")
