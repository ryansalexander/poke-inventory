import csv
import json
import re

def update_inventory(csv_name: str):
    inventory = {}
    with open('current_inventory.json', mode='r') as json_file:
        inventory = json.load(json_file)

    csv_abbr = str(re.findall(r"\((.*?)\)", csv_name)[0])

    with open(csv_name, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            card_id = csv_abbr + ' ' + row['Cards'].split(' ')[0].lstrip('0')
            inventory[card_id] = {
                "Name": row['Cards'].split(" ", 1)[1].lstrip(),
                "Quantity": int(row["Copies Owned"])
            }

    with open('current_inventory.json', mode='w', encoding='utf-8') as json_file:
        json.dump(inventory, json_file, indent=4)

def clear_inventory():
    with open('current_inventory.json', mode='w', encoding='utf-8') as json_file:
        json.dump({}, json_file, indent=4)