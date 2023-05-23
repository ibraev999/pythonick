import random
import time

# It's end of March 2023
# The final of
# open it: python rpg_game.py

# starting statistics
HP = 20
strange = 2
speed = 0.8
lvl = 1
exp = 0
defense = 0

# HP
zombie_HP = 10  # 0
skeleton_HP = 15  # 1
snake_HP = 30  # 2
bear_HP = 25  # 3

# speed
zombie_speed = 0.5  # 0
skeleton_speed = 1.5  # 1
snake_speed = 2  # 2
bear_speed = 4  # 3

# strange
zombie_strange = 0.8  # 0
skeleton_strange = 1  # 1
snake_strange = 3  # 2
bear_strange = 8  # 3

# items
healing_potion_effect = "+25% speed and HP"  # 4
time_healing_potion = 8
poison_flask_effect = "-25% speed and HP"  # 5
time_poison_flask = 8
wooden_sword_effect = "strange + 1"  # 6
time_wooden_sword = 0
iron_sword_effect = "strange + 3"  # 7
time_iron_sword = 0

# bosses
giant_spider = "1st boss"  # 8
time_giant_spider = 5
Dragon = "2nd boss"  # 9
time_Dragon = 5
boss = 1

# check
# lvl = int(input("lvl: "))
# HP = 20 + lvl / 1.5
# strange = strange + lvl / 1.5
# speed = speed + lvl / 1.5

# beginning
print("Your statistics: ")
print("HP: " + str(HP))
print("strange: " + str(strange))
print("speed: " + str(speed))
print('lvl: ' + str(lvl))
print('exp: ' + str(exp))
ready = input("hello! Are you ready? Nobody won. (y/n): ")

if ready == "n":
    print("No, you will play")
    ready = "y"

