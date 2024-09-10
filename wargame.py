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

# Generate random events for each round
def random_event(war):
    events = [
        "A lightning strike hits the battlefield.",
        "An earthquake shakes the battlefield.",
        "Acid rain is pouring into the battlefield.",
        "A tornado appears out of nowhere.",
        "Gods have sent healing clouds to the battlefield.",
        "The sun is shining, boosting soldiers' vitamin D."
    ]
    event = random.choice(events)
    print(f"\nRandom event: {event}")

    # A lightning strike hits the battlefield
    if event == "A lightning strike hits the battlefield.":
        # Random effect on 1 soldier
        if random.choice([True, False]):
            # Viking struck
            if war.vikingArmy:
                victim = random.choice(war.vikingArmy)
                victim.health = 0
                print(f"\n{victim.name} has been struck by the lightning, Vikings are one soldier down.")
        else:
            # Saxon struck
            if war.saxonArmy:
                victim = random.choice(war.saxonArmy)
                victim.health = 0
                print(f"\nA Saxon has been struck by the lightning, Saxons are one soldier down.")
    
    # An earthquake shakes the battlefield
    elif event == "An earthquake shakes the battlefield.":
        for viking in war.vikingArmy:
            viking.health -= 10
        for saxon in war.saxonArmy:
            saxon.health -= 10
        time.sleep(1)
        print("\nThe earthquake has weakened the soldiers, causing them to lose 10 health points.")

    # Acid rain pours into the battlefield
    elif event == "Acid rain is pouring into the battlefield.":
        for viking in war.vikingArmy:
            viking.health = 0
        for saxon in war.saxonArmy:
            saxon.health = 0
        print("\nAcid rain has destroyed both armies!")

    # A tornado appears out of nowhere
    elif event == "A tornado appears out of nowhere.":
        # Random effect on 3 soldiers
        if random.choice([True, False]):
            # Vikings trapped
            if len(war.vikingArmy) >= 3:
                victims = random.sample(war.vikingArmy, 3)
                victims[0].health -= 20
                victims[1].health -= 10
                victims[2].health -= 30
                print(f"\n{victims[0].name}, {victims[1].name}, and {victims[2].name} were caught in a tornado! "
                      f"{victims[0].name} loses 20 health points, {victims[1].name} loses 10 health points, "
                      f"and {victims[2].name} loses 30 health points.")
        else:
            # Saxons trapped
            if len(war.saxonArmy) >= 3:
                victims = random.sample(war.saxonArmy, 3)
                victims[0].health -= 20
                victims[1].health -= 10
                victims[2].health -= 30
                print(f"\nThree Saxons were caught in a tornado! One loses 20 health points, another loses 10, "
                      "and the third loses 30.")

    # Gods have sent healing clouds to the battlefield
    elif event == "Gods have sent healing clouds to the battlefield.":
        # Random healing effect
        if random.choice([True, False]):
            # Vikings blessed
            for viking in war.vikingArmy:
                viking.health += 10
            print("\nThe Vikings have been blessed by the gods, healing 10 health points!")
        else:
            # Saxons blessed
            for saxon in war.saxonArmy:
                saxon.health += 10
            print("\nThe Saxons have been blessed by the gods, healing 10 health points!")

    # The sun is shining, boosting soldiers' vitamin D
    elif event == "The sun is shining, boosting soldiers' vitamin D.":
        for viking in war.vikingArmy:
            viking.health = 100
        for saxon in war.saxonArmy:
            saxon.health = 100
        print("\nThe sun has revitalized both armies, restoring their health to 100!")

# Display soldiers before selection
def display_all_soldiers(soldiers_list, army_name):
    print(f"\nAll available {army_name}:")
    for i, soldier in enumerate(soldiers_list):
        print(f"{i + 1}. {soldier.name} (Health: {soldier.health}, Strength: {soldier.strength})")

# Choose specific Soldiers for battle
def choose_soldiers(soldiers_list, num_to_select, army_name):
    selected_soldiers = []
    for _ in range(num_to_select):
        while True:
            try:
                choice = int(input(f"\nSelect {army_name} by number (1-{len(soldiers_list)}): ")) - 1
                if 0 <= choice < len(soldiers_list) and soldiers_list[choice] not in selected_soldiers:
                    selected_soldiers.append(soldiers_list[choice])
                    break
                else:
                    print(f"\nInvalid selection or {army_name} already chosen. Please try again.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")
    return selected_soldiers

# Start game
def start_game():
    viking_names = ["eine", "thor", "gerard", "loki",  "maria", "eric", "iker", "dani", "david",]
    saxon_names = ["albert", "andres", "archie",  "german", "graham", "imanol", "laura", "arthur"]
    
    # Generate a random war name
    war_name = generate_war_name()
    
    # Fixed number 
    num_vikings = 5
    num_saxons = 5

    # Create an instance of War
    war = War()

    # Create Vikings
    all_vikings = []
    for i in range(num_vikings):
        viking_name = random.choice(viking_names)
        viking_health = 100
        viking_strength = random.randint(50, 100)  # Assign random strength between 50 and 100 for more variation
        viking = Viking(viking_name, viking_health, viking_strength)
        all_vikings.append(viking)

    # Create Saxons
    all_saxons = []
    for i in range(num_saxons):
        saxon_name = random.choice(saxon_names)
        saxon_health = 100
        saxon_strength = random.randint(50, 100)  # Assign random strength between 50 and 100 for more balanced battles
        saxon = Saxon(saxon_name, saxon_health, saxon_strength)
        all_saxons.append(saxon)

    # Verify armies are created
    print(f"\nWelcome to the {war_name}!")

    # Display all Vikings for player selection
    display_all_soldiers(all_vikings, "Vikings")

    # Display all Saxons for player selection
    display_all_soldiers(all_saxons, "Saxons")

    # Allow the user to choose soldiers for the battle
    selected_vikings = choose_soldiers(all_vikings, 3, "Vikings")
    selected_saxons = choose_soldiers(all_saxons, 3, "Saxons")
    
    # Add the selected Soldiers to the war
    for viking in selected_vikings:
        war.addViking(viking)
    for saxon in selected_saxons:
        war.addSaxon(saxon)

    # Start war with at least one round of battle
    round_num = 0
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(f"\nStarting round {round_num + 1}!")

        # Random event for each round
        random_event(war)

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
