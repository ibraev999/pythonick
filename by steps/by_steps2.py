import pygame
import random
# import button
from time import sleep
# button class
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
# int () in the attack and defance
# starting statistics
HP = 50
strange = 20
speed = 0.8
lvl = 1
exp = 0
defense = 0
player_num = 1110
random_num = 1110
animation_num = 1110
background_num = 0
kill = False
clock = pygame.time.Clock()
# HP
zombie_HP = 55  # 0
skeleton_HP = 70  # 1
spider_HP = 70  # 3

# speed
zombie_speed = 0.5  # 0
skeleton_speed = 1.5  # 1
spider_speed = 3  # 3

# strange
zombie_strange = 8  # 0
skeleton_strange = 20  # 1
spider_strange = 30  # 3


# items
healing_potion_effect = "+25% speed and HP"  # 4
time_healing_potion = 8
poison_flask_effect = "-25% speed and HP"  # 5
time_poison_flask = 8
wooden_sword_effect = "strange + 10%"  # 6
time_wooden_sword = 0
iron_sword_effect = "strange + 30%"  # 7
time_iron_sword = 0

# bosses
giant_spider = "1st boss"  # 8
time_giant_spider = 5
Dragon = "2nd boss"  # 9
time_Dragon = 5
boss = 1
boss_HP = 400
boss_speed = 4
boss_strange = 222
boss = 0
# create display window
SCREEN_HEIGHT = 645
SCREEN_WIDTH = 645
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("By steps(version 1.0)")

# load button images
start_img = pygame.image.load(r"textures\button_play.png").convert_alpha()
exit_img = pygame.image.load(r"textures\button_quit.png").convert_alpha()
attack_img = pygame.image.load(r"textures\button_attack.png").convert_alpha()
defance_img = pygame.image.load(r"textures\button_defance.png").convert_alpha()
# load images
background_normal = pygame.image.load(r"textures\background_normal.png").convert_alpha()
background_hell = pygame.image.load(r"textures\background_hell.png").convert_alpha()
background_cave = pygame.image.load(r"textures\background_cave.png").convert_alpha()
player = pygame.image.load(r"textures\player.png").convert_alpha()
player_attack = pygame.image.load(r"textures\player_attack.png").convert_alpha()
player_defence = pygame.image.load(r"textures\player_defence.png").convert_alpha()
zombie = pygame.image.load(r"textures\zombie.png").convert_alpha()
skeleton = pygame.image.load(r"textures\skeleton.png").convert_alpha()
spider = pygame.image.load(r"textures\spider.png").convert_alpha()
boss_image = pygame.image.load(r"textures\big_spider.png").convert_alpha()
health = pygame.image.load(r"textures\health.png").convert_alpha()
kill_image = pygame.image.load(r"textures\kill.png").convert_alpha()

# create button instances

start_button = Button(150, 402, start_img, 0.8)
exit_button = Button(150, 502, exit_img, 0.8)
attack_button = Button(1395, 395, attack_img, 0.8)
defance_button = Button(31195, 145, defance_img, 0.8)
# game loop
run = True


