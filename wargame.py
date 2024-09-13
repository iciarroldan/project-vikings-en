from vikingsClasses import Soldier, Viking, Saxon, War
import random
import time
import pygame

# Display round information
def display_round_info(round, war):
    print("\n" + "="*40)  
    print(f"End of round {round}")
    print("="*40)
    print(f"Viking Army: {len(war.vikingArmy)} warriors remaining")
    print(f"Saxon Army: {len(war.saxonArmy)} warriors remaining")
    print("="*40)

# Generate a random war name
def generate_war_name():
    adjectives = ["Epic", "Glorious", "Savage", "Violent", "Legendary", "Merciless", "Mighty", "Heroic"]
    nouns = ["Battle of the Plains", "Siege of the North", "Clash of Titans", "War of the Ages", "Skirmish of Honor"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

# Initialize pygame
pygame.init()

# Load sound files for random events
try:
    lightening_sound = pygame.mixer.Sound("sounds/thunder.mp3")
    earthquake_sound = pygame.mixer.Sound("sounds/earthquake.mp3")
    acid_rain_sound = pygame.mixer.Sound("sounds/rain.mp3")
    tornado_sound = pygame.mixer.Sound("sounds/tornado.mp3")
    print("Sounds loaded successfully.")
except pygame.error as e:
    print(f"Error loading sound files: {e}")

# Stop all event sounds
def stop_event_sounds():
    lightening_sound.stop()
    earthquake_sound.stop()
    acid_rain_sound.stop()
    tornado_sound.stop()

# Play sound for the selected random event
def play_event_sound(event):
    stop_event_sounds()
    if event == "A lightning strike hits the battlefield.":
        lightening_sound.play(loops=-1)
    elif event == "An earthquake shakes the battlefield.":
        earthquake_sound.play(loops=-1)
    elif event == "Acid rain is pouring into the battlefield.":
        acid_rain_sound.play(loops=-1)
    elif event == "A tornado appears out of nowhere.":
        tornado_sound.play(loops=-1)

# Global variable to track game over state
game_over = False

# Generate random events for each round
def random_event(war):
    global game_over  # Use global variable to end the game
    # 50% chance for a random event
    if random.random() < 0.5:  
        events = [
            "A lightning strike hits the battlefield.",
            "An earthquake shakes the battlefield.",
            "A tornado appears out of nowhere.",
            "Gods have sent healing clouds to the battlefield.",
            "The sun is shining, boosting soldiers' vitamin D."
        ]

        # 10% chance for "Acid rain"
        if random.random() < 0.1:  
            event = "Acid rain is pouring into the battlefield."
        else:
            event = random.choice(events)

        print(f"\nRandom event: {event}")

        # Play the appropriate sound
        play_event_sound(event)

        # Lightning strike
        if event == "A lightning strike hits the battlefield.":
            if random.choice([True, False]):
                if war.vikingArmy:
                    victim = random.choice(war.vikingArmy)
                    victim.health = 0
                    print(f"\n{victim.name} has been struck by lightning, the Vikings lose one soldier.")
            else:
                if war.saxonArmy:
                    victim = random.choice(war.saxonArmy)
                    victim.health = 0
                    print(f"\nA Saxon has been struck by lightning, the Saxons lose one soldier.")
        
        # Earthquake event
        elif event == "An earthquake shakes the battlefield.":
            for viking in war.vikingArmy:
                viking.health -= 10
            for saxon in war.saxonArmy:
                saxon.health -= 10
            time.sleep(1)
            print("\nThe earthquake weakened all soldiers, reducing their health by 10 points.")

        # Acid rain event
        elif event == "Acid rain is pouring into the battlefield.":
            for viking in war.vikingArmy:
                viking.health = 0
            for saxon in war.saxonArmy:
                saxon.health = 0
            print("\nAcid rain has destroyed both armies!")
            game_over = True  # End the game immediately

        # Tornado event
        elif event == "A tornado appears out of nowhere.":
            if random.choice([True, False]):
                if len(war.vikingArmy) >= 3:
                    victims = random.sample(war.vikingArmy, 3)
                    victims[0].health -= 20
                    victims[1].health -= 10
                    victims[2].health -= 30
                    print(f"\n{victims[0].name}, {victims[1].name}, and {victims[2].name} were caught in a tornado! "
                          f"{victims[0].name} loses 20 health points, {victims[1].name} loses 10 health points, "
                          f"and {victims[2].name} loses 30 health points.")
            else:
                if len(war.saxonArmy) >= 3:
                    victims = random.sample(war.saxonArmy, 3)
                    victims[0].health -= 20
                    victims[1].health -= 10
                    victims[2].health -= 30
                    print(f"\nThree Saxons were caught in a tornado! One loses 20 health points, another loses 10, "
                          "and the third loses 30.")

        # Gods sending healing clouds
        elif event == "Gods have sent healing clouds to the battlefield.":
            if random.choice([True, False]):
                for viking in war.vikingArmy:
                    viking.health += 10
                print("\nThe Vikings have been blessed by the gods, healing 10 health points!")
            else:
                for saxon in war.saxonArmy:
                    saxon.health += 10
                print("\nThe Saxons have been blessed by the gods, healing 10 health points!")

        # Sun boosting health
        elif event == "The sun is shining, boosting soldiers' vitamin D.":
            for viking in war.vikingArmy:
                viking.health = 100
            for saxon in war.saxonArmy:
                saxon.health = 100
            print("\nThe sun has revitalized both armies, restoring their health to 100!")
    
    # No event this round
    else:
        print("\nNo event this round.")

# Display all soldiers for selection
def display_all_soldiers(soldiers_list, army_name):
    print(f"\nAll available {army_name}:")
    for i, soldier in enumerate(soldiers_list):
        print(f"{i + 1}. {soldier.name} (Health: {soldier.health}, Strength: {soldier.strength}) , (Weapon: {soldier.weapon}, Damage: {soldier.weapon_damage})")

# Function to generate a description for the selected soldier
def get_soldier_description(soldier):
    descriptions = {
        "eine": "Eine, the swift and fearless, is known for her unparalleled speed on the battlefield.",
        "thor": "Thor, the god of thunder, wields his mighty hammer, ready to crush his enemies.",
        "gerard": "Gerard, the wise, a master strategist who can turn the tide of any battle.",
        "loki": "Loki, the trickster, always has a plan up his sleeve to outsmart his enemies.",
        "maria": "Maria, the shieldmaiden, stands firm in the face of danger, protecting her allies.",
        "eric": "Eric, the berserker, enters a frenzied rage in battle, striking fear into the hearts of foes.",
        "iker": "Iker, the silent blade, is known for his stealth and precision with his attacks.",
        "dani": "Dani, the healer, uses her wisdom to heal wounds and inspire her comrades.",
        "david": "David, the giant slayer, once defeated an enormous beast, earning legendary status.",
        "albert": "Albert, the stoic defender, is a Saxon warrior known for his unbreakable defense.",
        "andres": "Andres, the relentless, never backs down from a fight and always seeks revenge.",
        "archie": "Archie, the archer, can strike his enemies from great distances with pinpoint accuracy.",
        "german": "German, the strong, is the brute force of the Saxon army, unstoppable in hand-to-hand combat.",
        "graham": "Graham, the strategist, is known for outmaneuvering opponents with his tactical mind.",
        "imanol": "Imanol, the iron-willed, never succumbs to fear or pain in battle.",
        "laura": "Laura, the swift blade, uses her agility to outpace and outfight her enemies.",
        "arthur": "Arthur, the legendary, wields a sword said to be blessed by ancient gods."
    }
    # Return the description if available, or a generic message if not.
    return descriptions.get(soldier.name, f"{soldier.name} is a brave warrior ready to fight for glory.")

# Choose soldiers for battle
def choose_soldiers(soldiers_list, num_to_select, army_name):
    selected_soldiers = []
    for _ in range(num_to_select):
        while True:
            try:
                choice = int(input(f"\nSelect {army_name} by number (1-{len(soldiers_list)}): ")) - 1
                if 0 <= choice < len(soldiers_list) and soldiers_list[choice] not in selected_soldiers:
                    selected_soldiers.append(soldiers_list[choice])
                    
                    # Get and display the soldier's description or story
                    description = get_soldier_description(soldiers_list[choice])
                    print(f"\n{description}")
                    break
                else:
                    print(f"\nInvalid selection or {army_name} already chosen. Please try again.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")
    return selected_soldiers

# Start the game
def start_game():
    global game_over
    game_over = False  # Reset game_over at the beginning of each game
    viking_names = ["eine", "thor", "gerard", "loki",  "maria", "eric", "iker", "dani", "david"]
    saxon_names = ["albert", "andres", "archie",  "german", "graham", "imanol", "laura", "arthur"]
    
    # Generate a random war name
    war_name = generate_war_name()
    
    # Fixed number of soldiers in each army
    num_vikings = 5
    num_saxons = 5

    # Create the war instance
    war = War()

    # Create Vikings
    all_vikings = []
    for i in range(num_vikings):
        viking_name = random.choice(viking_names)
        viking_health = random.randint(90, 150)
        viking_strength = random.randint(25, 55)
        viking = Viking(viking_name, viking_health, viking_strength)
        all_vikings.append(viking)

    # Create Saxons
    all_saxons = []
    for i in range(num_saxons):
        saxon_name = random.choice(saxon_names)
        saxon_health = random.randint(90, 150)
        saxon_strength = random.randint(25, 55)
        saxon = Saxon(saxon_name, saxon_health, saxon_strength)
        all_saxons.append(saxon)

    # Show the armies
    print(f"\nWelcome to the {war_name}!")

    # Display Vikings and Saxons for player selection
    display_all_soldiers(all_vikings, "Vikings")
    display_all_soldiers(all_saxons, "Saxons")

    # Select 3 Vikings and 3 Saxons for battle
    selected_vikings = choose_soldiers(all_vikings, 3, "Vikings")
    selected_saxons = choose_soldiers(all_saxons, 3, "Saxons")
    
    # Add the selected soldiers to the war
    for viking in selected_vikings:
        war.addViking(viking)
    for saxon in selected_saxons:
        war.addSaxon(saxon)

    # Start the battle
    round_num = 1
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle." and not game_over:
        print("\n" + "="*40)
        print(f"\nStarting round {round_num}!")

        # Trigger a random event
        random_event(war)

        # Check if acid rain ended the game
        if game_over:
            print("\nThe game ends due to acid rain killing all soldiers!")
            break

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
        input("\nPress enter to start the next round ")
    
    # Final result
    if not game_over:
        print("\n" + war.showStatus())

# Start the game
input("\nPress enter to start a new game ")

# Main game loop
while True:
    start_game()

    # Ask if the user wants to play again
    while True:
        play_again = input("\nDo you want to play another game? (Y/N): ").strip().lower()
        if play_again in ['y', 'n']:
            break
        else:
            print("\nInvalid input! Please enter 'Y' to play again or 'N' to quit.")

    if play_again == 'n':
        print("\nThank you for playing the game!")
        break