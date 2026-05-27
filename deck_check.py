import json
import re

def process_decklist(decklist: str):
    card_list = decklist.split('\n')
    card_list = [card for card in card_list if card] #remove empties
    decklist_map = {}
    for card in card_list:
        decklist_map[str(re.findall(r"\((.*?)\)", card)[0])] = int(card.split(' ')[0])

    return decklist_map

def check_deck(decklist: str):
    decklist_map = process_decklist(decklist)
    missing_cards = {}

    inventory = {}
    with open('current_inventory.json', mode='r') as json_file:
        inventory = json.load(json_file)

    for id, quantity in decklist_map.items():
        inventory_quantity = inventory[id]['Quantity']
        if inventory_quantity < quantity:
            missing_cards.append('' + str(quantity - inventory_quantity) + ' ' + inventory[id]['Name'] + '(' + id + ')')
    for card in missing_cards:
        print(card)