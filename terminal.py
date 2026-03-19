mport random

def attributeAssigner(difficulty):
    if difficulty == 1:
        hp_hero = 110
        hero_potion = 4
        hp_enemy = 120
        enemy_potion = 3
        healing = 30
    elif difficulty == 2:
        hp_hero = 100
        hero_potion = 3
        hp_enemy = 120
        enemy_potion = 3
        healing = 20
    elif difficulty == 3:
        hp_hero = 100
        hero_potion = 3
        hp_enemy = 130
        enemy_potion = 4
        healing = 10
    return hp_hero, hero_potion, hp_enemy, enemy_potion, healing

def heroAction(action, life, potions, enemy_hp, healing):
    if action == 1:
        atk = random.randint(10,25)
        crit = random.randint(0,100)
        if crit > 90:
            atk *= 2
            print(f"Critical hit! Dealt {atk} dmg")
        else:
            print(f"Dealt {atk} dmg!")
        enemy_hp -= atk
    elif action == 2:
        if potions > 0:
            life += healing
            potions -= 1
            print(f"Healed {healing} HP")
            print(f"{potions} potions remaining...")
        else:
            print("You don't have any more potions")
    elif action == 3:
        probability = random.randint(0,1)
        if probability > 0:
            atk = random.randint(30,50)
            crit = random.randint(0,100)
            if crit > 90:
                atk *= 2
                print(f"Critical hit! Dealt {atk} dmg")
            else:
                print(f"Dealt {atk} dmg")
        else:
            print("Missed!")
        enemy_hp -= atk
  
    return life, potions, enemy_hp


options = {
    "menu":{
        "1": 1,
        "n": 1,
        "new": 1,
        "game": 1,
        "new game": 1,
        "2": 2,
        "c": 2,
        "close": 2
    },
    "difficulty":{
        "1": 1,
        "e": 1,
        "easy": 1,
        "2": 2,
        "m": 2,
        "medium": 2,
        "3": 3,
        "h": 3,
        "hard": 3
    },
    "actions":{
        "1": 1,
        "a": 1,
        "attack": 1,
        "2": 2,
        "h": 2,
        "heal": 2,
        "3": 3,
        "s": 3,
        "skill": 3
    }
}

print("Terminal Souls")

option_menu = input("Select an option:\n1.New game\n2.Close\n--- ")

if option_menu in options["menu"]:
    option_menu = options["menu"][option_menu]
    if option_menu == 1:
        option_difficulty = input("Select a difficulty:\n1.Easy\n2.Medium\n3.Hard\n--- ")
        if option_difficulty in options["difficulty"]:
            option_difficulty = options["difficulty"][option_difficulty]
            loop_principal = 0
            while loop_principal == 0:
                hp_hero, hero_potion, hp_enemy, enemy_potion = attributeAssigner(option_difficulty)
                loop_action = 0
                while loop_action == 0:
                    action = input("Select your action:\n1.Attack\n2.Heal\n3.Skill\n--- ")
                    if action in options["actions"]:
                        action = options["actions"][action]
                        loop_action = 1
                    else:
                        print("Select a valid action...")
                
                        
                