# health bars
class Player0(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((200, 30, 30))
        self.rect = self.image.get_rect(center=(400, 400))
        self.current_health = 0
        self.target_health = 50
        self.max_health = 50
        self.health_bar_length = 400
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 1

    def get_damage(self, amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    def get_health(self, amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health

    def update(self):
        self.advanced_health()

    def advanced_health(self):
        transition_width = 0
        transition_color = (255, 0, 0)

        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed

        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed
            transition_width = int(
                (self.target_health - self.current_health) / self.health_ratio
            )
            transition_color = (255, 255, 0)

        health_bar_width = int(self.current_health / self.health_ratio)
        health_bar = pygame.Rect(210, 20, health_bar_width, 25)
        # transition_bar = pygame.Rect(health_bar.right, 45, transition_width, 25)

        pygame.draw.rect(screen, (255, 0, 0), health_bar)
        # pygame.draw.rect(screen, transition_color, transition_bar)
        pygame.draw.rect(
            screen, (255, 255, 255), (210, 20, self.health_bar_length, 25), 4
        )


class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((200, 30, 30))
        self.rect = self.image.get_rect(center=(400, 400))
        self.current_health = 0
        self.target_health = 50
        self.max_health = 50
        self.health_bar_length = 400
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 1

    def get_damage(self, amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    def get_health(self, amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health

    def update(self):
        self.advanced_health()

    def advanced_health(self):
        transition_width = 0
        transition_color = (255, 0, 0)

        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed

        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed
            transition_width = int(
                (self.target_health - self.current_health) / self.health_ratio
            )
            transition_color = (255, 255, 0)

        health_bar_width = int(self.current_health / self.health_ratio)
        health_bar = pygame.Rect(20, 595, health_bar_width, 25)

        pygame.draw.rect(screen, (255, 0, 0), health_bar)
        pygame.draw.rect(
            screen, (255, 255, 255), (20, 595, self.health_bar_length, 25), 4
        )


while run:
    # print("---------------------")
    # print("Your statistics: ")
    # print("HP: " + str(HP))
    # print("strange: " + str(strange))
    # print("speed: " + str(speed))
    # print("lvl: " + str(lvl))
    # print("exp: " + str(exp))
    if kill == True:
        lvl = lvl + 1
        HP = 100
        strange = strange + lvl * 1.7
        speed = speed + lvl * 1.7
        kill = False
        boss += 1
    if background_num == 0:
        screen.blit(background_normal, (0, 0))
    if background_num == 1:
        screen.blit(background_cave, (0, 0))
    if background_num == 2:
        screen.blit(background_hell, (0, 0))
    # animation
    if player_num == 0:
        screen.blit(player, (-20, 192))
    if player_num == 1:
        screen.blit(player_attack, (-20, 192))
    if player_num == 2:
        screen.blit(player_defence, (-20, 192))
    if random_num == 0:
        screen.blit(zombie, (360, 40))
        try:
            player1.sprite.target_health(55)
            player1.sprite.max_health(55)
        except:
            None
    if random_num == 1:
        screen.blit(skeleton, (360, 40))
        try:
            player1.sprite.target_health(70)
            player1.sprite.max_health(70)
        except:
            None
    if random_num == 2:
        screen.blit(spider, (230, 170))
        try:
            player1.sprite.target_health(70)
            player1.sprite.max_health(70)
        except:
            None
    if boss == 5:
        random_num = 333
        screen.blit(boss_image, (230, 170))
        try:
            player1.sprite.target_health(400)
            player1.sprite.max_health(400)
        except:
            None        
    if start_button.draw(screen):
        attack_button = button.Button(495, 495, attack_img, 0.8)
        defance_button = button.Button(495, 345, defance_img, 0.8)
        start_button = button.Button(152120, 402, start_img, 0.8)
        exit_button = button.Button(15110, 502, exit_img, 0.8)
        player0 = pygame.sprite.GroupSingle(Player0())
        player1 = pygame.sprite.GroupSingle(Player1())
        player_num = 0
        random_num = 0
    if exit_button.draw(screen):
        run = False
    if attack_button.draw(screen):
        sleep(0.5)
        player_num = 1
        if boss == 5:
            attack_random = random.randint(0, 3)
            if attack_random == 0:
                boss_HP -= strange
                player0.sprite.get_damage(strange)
                if HP <= 0:
                    player0 = 12
                    player1 = 14
                    start_button = button.Button(150, 402, start_img, 0.8)
                    exit_button = button.Button(150, 502, exit_img, 0.8)
                    attack_button = button.Button(1395, 395, attack_img, 0.8)
                    defance_button = button.Button(31195, 145, defance_img, 0.8)
                    # starting statistics
                    HP = 50
                    strange = 20
                    speed = 0.8
                    lvl = 1
                    exp = 0
                    defense = 0
                    player_num = 1110
                    random_num = 1110
                    animation_num = 1110
                    background_num = 0
                    clock = pygame.time.Clock()
                    # HP
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70  # 3

                    # speed
                    zombie_speed = 0.5  # 0
                    skeleton_speed = 1.5  # 1
                    spider_speed = 3  # 3

                    # strange
                    zombie_strange = 8  # 0
                    skeleton_strange = 20  # 1
                    spider_strange = 30  # 3

                    # items
                    healing_potion_effect = "+25% speed and HP"  # 4
                    time_healing_potion = 8
                    poison_flask_effect = "-25% speed and HP"  # 5
                    time_poison_flask = 8
                    wooden_sword_effect = "strange + 10%"  # 6
                    time_wooden_sword = 0
                    iron_sword_effect = "strange + 30%"  # 7
                    time_iron_sword = 0

                    # bosses
                    giant_spider = "1st boss"  # 8
                    time_giant_spider = 5
                    Dragon = "2nd boss"  # 9
                    time_Dragon = 5
                    boss = 1
                if boss_HP <= 0:
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    attack_button = button.Button(495, 495, attack_img, 0.8)
                    defance_button = button.Button(495, 345, defance_img, 0.8)
                    start_button = button.Button(152120, 402, start_img, 0.8)
                    exit_button = button.Button(15110, 502, exit_img, 0.8)
                    player0 = pygame.sprite.GroupSingle(Player0())
                    player_num = 0
                    # screen.blit(kill, (375, 40))

                    time_healing_potion = time_healing_potion - 1
                    time_poison_flask = time_poison_flask - 1
                    time_giant_spider = time_giant_spider - 1
                    time_Dragon = time_Dragon - 1
                    defense = defense - 1
                    exp = exp + zombie_HP / 3
                    # random
                    random_num = 2
                    kill = True

            else:
                attack_random = random.randint(0, 3)
                zombie_HP -= strange / 3
                player0.sprite.get_damage(strange / 3)
                HP -= zombie_strange
                player1.sprite.get_damage(zombie_strange)
                if HP <= 0:  # die
                    player0 = 12
                    player1 = 14
                    start_button = button.Button(150, 402, start_img, 0.8)
                    exit_button = button.Button(150, 502, exit_img, 0.8)
                    attack_button = button.Button(1395, 395, attack_img, 0.8)
                    defance_button = button.Button(31195, 145, defance_img, 0.8)
                    # starting statistics
                    HP = 50
                    strange = 20
                    speed = 0.8
                    lvl = 1
                    exp = 0
                    defense = 0
                    player_num = 1110
                    random_num = 1110
                    animation_num = 1110
                    background_num = 0
                    clock = pygame.time.Clock()
                    # HP
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70  # 3

                    # speed
                    zombie_speed = 0.5  # 0
                    skeleton_speed = 1.5  # 1
                    spider_speed = 3  # 3

                    # strange
                    zombie_strange = 8  # 0
                    skeleton_strange = 20  # 1
                    spider_strange = 30  # 3

                    # items
                    healing_potion_effect = "+25% speed and HP"  # 4
                    time_healing_potion = 8
                    poison_flask_effect = "-25% speed and HP"  # 5
                    time_poison_flask = 8
                    wooden_sword_effect = "strange + 10%"  # 6
                    time_wooden_sword = 0
                    iron_sword_effect = "strange + 30%"  # 7
                    time_iron_sword = 0

                    # bosses
                    giant_spider = "1st boss"  # 8
                    time_giant_spider = 5
                    Dragon = "2nd boss"  # 9
                    time_Dragon = 5
                    boss = 1
                if zombie_HP <= 0:
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    attack_button = button.Button(495, 495, attack_img, 0.8)
                    defance_button = button.Button(495, 345, defance_img, 0.8)
                    start_button = button.Button(152120, 402, start_img, 0.8)
                    exit_button = button.Button(15110, 502, exit_img, 0.8)
                    player0 = pygame.sprite.GroupSingle(Player0())
                    player_num = 0
                    # screen.blit(kill, (375, 40))

                    time_healing_potion = time_healing_potion - 1
                    time_poison_flask = time_poison_flask - 1
                    time_giant_spider = time_giant_spider - 1
                    time_Dragon = time_Dragon - 1
                    defense = defense - 1
                    exp = exp + zombie_HP / 3
                    # random
                    random_num = 2
                    if exp >= lvl * 10:
                        exp = 0
                        lvl = lvl + 1
                        HP = 20
                        strange = strange + lvl / 1.5
                        speed = speed + lvl / 1.5

        if random_num == 0:
            attack_random = random.randint(0, 3)
            if attack_random == 0:
                zombie_HP -= strange
                player0.sprite.get_damage(strange)
                if HP <= 0:
                    player0 = 12
                    player1 = 14
                    start_button = button.Button(150, 402, start_img, 0.8)
                    exit_button = button.Button(150, 502, exit_img, 0.8)
                    attack_button = button.Button(1395, 395, attack_img, 0.8)
                    defance_button = button.Button(31195, 145, defance_img, 0.8)
                    # starting statistics
                    HP = 50
                    strange = 20
                    speed = 0.8
                    lvl = 1
                    exp = 0
                    defense = 0
                    player_num = 1110
                    random_num = 1110
                    animation_num = 1110
                    background_num = 0
                    clock = pygame.time.Clock()
                    # HP
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70  # 3

                    # speed
                    zombie_speed = 0.5  # 0
                    skeleton_speed = 1.5  # 1
                    spider_speed = 3  # 3

                    # strange
                    zombie_strange = 8  # 0
                    skeleton_strange = 20  # 1
                    spider_strange = 30  # 3

                    # items
                    healing_potion_effect = "+25% speed and HP"  # 4
                    time_healing_potion = 8
                    poison_flask_effect = "-25% speed and HP"  # 5
                    time_poison_flask = 8
                    wooden_sword_effect = "strange + 10%"  # 6
                    time_wooden_sword = 0
                    iron_sword_effect = "strange + 30%"  # 7
                    time_iron_sword = 0

                    # bosses
                    giant_spider = "1st boss"  # 8
                    time_giant_spider = 5
                    Dragon = "2nd boss"  # 9
                    time_Dragon = 5
                    boss = 1
                if zombie_HP <= 0:
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    attack_button = button.Button(495, 495, attack_img, 0.8)
                    defance_button = button.Button(495, 345, defance_img, 0.8)
                    start_button = button.Button(152120, 402, start_img, 0.8)
                    exit_button = button.Button(15110, 502, exit_img, 0.8)
                    player0 = pygame.sprite.GroupSingle(Player0())
                    player_num = 0
                    # screen.blit(kill, (375, 40))

                    time_healing_potion = time_healing_potion - 1
                    time_poison_flask = time_poison_flask - 1
                    time_giant_spider = time_giant_spider - 1
                    time_Dragon = time_Dragon - 1
                    defense = defense - 1
                    exp = exp + zombie_HP / 3
                    # random
                    random_num = 2
                    kill = True

            else:
                attack_random = random.randint(0, 3)
                zombie_HP -= strange / 3
                player0.sprite.get_damage(strange / 3)
                HP -= zombie_strange
                player1.sprite.get_damage(zombie_strange)
                if HP <= 0:  # die
                    player0 = 12
                    player1 = 14
                    start_button = button.Button(150, 402, start_img, 0.8)
                    exit_button = button.Button(150, 502, exit_img, 0.8)
                    attack_button = button.Button(1395, 395, attack_img, 0.8)
                    defance_button = button.Button(31195, 145, defance_img, 0.8)
                    # starting statistics
                    HP = 50
                    strange = 20
                    speed = 0.8
                    lvl = 1
                    exp = 0
                    defense = 0
                    player_num = 1110
                    random_num = 1110
                    animation_num = 1110
                    background_num = 0
                    clock = pygame.time.Clock()
                    # HP
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70  # 3

                    # speed
                    zombie_speed = 0.5  # 0
                    skeleton_speed = 1.5  # 1
                    spider_speed = 3  # 3

                    # strange
                    zombie_strange = 8  # 0
                    skeleton_strange = 20  # 1
                    spider_strange = 30  # 3

                    # items
                    healing_potion_effect = "+25% speed and HP"  # 4
                    time_healing_potion = 8
                    poison_flask_effect = "-25% speed and HP"  # 5
                    time_poison_flask = 8
                    wooden_sword_effect = "strange + 10%"  # 6
                    time_wooden_sword = 0
                    iron_sword_effect = "strange + 30%"  # 7
                    time_iron_sword = 0

                    # bosses
                    giant_spider = "1st boss"  # 8
                    time_giant_spider = 5
                    Dragon = "2nd boss"  # 9
                    time_Dragon = 5
                    boss = 1
                if zombie_HP <= 0:
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    attack_button = button.Button(495, 495, attack_img, 0.8)
                    defance_button = button.Button(495, 345, defance_img, 0.8)
                    start_button = button.Button(152120, 402, start_img, 0.8)
                    exit_button = button.Button(15110, 502, exit_img, 0.8)
                    player0 = pygame.sprite.GroupSingle(Player0())
                    player_num = 0
                    # screen.blit(kill, (375, 40))

                    time_healing_potion = time_healing_potion - 1
                    time_poison_flask = time_poison_flask - 1
                    time_giant_spider = time_giant_spider - 1
                    time_Dragon = time_Dragon - 1
                    defense = defense - 1
                    exp = exp + zombie_HP / 3
                    # random
                    random_num = 2
                    if exp >= lvl * 10:
                        exp = 0
                        lvl = lvl + 1
                        HP = 20
                        strange = strange + lvl / 1.5
                        speed = speed + lvl / 1.5
        if random_num == 1:
            attack_random = random.randint(0, 3)
            if attack_random == 0:
                skeleton_HP -= int(strange)
                player0.sprite.get_damage(int(strange))
                if HP <= 0:
                    player0 = 12
                    player1 = 14
                    start_button = button.Button(150, 402, start_img, 0.8)
                    exit_button = button.Button(150, 502, exit_img, 0.8)
                    attack_button = button.Button(1395, 395, attack_img, 0.8)
                    defance_button = button.Button(31195, 145, defance_img, 0.8)
                    # starting statistics
                    HP = 50
                    strange = 20
                    speed = 0.8
                    lvl = 1
                    exp = 0
                    defense = 0
                    player_num = 1110
                    random_num = 1110
                    animation_num = 1110
                    background_num = 0
                    clock = pygame.time.Clock()
                    # HP
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70  # 3

                    # speed
                    zombie_speed = 0.5  # 0
                    skeleton_speed = 1.5  # 1
                    spider_speed = 3  # 3

                    # strange
                    zombie_strange = 8  # 0
                    skeleton_strange = 20  # 1
                    spider_strange = 30  # 3

                    # items
                    healing_potion_effect = "+25% speed and HP"  # 4
                    time_healing_potion = 8
                    poison_flask_effect = "-25% speed and HP"  # 5
                    time_poison_flask = 8
                    wooden_sword_effect = "strange + 10%"  # 6
                    time_wooden_sword = 0
                    iron_sword_effect = "strange + 30%"  # 7
                    time_iron_sword = 0

                    # bosses
                    giant_spider = "1st boss"  # 8
                    time_giant_spider = 5
                    Dragon = "2nd boss"  # 9
                    time_Dragon = 5
                    boss = 1
                if skeleton_HP <= 0:
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70  # 2
                    attack_button = button.Button(495, 495, attack_img, 0.8)
                    defance_button = button.Button(495, 345, defance_img, 0.8)
                    start_button = button.Button(152120, 402, start_img, 0.8)
                    exit_button = button.Button(15110, 502, exit_img, 0.8)
                    player0 = pygame.sprite.GroupSingle(Player0())
                    player_num = 0
                    # screen.blit(kill, (375, 40))

                    time_healing_potion = time_healing_potion - 1
                    time_poison_flask = time_poison_flask - 1
                    time_giant_spider = time_giant_spider - 1
                    time_Dragon = time_Dragon - 1
                    defense = defense - 1
                    exp = exp + skeleton_HP / 3
                    # random
                    random_num = 2
                    kill = True

            else:
                attack_random = random.randint(0, 3)
                skeleton_HP -= strange / 3
                player0.sprite.get_damage(int(strange / 3))
                HP -= skeleton_strange
                player1.sprite.get_damage(int(skeleton_strange))
                if HP <= 0:  # die
                    player0 = 12
                    player1 = 14
                    start_button = button.Button(150, 402, start_img, 0.8)
                    exit_button = button.Button(150, 502, exit_img, 0.8)
                    attack_button = button.Button(1395, 395, attack_img, 0.8)
                    defance_button = button.Button(31195, 145, defance_img, 0.8)
                    # starting statistics
                    HP = 50
                    strange = 20
                    speed = 0.8
                    lvl = 1
                    exp = 0
                    defense = 0
                    player_num = 1110
                    random_num = 1110
                    animation_num = 1110
                    background_num = 0
                    clock = pygame.time.Clock()
                    # HP
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70  # 3

                    # speed
                    zombie_speed = 0.5  # 0
                    skeleton_speed = 1.5  # 1
                    spider_speed = 3  # 3

                    # strange
                    zombie_strange = 8  # 0
                    skeleton_strange = 20  # 1
                    spider_strange = 30  # 3

                    # items
                    healing_potion_effect = "+25% speed and HP"  # 4
                    time_healing_potion = 8
                    poison_flask_effect = "-25% speed and HP"  # 5
                    time_poison_flask = 8
                    wooden_sword_effect = "strange + 10%"  # 6
                    time_wooden_sword = 0
                    iron_sword_effect = "strange + 30%"  # 7
                    time_iron_sword = 0

                    # bosses
                    giant_spider = "1st boss"  # 8
                    time_giant_spider = 5
                    Dragon = "2nd boss"  # 9
                    time_Dragon = 5
                    boss = 1
                if skeleton_HP <= 0:
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70 # 2
                    attack_button = button.Button(495, 495, attack_img, 0.8)
                    defance_button = button.Button(495, 345, defance_img, 0.8)
                    start_button = button.Button(152120, 402, start_img, 0.8)
                    exit_button = button.Button(15110, 502, exit_img, 0.8)
                    player0 = pygame.sprite.GroupSingle(Player0())
                    player_num = 0
                    # screen.blit(kill, (375, 40))

                    time_healing_potion = time_healing_potion - 1
                    time_poison_flask = time_poison_flask - 1
                    time_giant_spider = time_giant_spider - 1
                    time_Dragon = time_Dragon - 1
                    defense = defense - 1
                    exp = exp + skeleton_HP / 3
                    # random+ skeleton_HP / 3
                    random_num = 2
                    if exp >= lvl * 10:
                        exp = 0
                        lvl = lvl + 1
                        HP = 20
                        strange = strange + lvl / 1.5
                        speed = speed + lvl / 1.5
        if random_num == 2:
            attack_random = random.randint(0, 3)
            if attack_random == 0:
                spider_HP -= strange
                player0.sprite.get_damage(int(strange))
                if HP <= 0:
                    player0 = 12
                    player1 = 14
                    start_button = button.Button(150, 402, start_img, 0.8)
                    exit_button = button.Button(150, 502, exit_img, 0.8)
                    attack_button = button.Button(1395, 395, attack_img, 0.8)
                    defance_button = button.Button(31195, 145, defance_img, 0.8)
                    # starting statistics
                    HP = 50
                    strange = 20
                    speed = 0.8
                    lvl = 1
                    exp = 0
                    defense = 0
                    player_num = 1110
                    random_num = 1110
                    animation_num = 1110
                    background_num = 0
                    clock = pygame.time.Clock()
                    # HP
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70  # 3

                    # speed
                    zombie_speed = 0.5  # 0
                    skeleton_speed = 1.5  # 1
                    spider_speed = 3  # 3

                    # strange
                    zombie_strange = 8  # 0
                    skeleton_strange = 20  # 1
                    spider_strange = 30  # 3

                    # items
                    healing_potion_effect = "+25% speed and HP"  # 4
                    time_healing_potion = 8
                    poison_flask_effect = "-25% speed and HP"  # 5
                    time_poison_flask = 8
                    wooden_sword_effect = "strange + 10%"  # 6
                    time_wooden_sword = 0
                    iron_sword_effect = "strange + 30%"  # 7
                    time_iron_sword = 0

                    # bosses
                    giant_spider = "1st boss"  # 8
                    time_giant_spider = 5
                    Dragon = "2nd boss"  # 9
                    time_Dragon = 5
                    boss = 1
                if spider_HP <= 0:
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70 # 2
                    attack_button = button.Button(495, 495, attack_img, 0.8)
                    defance_button = button.Button(495, 345, defance_img, 0.8)
                    start_button = button.Button(152120, 402, start_img, 0.8)
                    exit_button = button.Button(15110, 502, exit_img, 0.8)
                    player0 = pygame.sprite.GroupSingle(Player0())
                    player_num = 0
                    # screen.blit(kill, (375, 40))

                    time_healing_potion = time_healing_potion - 1
                    time_poison_flask = time_poison_flask - 1
                    time_giant_spider = time_giant_spider - 1
                    time_Dragon = time_Dragon - 1
                    defense = defense - 1
                    exp = exp + skeleton_HP / 3
                    # random
                    random_num = 2
                    kill = True

            else:
                attack_random = random.randint(0, 3)
                spider_HP -= strange / 3
                player0.sprite.get_damage(int(strange / 3))
                HP -= spider_strange
                player1.sprite.get_damage(int(spider_strange))
                if HP <= 0:  # die
                    player0 = 12
                    player1 = 14
                    start_button = button.Button(150, 402, start_img, 0.8)
                    exit_button = button.Button(150, 502, exit_img, 0.8)
                    attack_button = button.Button(1395, 395, attack_img, 0.8)
                    defance_button = button.Button(31195, 145, defance_img, 0.8)
                    # starting statistics
                    HP = 50
                    strange = 20
                    speed = 0.8
                    lvl = 1
                    exp = 0
                    defense = 0
                    player_num = 1110
                    random_num = 1110
                    animation_num = 1110
                    background_num = 0
                    clock = pygame.time.Clock()
                    # HP
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70  # 3

                    # speed
                    zombie_speed = 0.5  # 0
                    skeleton_speed = 1.5  # 1
                    spider_speed = 3  # 3

                    # strange
                    zombie_strange = 8  # 0
                    skeleton_strange = 20  # 1
                    spider_strange = 30  # 3

                    # items
                    healing_potion_effect = "+25% speed and HP"  # 4
                    time_healing_potion = 8
                    poison_flask_effect = "-25% speed and HP"  # 5
                    time_poison_flask = 8
                    wooden_sword_effect = "strange + 10%"  # 6
                    time_wooden_sword = 0
                    iron_sword_effect = "strange + 30%"  # 7
                    time_iron_sword = 0

                    # bosses
                    giant_spider = "1st boss"  # 8
                    time_giant_spider = 5
                    Dragon = "2nd boss"  # 9
                    time_Dragon = 5
                    boss = 1
                if spider_HP <= 0:
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70 # 2
                    attack_button = button.Button(495, 495, attack_img, 0.8)
                    defance_button = button.Button(495, 345, defance_img, 0.8)
                    start_button = button.Button(152120, 402, start_img, 0.8)
                    exit_button = button.Button(15110, 502, exit_img, 0.8)
                    player0 = pygame.sprite.GroupSingle(Player0())
                    player_num = 0
                    # screen.blit(kill, (375, 40))

                    time_healing_potion = time_healing_potion - 1
                    time_poison_flask = time_poison_flask - 1
                    time_giant_spider = time_giant_spider - 1
                    time_Dragon = time_Dragon - 1
                    defense = defense - 1
                    kill = True
                    # random+ skeleton_HP / 3
                    random_num = 2
    if defance_button.draw(screen):
        sleep(0.5)
        player_num = 2
        if random_num == 0:
            player_num = 2
            if speed > zombie_speed and defense < 5:
                HP = HP + 10
                player1.sprite.get_health(10)
                defense = defense + 1
            else:
                HP = HP - zombie_strange
                player1.sprite.get_damage(zombie_strange)
                if HP <= 0:  # die
                    player0 = 12
                    player1 = 14
                    start_button = button.Button(150, 402, start_img, 0.8)
                    exit_button = button.Button(150, 502, exit_img, 0.8)
                    attack_button = button.Button(1395, 395, attack_img, 0.8)
                    defance_button = button.Button(31195, 145, defance_img, 0.8)
                    # starting statistics
                    HP = 50
                    strange = 20
                    speed = 0.8
                    lvl = 1
                    exp = 0
                    defense = 0
                    player_num = 1110
                    random_num = 1110
                    animation_num = 1110
                    background_num = 0
                    clock = pygame.time.Clock()
                    # HP
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70  # 3

                    # speed
                    zombie_speed = 0.5  # 0
                    skeleton_speed = 1.5  # 1
                    spider_speed = 3  # 3

                    # strange
                    zombie_strange = 8  # 0
                    skeleton_strange = 20  # 1
                    spider_strange = 30  # 3

                    # items
                    healing_potion_effect = "+25% speed and HP"  # 4
                    time_healing_potion = 8
                    poison_flask_effect = "-25% speed and HP"  # 5
                    time_poison_flask = 8
                    wooden_sword_effect = "strange + 10%"  # 6
                    time_wooden_sword = 0
                    iron_sword_effect = "strange + 30%"  # 7
                    time_iron_sword = 0

                    # bosses
                    giant_spider = "1st boss"  # 8
                    time_giant_spider = 5
                    Dragon = "2nd boss"  # 9
                    time_Dragon = 5
                    boss = 1
        if random_num == 1:
            player_num = 2
            if speed > skeleton_speed and defense < 5:
                HP = HP + 10
                player1.sprite.get_health(10)
                defense = defense + 1
            else:
                HP = HP - skeleton_strange
                player1.sprite.get_damage(skeleton_strange)
                if HP <= 0:  # die
                    player0 = 12
                    player1 = 14
                    start_button = button.Button(150, 402, start_img, 0.8)
                    exit_button = button.Button(150, 502, exit_img, 0.8)
                    attack_button = button.Button(1395, 395, attack_img, 0.8)
                    defance_button = button.Button(31195, 145, defance_img, 0.8)
                    # starting statistics
                    HP = 50
                    strange = 20
                    speed = 0.8
                    lvl = 1
                    exp = 0
                    defense = 0
                    player_num = 1110
                    random_num = 1110
                    animation_num = 1110
                    background_num = 0
                    clock = pygame.time.Clock()
                    # HP
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70  # 3

                    # speed
                    zombie_speed = 0.5  # 0
                    skeleton_speed = 1.5  # 1
                    spider_speed = 3  # 3

                    # strange
                    zombie_strange = 8  # 0
                    skeleton_strange = 20  # 1
                    spider_strange = 30  # 3

                    # items
                    healing_potion_effect = "+25% speed and HP"  # 4
                    time_healing_potion = 8
                    poison_flask_effect = "-25% speed and HP"  # 5
                    time_poison_flask = 8
                    wooden_sword_effect = "strange + 10%"  # 6
                    time_wooden_sword = 0
                    iron_sword_effect = "strange + 30%"  # 7
                    time_iron_sword = 0

                    # bosses
                    giant_spider = "1st boss"  # 8
                    time_giant_spider = 5
                    Dragon = "2nd boss"  # 9
                    time_Dragon = 5
                    boss = 1
        if random_num == 2:
            player_num = 2
            if speed > spider_speed and defense < 5:
                HP = HP + 10
                player1.sprite.get_health(10)
                defense = defense + 1
            else:
                HP = HP - spider_strange
                player1.sprite.get_damage(spider_strange)
                if HP <= 0:  # die
                    player0 = 12
                    player1 = 14
                    start_button = button.Button(150, 402, start_img, 0.8)
                    exit_button = button.Button(150, 502, exit_img, 0.8)
                    attack_button = button.Button(1395, 395, attack_img, 0.8)
                    defance_button = button.Button(31195, 145, defance_img, 0.8)
                    # starting statistics
                    HP = 50
                    strange = 20
                    speed = 0.8
                    lvl = 1
                    exp = 0
                    defense = 0
                    player_num = 1110
                    random_num = 1110
                    animation_num = 1110
                    background_num = 0
                    clock = pygame.time.Clock()
                    # HP
                    zombie_HP = 55  # 0
                    skeleton_HP = 70  # 1
                    spider_HP = 70  # 3

                    # speed
                    zombie_speed = 0.5  # 0
                    skeleton_speed = 1.5  # 1
                    spider_speed = 3  # 3

                    # strange
                    zombie_strange = 8  # 0
                    skeleton_strange = 20  # 1
                    spider_strange = 30  # 3

                    # items
                    healing_potion_effect = "+25% speed and HP"  # 4
                    time_healing_potion = 8
                    poison_flask_effect = "-25% speed and HP"  # 5
                    time_poison_flask = 8
                    wooden_sword_effect = "strange + 10%"  # 6
                    time_wooden_sword = 0
                    iron_sword_effect = "strange + 30%"  # 7
                    time_iron_sword = 0

                    # bosses
                    giant_spider = "1st boss"  # 8
                    time_giant_spider = 5
                    Dragon = "2nd boss"  # 9
                    time_Dragon = 5
                    boss = 1
    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
    try:
        player0.update()
        player1.update()
    except:
        None
    pygame.display.update()
    clock.tick(60)
pygame.quit()
