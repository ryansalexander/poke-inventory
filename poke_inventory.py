import Settings.COMMANDS as COMMANDS
from Settings.STATE import State
import deck_check
import manage_inventory

def listen_for_input():
    print("Type 'quit' to terminate poke-inventory")
    state = State.NEUTRAL
    current_deck = ""
    while True:
        #print(state)
        unedited_user_data = input("> ")
        user_data = unedited_user_data

        if user_data == COMMANDS.QUIT:
            print("Goodbye!")
            break

        match state:
            case State.NEUTRAL:
                if user_data == COMMANDS.CLEAR_INVENTORY:
                    state = State.CLEARING
                    print("Are you sure you want to clear your inventory?")
                elif user_data == COMMANDS.UPDATE_INVENTORY:
                    state = State.UPDATING
                    print("Please provide a file path to update your inventory or type 'quit' to stop updating.")
                elif user_data == COMMANDS.UPDATE_INVENTORY:
                    state = State.UPDATING
                    print("Please provide a file path to update your inventory or type 'quit' to stop updating.")
                elif user_data == COMMANDS.DECK_CHECK:
                    state = State.DECK_CHECK
                    print("Please submit a decklist.")
                else:
                    print("Unknown command. Type 'quit' to terminate poke-inventory.")
            case State.CLEARING:
                if user_data == COMMANDS.YES:
                    manage_inventory.clear_inventory()
                    print("Inventory cleared.")
                elif user_data == COMMANDS.NO:
                    print("Okay, your inventory is unchanged.")
                state = State.NEUTRAL
            case State.UPDATING:
                try:
                    manage_inventory.update_inventory(unedited_user_data)
                except:
                    print("Invalid file path")
                print("Please provide an additional file path to update your inventory or type 'quit' to stop updating.")
            case State.DECK_CHECK:
                if user_data != COMMANDS.SUBMIT:
                    current_deck += user_data + '\n'
                if user_data == COMMANDS.SUBMIT:
                    deck_check.check_deck(current_deck)
            
        #print(user_data)

if __name__ == "__main__":
    listen_for_input()