while ready == "y":
    random_num = random.randint(0, 10)
    # mobs
    if random_num == 0:  # zombie 0
        if lvl <= 5:
            zombie_HP = 10
            while True:
                print("-------------")
                print('zombie:')
                print('HP: ' + str(zombie_HP))
                print('strange: ' + str(zombie_strange))
                print('speed: ' + str(zombie_speed))
                time.sleep(0.1)
                print("Your statistics: ")
                print("HP: " + str(HP))
                print("strange: " + str(strange))
                print("speed: " + str(speed))
                print('lvl: ' + str(lvl))
                print("exp: " + str(exp))
                choice = input("You can use attack(1), defense(2): ")
                if choice == '1':  # attack
                    attack_random = random.randint(0, 1)
                    if attack_random == 0:
                        attack_random = random.randint(0, 2)
                        print("you used to attack.")
                        zombie_HP = zombie_HP - strange
                        HP = HP - zombie_strange / 3
                        if zombie_HP <= 0:
                            time_healing_potion = time_healing_potion - 1
                            time_poison_flask = time_poison_flask - 1
                            time_giant_spider = time_giant_spider - 1
                            time_Dragon = time_Dragon - 1
                            defense = defense - 1
                            zombie_HP = 10
                            exp = exp + zombie_HP / 3
                            random_num = random.randint(0, 1)
                            print("You killed zombie.")
                            if exp >= lvl * 10:
                                exp = 0
                                lvl = lvl + 1
                                HP = 20 + lvl / 1.5
                                strange = strange + lvl / 1.5
                                speed = speed + lvl / 1.5
                                print(
                                    "You've got lvl " + str(lvl) + '!')
                                break
                    elif attack_random == 1:
                        attack_random = random.randint(0, 1)
                        print("Zombie's faster.")
                        HP = HP - zombie_strange / 3.2
                        if HP < 1:  # die
                            print(
                                "You died! The zombie is so dangerous.")
                            exit()
                elif choice == "2":  # defense
                    random_num = random.randint(0, 1)
                    if speed > zombie_speed and defense < 5:
                        print("You used to defense.")
                        HP = HP + 1
                        defense = defense + 1
                    else:
                        print("Zombie's faster.")
                        HP = HP - zombie_strange
                        if HP < 1:  # die
                            print(
                                "You died! The zombie is so dangerous.")
                            exit()
    if random_num == 1:  # skeleton 1
        if lvl <= 5 and lvl > 2:
            skeleton_HP = 15
            while True:
                print("-------------")
                print('skeleton:')
                print('HP: ' + str(skeleton_HP))
                print('speed: ' + str(skeleton_speed))
                print('strange: ' + str(skeleton_strange))
                time.sleep(0.1)
                print("Your statistics: ")
                print("HP: " + str(HP))
                print("strange: " + str(strange))
                print("speed: " + str(speed))
                print('lvl: ' + str(lvl))
                print("exp: " + str(exp))
                choice = input("You can use attack(1), defense(2): ")
                if choice == '1':  # attack
                    attack_random = random.randint(0, 1)
                    if attack_random == 0:
                        attack_random = random.randint(0, 2)
                        print("you used to attack.")
                        skeleton_HP = skeleton_HP - strange
                        HP = HP - skeleton_strange / 3
                        if skeleton_HP <= 0:
                            time_healing_potion = time_healing_potion - 1
                            time_poison_flask = time_poison_flask - 1
                            time_giant_spider = time_giant_spider - 1
                            time_Dragon = time_Dragon - 1
                            defense = defense - 1
                            skeleton_HP = 15
                            exp = exp + skeleton_HP / 3
                            random_num = random.randint(0, 1)
                            print("You killed skeleton.")
                            if exp >= lvl * 10:
                                exp = 0
                                lvl = lvl + 1
                                HP = 20 + lvl / 1.5
                                strange = strange + lvl / 1.5
                                speed = speed + lvl / 1.5
                                print(
                                    "You've got lvl " + str(lvl) + '!')
                            break
                    elif attack_random == 1:
                        attack_random = random.randint(0, 1)
                        print("Skeleton's faster.")
                        HP = HP - skeleton_strange / 3.2
                        if HP < 1:  # die
                            print(
                                "You died! The skeleton is so dangerous.")
                            exit()
                elif choice == "2":  # defense
                    random_num = random.randint(0, 1)
                    if speed > zombie_speed and defense < 5:
                        print("You used to defense.")
                        HP = HP + 1
                        defense = defense + 1
                    else:
                        print("Skeleton's faster.")
                        HP = HP - zombie_strange
                        if HP < 1:  # die
                            print(
                                "You died! The zombie is so dangerous.")
                            exit()
    if random_num == 2:  # snake 2
        if lvl >= 5:
            snake_HP = 30
            while True:
                print("-------------")
                print('snake:')
                print('HP: ' + str(snake_HP))
                print('speed: ' + str(snake_speed))
                print('strange: ' + str(snake_strange))
                time.sleep(0.1)
                print("Your statistics: ")
                print("HP: " + str(HP))
                print("strange: " + str(strange))
                print("speed: " + str(speed))
                print('lvl: ' + str(lvl))
                print("exp: " + str(exp))
                choice = input("You can use attack(1), defense(2): ")
                if choice == '1':  # attack
                    attack_random = random.randint(0, 1)
                    if attack_random == 0:
                        attack_random = random.randint(0, 2)
                        print("you used to attack.")
                        snake_HP = snake_HP - strange
                        HP = HP - snake_strange / 3
                        if snake_HP <= 0:
                            time_healing_potion = time_healing_potion - 1
                            time_poison_flask = time_poison_flask - 1
                            time_giant_spider = time_giant_spider - 1
                            time_Dragon = time_Dragon - 1
                            defense = defense - 1
                            snake_HP = 30
                            exp = exp + snake_HP / 3
                            random_num = random.randint(0, 1)
                            print("You killed snake.")
                            if exp >= lvl * 10:
                                exp = 0
                                lvl = lvl + 1
                                HP = 20 + lvl / 1.5
                                strange = strange + lvl / 1.5
                                speed = speed + lvl / 1.5
                                print(
                                    "You've got lvl " + str(lvl) + '!')
                            break
                    elif attack_random == 1:
                        attack_random = random.randint(0, 1)
                        print("Snake's faster.")
                        HP = HP - snake_strange / 3.2
                        if HP < 1:  # die
                            print(
                                "You died! The snake is so dangerous.")
                            exit()
                elif choice == "2":  # defense
                    random_num = random.randint(0, 1)
                    if speed > zombie_speed and defense < 5:
                        print("You used to defense.")
                        HP = HP + 1
                        defense = defense + 1
                    else:
                        print("Snake's faster.")
                        HP = HP - zombie_strange
                        if HP < 1:  # die
                            print(
                                "You died! The zombie is so dangerous.")
                            exit()
    if random_num == 3:  # bear 3
        if lvl >= 8:

            bear_HP = 25
            while True:
                print("-------------")
                print('bear:')
                print('HP: ' + str(bear_HP))
                print('speed: ' + str(bear_speed))
                print('strange: ' + str(bear_strange))
                time.sleep(0.1)
                print("Your statistics: ")
                print("HP: " + str(HP))
                print("strange: " + str(strange))
                print("speed: " + str(speed))
                print('lvl: ' + str(lvl))
                print("exp: " + str(exp))
                choice = input("You can use attack(1), defense(2): ")
                if choice == '1':  # attack
                    attack_random = random.randint(0, 1)
                    if attack_random == 0:
                        attack_random = random.randint(0, 2)
                        print("you used to attack.")
                        bear_HP = bear_HP - strange
                        HP = HP - bear_strange / 3
                        if bear_HP <= 0:
                            time_healing_potion = time_healing_potion - 1
                            time_poison_flask = time_poison_flask - 1
                            time_giant_spider = time_giant_spider - 1
                            time_Dragon = time_Dragon - 1
                            defense = defense - 1
                            bear_HP = 30
                            exp = exp + bear_HP / 3
                            random_num = random.randint(0, 1)
                            print("You killed bear.")
                            if exp >= lvl * 10:
                                exp = 0
                                lvl = lvl + 1
                                HP = 20 + lvl / 1.5
                                strange = strange + lvl / 1.5
                                speed = speed + lvl / 1.5
                                print(
                                    "You've got lvl " + str(lvl) + '!')
                            break
                    elif attack_random == 1:
                        attack_random = random.randint(0, 1)
                        print("Bear's faster.")
                        HP = HP - bear_strange / 3.2
                        if HP < 1:  # die
                            print(
                                "You died! The bear is so dangerous.")
                            exit()
                elif choice == "2":  # defense
                    random_num = random.randint(0, 1)
                    if speed > zombie_speed and defense < 5:
                        print("You used to defense.")
                        HP = HP + 1
                        defense = defense + 1
                    else:
                        print("Bear's faster.")
                        HP = HP - zombie_strange
                        if HP < 1:  # die
                            print(
                                "You died! The zombie is so dangerous.")
                            exit()
    # items
    if random_num == 4:
        if time_healing_potion <= 0:
            print("-------------")
            print(f"You found a healing potion! It's +10% for your speed and HP.")
            time.sleep(0.5)
            HP = HP * 1.1
            speed = speed * 1.25
            time_healing_potion = 10
    if random_num == 5:
        if time_poison_flask <= 0:
            print("-------------")
            print(f"You found a poison flask! It's -10% for your speed and HP.")
            time.sleep(0.5)
            HP = HP * 0.9
            speed = speed * 0.75
            time_poison_flask = 10
    if random_num == 6:
        if time_wooden_sword <= 0:
            print("-------------")
            print("You found a wooden sword! It's +1 for your strange.")
            time.sleep(0.5)
            strange = strange + 1
            time_wooden_sword = 1
    if random_num == 7:
        if time_iron_sword <= 0:
            print("-------------")
            print("You found a iron sword! It's +3 for your strange.")
            time.sleep(0.5)
            strange = strange + 3
            time_iron_sword = 1
    # bosses
    if random_num == 8:
        if time_giant_spider <= 0:
            if boss == 1:
                print("-------------")
                print("You found a cave! It's dangerous!")
                question = input("Do you wanna go inside(yes/no): ")
                if question == 'yes':
                    print("There are only spiderweb.")
                    time.sleep(6.23)
                    print("You found 3 big spiders!")
                    BigSpider = 3
                    big_spider_HP = 55
                    big_spider_speed = 10
                    big_spider_strange = 8
                    print("No info about these big spiders.")
                    while True:
                        print("-------------")
                        print("Your statistics: ")
                        print("HP: " + str(HP))
                        print("strange: " + str(strange))
                        print("speed: " + str(speed))
                        print("lvl: " + str(lvl))
                        print("exp: " + str(exp))
                        choice = input("You can use attack(1), defense(2): ")
                        if choice == '1':  # attack
                            attack_random = random.randint(0, 1)
                            if attack_random == 0:
                                print("you used to attack.")
                                big_spider_HP = big_spider_HP - strange
                                HP = HP - strange / 3
                                if HP < 1:  # die
                                    print("You died!")
                                    print("Shift + f10 to try again.")
                                print("big spiders is not die. try again.")
                                if big_spider_HP <= 0:
                                    defense = defense - 1
                                    print(
                                        "You killed all big spiders in cave.")
                                    time_healing_potion = time_healing_potion - 3
                                    time_poison_flask = time_poison_flask - 3
                                    time_giant_spider = time_giant_spider - 3
                                    time_Dragon = time_Dragon - 3
                                    big_spider_HP = 25
                                    exp = exp + big_spider_HP / 3
                                    time.sleep(3)
                                    print("You're going forward.")
                                    time.sleep(3)
                                    print("And you found a giant spider!")
                                    giant_spider_HP = 100
                                    giant_spider_speed = 12
                                    giant_spider_strange = 12
                                    HP = 20 + lvl / 1.05
                                    while True:

                                        HP = 20 + lvl / 1.5
                                        time.sleep(1)
                                        print(
                                            "Ok. You need to kill a Giant spider!")
                                        print("-------------")
                                        print('giant spider:')
                                        print('HP: ' + str(giant_spider_HP))
                                        print('speed: ' +
                                              str(giant_spider_speed))
                                        print('strange: ' +
                                              str(giant_spider_strange))
                                        time.sleep(1)
                                        print("Your statistics: ")
                                        print("HP: " + str(HP))
                                        print("strange: " + str(strange))
                                        print("speed: " + str(speed))
                                        print('lvl: ' + str(lvl))
                                        print("exp: " + str(exp))
                                        choice = input(
                                            "You can use attack(1), defense(2): ")
                                        if choice == '1':
                                            attack_random = random.randint(
                                                0, 1)
                                            if attack_random == 0:
                                                attack_random = random.randint(
                                                    0, 1)
                                                print("you used to attack.")
                                                giant_spider_HP = giant_spider_HP - strange
                                                HP = HP - giant_spider_strange / 3
                                                if giant_spider_HP <= 0:
                                                    giant_spider_HP = 100
                                                    time_healing_potion = time_healing_potion - 1
                                                    time_poison_flask = time_poison_flask - 1
                                                    time_giant_spider = time_giant_spider - 1
                                                    time_Dragon = time_Dragon - 1
                                                    defense = defense - 1
                                                    print(
                                                        "You killed Boss - giant spider!")
                                                    exp = exp + giant_spider_HP / 3
                                                    random_num = random.randint(0, 1)
                                                    lvl = lvl + 1  # lvl + 1 after boss
                                                    HP = 20 + lvl / 1.5
                                                    strange = strange + lvl / 1.5
                                                    speed = speed + lvl / 1.5
                                                    boss = 2
                                                    print(
                                                        "You've got lvl " + str(lvl) + '!')
                                                    break
                                            elif attack_random == 1:
                                                print("Giant spider's faster.")
                                                HP = HP - giant_spider_strange / 3.2
                                                if HP < 1:  # die
                                                    print("You died!")
                                                    print("giant spider's HP:" +
                                                          str(giant_spider_HP))
                                                    if giant_spider_HP <= 0:
                                                        print(
                                                            "You killed Boss - giant spider!")
                                                        boss = 2
                                                        exp = exp + giant_spider_HP / 3
                                                        random_num = random.randint(
                                                            0, 1)
                                                        lvl = lvl + 1  # lvl + 1 after boss
                                                        HP = 20 + lvl / 1.5
                                                        strange = strange + lvl / 1.5
                                                        speed = speed + lvl / 1.5
                                                        print(
                                                            "You've got lvl " + str(lvl) + '!')
                                                    break
                                        elif choice == "2":  # defense
                                            random_num = random.randint(0, 1)
                                            if speed > giant_spider_speed and defense < 5:
                                                print("You used to defense.")
                                                HP = HP + 1
                                                defense = defense + 1
                                            else:
                                                print("Giant spider's faster.")
                                                HP = HP - giant_spider_strange
                                                if HP < 1:  # die
                                                    print(
                                                        "You died!")
                                                    print(
                                                        "Shift + f10 or Ctrl + Alt + n to try again.")
                                                    exit()
                            elif attack_random == 1:
                                print("Big spider's faster.")
                                HP = HP - big_spider_strange
                                if HP < 1:  # die
                                    print("You died!")
                                    print("Shift + f10 to try again")
                                    exit()
                        elif choice == "2":  # defense
                            random_num = random.randint(0, 1)
                            if speed > big_spider_speed and defense < 5:
                                print("You used to defense.")
                                HP = HP + 1
                                defense = defense + 1
                            else:
                                print("Big spider's faster.")
                                HP = HP - big_spider_strange
                                if HP < 1:  # die
                                    print(
                                        "You died!")
                                    print(
                                        "Shift + f10 or Ctrl + Alt + n to try again.")
                                    exit()
                elif question == "no":
                    print("Ok, it's your choice.")
                    time.sleep(0.1)
        if time_giant_spider > 0:
            time_giant_spider = 3
    if random_num == 9:
        if time_Dragon <= 0:
            if boss == 2:
                print("-------------")
                print("You found a portal of hell! It's so dangerous and hot!")
                question = input("Do you wanna go inside(yes/no): ")
                if question == 'yes':
                    print("There are only fire.")
                    time.sleep(6.23)
                    print("You found magma cubes!")
                    magma_cube_HP = 60
                    magma_cube_speed = 15
                    magma_cube_strange = 5
                    print("No info about that.")
                    while True:
                        print("-------------")
                        print("Your statistics: ")
                        print("HP: " + str(HP))
                        print("strange: " + str(strange))
                        print("speed: " + str(speed))
                        print("lvl: " + str(lvl))
                        print("exp: " + str(exp))
                        choice = input(
                            "You can use attack(1), defense(2): ")
                        if choice == '1':  # attack
                            attack_random = random.randint(0, 1)
                            if attack_random == 0:
                                print("you used to attack.")
                                magma_cube_HP = magma_cube_HP - strange
                                HP = HP - strange / 3
                                if HP < 1:  # die
                                    print("You died!")
                                    print("Shift + f10 to try again.")
                                print("Magma cubes are not die. try again.")
                                if magma_cube_HP <= 0:
                                    defense = defense - 1
                                    print(
                                        "You killed all magma cubes.")
                                    time_healing_potion = time_healing_potion - 1
                                    time_poison_flask = time_poison_flask - 1
                                    time_giant_spider = time_giant_spider - 1
                                    time_Dragon = time_Dragon - 1
                                    magma_cube_HP = 25
                                    exp = exp + magma_cube_HP / 3
                                    time.sleep(3)
                                    print("you're going to further.")
                                    time.sleep(3)
                                    print(
                                        "And you found the last boss - The Dragon!!!")
                                    Dragon_HP = 150
                                    Dragon_speed = 8
                                    Dragon_strange = 16
                                    while True:
                                        time.sleep(1)
                                        print(
                                            "Ok. You need to kill a Dragon!")
                                        print("-------------")
                                        print('Dragon:')
                                        print('HP: ' + str(Dragon_HP))
                                        print('speed: ' +
                                              str(Dragon_speed))
                                        print('strange: ' +
                                              str(Dragon_strange))
                                        time.sleep(1)
                                        print("Your statistics: ")
                                        print("HP: " + str(HP))
                                        print("strange: " + str(speed))
                                        print("speed: " + str(strange))
                                        print('lvl: ' + str(lvl))
                                        print("exp: " + str(exp))
                                        choice = input(
                                            "You can use attack(1), defense(2): ")
                                        if choice == '1':  # attack
                                            attack_random = random.randint(
                                                0, 1)
                                            if attack_random == 0:
                                                print(
                                                    "you used to attack.")
                                                giant_spider_HP = Dragon_HP - strange
                                                HP = HP - Dragon_strange / 3
                                                if Dragon_HP <= 0:
                                                    defense = defense - 1
                                                    print(
                                                        "You killed Boss - Dragon!")
                                                    exp = exp + Dragon_HP / 3
                                                    random_num = random.randint(
                                                        0, 1)
                                                    lvl = lvl + 1  # lvl + 1 after boss
                                                    HP = 20 + lvl / 1.5
                                                    strange = strange + lvl / 1.5
                                                    speed = speed + lvl / 1.5
                                                    print(
                                                        "You've got lvl " + str(lvl) + '!')
                                                    print(
                                                        "And you've done this game!")
                                                    print("YES!!!")
                                                    print("AMAZING!!!")
                                                    print("PERFECT!!!")
                                                    exit()
                                            elif attack_random == 1:
                                                print("Dragon's faster.")
                                                HP = HP - Dragon_strange / 3.2
                                                if HP < 1:  # die
                                                    print("You died!")
                                                    print("Dragon's HP:" +
                                                          str(Dragon_HP))
                                                if Dragon_HP <= 0:
                                                    defense = defense - 1
                                                    print(
                                                        "You killed Boss - Dragon!")
                                                    exp = exp + Dragon_HP / 3
                                                    random_num = random.randint(
                                                        0, 1)
                                                    lvl = lvl + 1  # lvl + 1 after boss
                                                    HP = 20 + lvl / 1.5
                                                    strange = strange + lvl / 1.5
                                                    speed = speed + lvl / 1.5
                                                    print(
                                                        "You've got lvl " + str(lvl) + '!')
                                                    print(
                                                        "And you've done this game!")
                                                    print("YES!!!")
                                                    print("AMAZING!!!")
                                                    print("PERFECT!!!")
                                                    exit()
                                        elif choice == "2":  # defense
                                            random_num = random.randint(0, 1)
                                            if speed > Dragon_speed and defense < 5:
                                                print(
                                                    "You used to defense.")
                                                HP = HP + HP / 20
                                                defense = defense + 1
                                            else:
                                                print("Dragon's faster.")
                                                HP = HP - Dragon_strange
                                                if HP < 1:  # die
                                                    print(
                                                        "You died! The Dragon is too dangerous.")
                                                    print(
                                                        "Shift + f10 or Ctrl + Alt + n to try again.")
                                                    exit()
                            elif attack_random == 1:
                                print("Magma cubes're faster.")
                                HP = HP - magma_cube_strange
                                if HP < 1:  # die
                                    print("You died!")
                                    print("Shift + f10 to try again")
                                    exit()
                        elif choice == "2":  # defense
                            random_num = random.randint(0, 1)
                            if speed > magma_cube_speed and defense < 5:
                                print("You used to defense.")
                                HP = HP + HP / 20
                                defense = defense + 1
                            else:
                                print("Magma cubes're faster.")
                                HP = HP - magma_cube_strange
                                if HP < 1:  # die
                                    print(
                                        "You died! The Magma cubes are so dangerous.")
                                    print(
                                        "Shift + f10 or Ctrl + Alt + n to try again.")
                                    exit()
                elif question == "no":
                    print("Ok, it's your choice.")
                    time.sleep(0.1)
            if time_Dragon > 0:
                time_Dragon = 3
