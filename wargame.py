from vikingsClasses import Soldier, Viking, Saxon, War
import random
import time

# Display info
def display_round_info(round, war):
    print("\n" + "="*40)  # Visual separator for readability
    print(f"Round {round}")
    print("="*40)
    print(f"Viking Army: {len(war.vikingArmy)} warriors remaining")
    print(f"Saxon Army: {len(war.saxonArmy)} warriors remaining")
    print("="*40)

# Generate war name
def generate_war_name():
    adjectives = ["Epic", "Glorious", "Savage", "Violent", "Legendary", "Merciless", "Mighty", "Heroic"]
    nouns = ["Battle of the Plains", "Siege of the North", "Clash of Titans", "War of the Ages", "Skirmish of Honor"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

# Display all Vikings before selection
def display_all_vikings(vikings_list):
    print("\nAll available Vikings:")
    for i, viking in enumerate(vikings_list):
        print(f"{i + 1}. {viking.name} (Health: {viking.health}, Strength: {viking.strength})")

# Choose specific Vikings to go to battle
def choose_vikings(vikings_list, num_to_select):
    selected_vikings = []
    for _ in range(num_to_select):
        while True:
            try:
                choice = int(input(f"\nSelect Viking by number (1-{len(vikings_list)}): ")) - 1
                if 0 <= choice < len(vikings_list) and vikings_list[choice] not in selected_vikings:
                    selected_vikings.append(vikings_list[choice])
                    break
                else:
                    print("\nInvalid selection or Viking already chosen. Please try again.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")
    
    return selected_vikings

# Start game
def start_game():
    soldier_names = ["albert", "andres", "archie", "dani", "david", "gerard", "german", "graham", "imanol", "laura"]
    
    # Generate a random war name
    war_name = generate_war_name()
    
    # Fixed number of 7 Vikings created
    num_vikings = 7
    num_saxons = 5

    # Create an instance of War
    war = War()

    # Create 7 Vikings
    all_vikings = []
    for i in range(num_vikings):
        viking_name = random.choice(soldier_names)
        viking_health = 100
        viking_strength = random.randint(50, 100)  # Assign random strength between 50 and 100 for more variation
        viking = Viking(viking_name, viking_health, viking_strength)
        all_vikings.append(viking)

    # Create 5 random Saxons
    for i in range(num_saxons):
        saxon_health = 100
        saxon_strength = random.randint(50, 100)  # Assign random strength between 50 and 100 for more balanced battles
        war.addSaxon(Saxon(saxon_health, saxon_strength))

    # Verify armies are created
    print(f"\nWelcome to the {war_name}!")
    print(f"\nSaxons created: {len(war.saxonArmy)}")

    # Display all Vikings for player selection
    display_all_vikings(all_vikings)

    # Allow the user to choose 7 Vikings for the battle
    selected_vikings = choose_vikings(all_vikings, 5)
    
    # Add the selected Vikings to the war
    for viking in selected_vikings:
        war.addViking(viking)

    # Start war with at least one round of battle
    round_num = 0
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(f"\nStarting round {round_num + 1}!")

        # Viking attacks
        print("\nViking attack:")
        print(war.vikingAttack())
        
        # Check status after Viking attack
        if war.showStatus() != "Vikings and Saxons are still in the thick of battle.":
            break

        # Saxon attacks
        print("\nSaxon attack:")
        print(war.saxonAttack())

        # Display round info
        display_round_info(round_num, war)
        round_num += 1
        time.sleep(2)  # Wait 2 seconds between each round for better visualization
    
    # Final results
    print("\n" + war.showStatus())

# Prompt the user to press Enter to start
input("\nPress enter to start a new game ")

# Main loop to repeat games
while True:
    start_game()

    # Ensure the user enters 'Y' or 'N'
    while True:
        play_again = input("\nDo you want to play another game? (Y/N): ").strip().lower()
        if play_again in ['y', 'n']:
            break
        else:
            print("\nInvalid input! Please enter 'Y' to play again or 'N' to quit.")

    if play_again == 'n':
        print("\nThank you for playing the game!")
        break

start_game()