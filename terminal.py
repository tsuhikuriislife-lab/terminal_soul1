import random
import os

def clearScreen():
    """Clears the terminal"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def attributeAssigner(difficulty):
    """Assigns the attributes for the Hero and Enemy in regard to the difficulty"""
    if difficulty == "easy":
        hp_hero = 110
        hero_potion = 4
        hp_enemy = 120
        remaining_hp = 120
        enemy_potion = 3
        healing = 30
        healing_enemy = 10
        enemy_max_dmg = 15
    elif difficulty == "medium":
        hp_hero = 100
        hero_potion = 3
        hp_enemy = 120
        remaining_hp = 120
        enemy_potion = 3
        healing = 20
        healing_enemy = 20
        enemy_max_dmg = 20
    elif difficulty == "hard":
        hp_hero = 100
        hero_potion = 3
        hp_enemy = 130
        remaining_hp = 130
        enemy_potion = 4
        healing = 10
        healing_enemy = 30
        enemy_max_dmg = 30
    return hp_hero, hero_potion, hp_enemy, enemy_potion, healing, healing_enemy, enemy_max_dmg, remaining_hp

def heroAction(action, life, potions, healing, remaining_hp):
    if action == 1:
        atk = random.randint(10,25)
        crit = random.randint(0,100)
        if crit >= 90:
            atk *= 2
            print(f"Critical hit! Dealt {atk} damage")
        else:
            print(f"Dealt {atk} damage!")
        remaining_hp -= atk
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
            if crit >= 90:
                atk *= 2
                print(f"Critical hit! Dealt {atk} damage")
            else:
                print(f"Dealt {atk} damage")
        else:
            print("Missed!")
            atk = 0
        remaining_hp -= atk
  
    return life, potions, remaining_hp

def winCondition(life, loop):
    if life <= 0:
        print("You win!")
        loop = 1
    return loop

def enemyAction(life, potions, hero_life, healing, enemy_dmg, remaining_hp):
    if potions > 0:
        if remaining_hp <= (life*0.2):
            remaining_hp += healing
            potions -= 1
            print(f"Healed {healing}")
    atk = random.randint(15,enemy_dmg)
    crit = random.randint(0,100)
    if crit >= 90:
        atk *= 2
        print(f"Critical hit! Dealt {atk} damage")
    else:
        print(f"Dealt {atk} damage")
    hero_life -= atk
    return potions, remaining_hp, hero_life
    
def loseCondition(life, loop):
    if life <= 0:
        print("You lose!")
        loop = 1
    return loop

def showInfo(remaining_hp, hero_life, hero_potions, enemy_potions, rounds):
    print(f"--- Your stats (Round {rounds})")
    print(f"Life: {hero_life}")
    print(f"Potions remaining: {hero_potions}")
    print("--- Enemy stats:")
    print(f"Life: {remaining_hp}")
    print(f"Potions remaning: {enemy_potions}")

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
        "1": "easy",
        "e": "easy",
        "easy": "easy",
        "2": "medium",
        "m": "medium",
        "medium": "medium",
        "3": "hard",
        "h": "hard",
        "hard": "hard",
        "4": "exit",
        "e": "exit",
        "exit": "exit"
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

clearScreen()
print("Terminal Souls")
loop_menu = 0
while loop_menu == 0:
    option_menu = input("Select an option:\n1.New game\n2.Close\n--- ")

    if option_menu in options["menu"]:
        option_menu = options["menu"][option_menu]
        if option_menu == 1:
            clearScreen()
            loop_difficulty = 0
            while loop_difficulty == 0:
                option_difficulty = input("Select a difficulty:\n1.Easy\n2.Medium\n3.Hard\n4.Exit\n--- ")
                if option_difficulty in options["difficulty"]:
                    difficulty = options["difficulty"][option_difficulty]
                    if difficulty == "exit":
                        loop_difficulty = 1
                        continue
                    else:
                        print(f"Difficulty selected: {difficulty.capitalize()}")
                        hp_hero, hero_potion, hp_enemy, enemy_potion, healing, healing_enemy, enemy_max_dmg, remaining_hp = attributeAssigner(difficulty)
                        loop_principal = 0
                        rounds = 1
                        input("Press Enter to continue...")
                        while loop_principal == 0:
                            clearScreen()
                            showInfo(remaining_hp, hp_hero, hero_potion, enemy_potion, rounds)
                            input("Press Enter to continue...")
                            clearScreen()
                            print("--- Your turn...")
                            loop_action = 0
                            while loop_action == 0:
                                action = input("Select your action:\n1.Attack\n2.Heal\n3.Skill\n--- ")
                                if action in options["actions"]:
                                    action = options["actions"][action]
                                    hp_hero, hero_potion, remaining_hp = heroAction(action, hp_hero, hero_potion, healing, remaining_hp)
                                    loop_action = 1
                                else:
                                    print("Select a valid action...")
                            loop_principal = winCondition(remaining_hp, loop_principal)
                            if loop_principal == 1:
                                continue
                            input("Press Enter to continue...")
                            clearScreen()
                            print("--- Enemy turn...")
                            enemy_potion, remaining_hp, hp_hero = enemyAction(hp_enemy, enemy_potion, hp_hero, healing_enemy, enemy_max_dmg, remaining_hp)
                            loop_principal = loseCondition(hp_hero, loop_principal)
                            input("Press Enter to continue...")
                            rounds += 1
                else:
                    print("Select a valid option...")
        elif option_menu == 2:
            print("Closing...")
            loop_menu = 1    
    else:
        print("Select a valid option...")
