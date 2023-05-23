import pygame
import sys
import random
import time
import button

# starting statistics
HP = 100
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
_quit_ = False
game = False
# HP
zombie_HP = 50  # 0
skeleton_HP = 45  # 1

# speed
zombie_speed = 0.5  # 0
skeleton_speed = 1.5  # 1

# strange
zombie_strange = 8  # 0
skeleton_strange = 10  # 1


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


# pygame
# display
pygame.init()
screen = pygame.display.set_mode((645, 645))
pygame.display.set_caption("By steps(version 0.2)")
font = pygame.font.SysFont("Times new Roman", 40, bold=True)
background_normal = pygame.image.load(r"by steps\textures\background_normal.png")
background_hell = pygame.image.load(r"by steps\textures\background_hell.png")
background_cave = pygame.image.load(r"by steps\textures\background_cave.png")
player = pygame.image.load(r"by steps\textures\player.png")
player_attack = pygame.image.load(r"by steps\textures\player_attack.png")
player_defence = pygame.image.load(r"by steps\textures\player_defence.png")
zombie = pygame.image.load(r"by steps\textures\zombie.png")
skeleton = pygame.image.load(r"by steps\textures\skeleton.png")
health = pygame.image.load(r"by steps\textures\health.png")
# buttons
surf_button_quit = font.render("Quit", True, "white")
# button_quit = pygame.Rect(292, 565, 110, 60)
button_quit_image = pygame.image.load(
    r"by steps\textures\button_quit.png"
).convert_alpha()
button_quit = button.Button(177, 502, button_quit_image, 0.8)
# button_quit_image = pygame.image.load(r"by steps\textures\button_quit.png")

# surf_button_play = font.render("play", True, "white")
# button_play = pygame.Rect(292, 485, 110, 60)
button_play_image = pygame.image.load(
    r"by steps\textures\button_play.png"
).convert_alpha()
button_play = button.Button(177, 402, button_play_image, 0.8)

surf_button_attack = font.render("Attack", True, "white")
button_attack = pygame.Rect(1206, 240, 110, 60)
# button_attack_image = pygame.image.load(r"by steps\textures\button_attack.png")
surf_button_defence = font.render("Defence", True, "white")
button_defence = pygame.Rect(2186, 340, 110, 60)
# button_defence_image = pygame.image.load(r"by steps\textures\button_defence.png")
surf_button_HP = font.render("HP:" + str(HP), True, "white")
button_HP = pygame.Rect(2206, 2240, 110, 60)
surf_button_HP2 = font.render("HP:" + str(HP), True, "white")
button_HP2 = pygame.Rect(2406, 2240, 110, 60)
surf_button_text = font.render("Nothing", True, "white")
button_text = pygame.Rect(4206, 2240, 110, 60)
while True:
    a, b = pygame.mouse.get_pos()
    if background_num == 0:
        screen.blit(background_normal, (0, 0))
    if background_num == 1:
        screen.blit(background_cave, (0, 0))
    if background_num == 2:
        screen.blit(background_hell, (0, 0))
    # button quit
    if _quit_ == True:
        pygame.quit()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
    if button_quit.draw(screen):
        _quit_ = True
    # button play
    if button_play.draw(screen):
        game = True
    if game == True:
        # start game
        button_attack = pygame.Rect(490, 565, 125, 60)
        button_defence = pygame.Rect(490, 485, 140, 60)
        # button_play = pygame.Rect(1206, 142, 280, 60)
        button_play = button.Button(1010, 200, button_play_image, 0.8)
        button_quit = pygame.Rect(20, 20, 110, 60)
        button_HP = pygame.Rect(20, 565, 215, 60)
        button_HP2 = pygame.Rect(410, 20, 215, 60)
        # button_text = pygame.Rect(20, 60, 180, 60)
        player_num = 0
        random_num = 0
    # animation
    if player_num == 0:
        screen.blit(player, (-20, 192))
    if player_num == 1:
        screen.blit(player_attack, (-20, 192))
    if player_num == 2:
        screen.blit(player_defence, (-20, 192))
    if animation_num == 0:
        screen.blit(zombie, (370, 40))
    # if (
    #     button_play.x <= a <= button_play.x + 110
    #     and button_play.y <= b <= button_play.y + 60
    # ):
    #     pygame.draw.rect(gameDisplay, (110, 110, 110), button_play)

    # else:
    #     pygame.draw.rect(gameDisplay, (110, 110, 110), button_play)

    # gameDisplay.blit(surf_button_play, (button_play.x + 5, button_play.y + 5))

    if (
        button_attack.x <= a <= button_attack.x + 125
        and button_attack.y <= b <= button_attack.y + 60
    ):
        pygame.draw.rect(screen, (110, 110, 110), button_attack)
        if events.type == pygame.MOUSEBUTTONDOWN:
            if random_num == 0:
                player_num = 1
                time.sleep(0.1)
                animation_num = 0
                random_num = random.randint(0, 10)
                surf_button_text = font.render("Attack!", True, "white")
                attack_random = random.randint(0, 2)
                if attack_random == 0:
                    surf_button_text = font.render("U used!", True, "white")
                    attack_random = random.randint(0, 2)
                    zombie_HP -= strange

                    # health_bar.sprite.get_damage(8)
                    # if health_bar.sprite.target_health <= 0:  # die
                    if HP <= 0:
                        surf_button_text = font.render(
                            "You died! The zombie is so dangerous.", True, "white"
                        )
                        button_quit = pygame.Rect(267, 240, 110, 60)
                        # button_play = pygame.Rect(267, 170, 110, 60)
                        button_attack = pygame.Rect(1206, 240, 110, 60)
                        button_defence = pygame.Rect(2186, 340, 110, 60)
                        button_HP = pygame.Rect(2206, 2240, 110, 60)
                        button_HP2 = pygame.Rect(2406, 2240, 110, 60)
                        button_text = pygame.Rect(4206, 2240, 110, 60)
                        HP = 20
                        strange = 2
                        speed = 0.8
                        lvl = 1
                        exp = 0
                        defense = 0
                        player_num = 1110
                        random_num = 1110
                        animation_num = 1110
                    if zombie_HP <= 0:
                        time_healing_potion = time_healing_potion - 1
                        time_poison_flask = time_poison_flask - 1
                        time_giant_spider = time_giant_spider - 1
                        time_Dragon = time_Dragon - 1
                        defense = defense - 1
                        zombie_HP = 10
                        exp = exp + zombie_HP / 3
                        random_num = random.randint(0, 10)
                        surf_button_text = font.render(
                            "You killed zombie.", True, "white"
                        )
                        if exp >= lvl * 10:
                            exp = 0
                            lvl = lvl + 1
                            HP = 20
                            strange = strange + lvl / 1.5
                            speed = speed + lvl / 1.5
                            surf_button_text = font.render(
                                "You've got lvl " + str(lvl) + "!", True, "white"
                            )
                            break
                else:
                    surf_button_text = font.render("Zombie's faster!", True, "white")
                    attack_random = random.randint(0, 2)
                    zombie_HP -= strange / 3
                    HP -= zombie_strange
                    if HP <= 0:  # die
                        surf_button_text = font.render(
                            "You died! The zombie is so dangerous.", True, "white"
                        )
                        button_quit = pygame.Rect(267, 240, 110, 60)
                        button_play = pygame.Rect(267, 170, 110, 60)
                        button_attack = pygame.Rect(1206, 240, 110, 60)
                        button_defence = pygame.Rect(2186, 340, 110, 60)
                        button_HP = pygame.Rect(2206, 2240, 110, 60)
                        button_HP2 = pygame.Rect(2406, 2240, 110, 60)
                        button_text = pygame.Rect(4206, 2240, 110, 60)
                        HP = 20
                        strange = 2
                        speed = 0.8
                        lvl = 1
                        exp = 0
                        defense = 0
                        player_num = 1110
                        random_num = 1110
                        animation_num = 1110
                    if zombie_HP <= 0:
                        time_healing_potion = time_healing_potion - 1
                        time_poison_flask = time_poison_flask - 1
                        time_giant_spider = time_giant_spider - 1
                        time_Dragon = time_Dragon - 1
                        defense = defense - 1
                        zombie_HP = 10
                        exp = exp + zombie_HP / 3
                        surf_button_text = font.render(
                            "You killed zombie.", True, "white"
                        )
                        if exp >= lvl * 10:
                            exp = 0
                            lvl = lvl + 1
                            HP = 100
                            strange = strange + lvl / 1.5
                            speed = speed + lvl / 1.5
                            surf_button_text = font.render(
                                "You've got lvl " + str(lvl) + "!", True, "white"
                            )
                            break
            surf_button_HP = font.render("HP: " + str(int(HP)), True, "white")
            surf_button_HP2 = font.render("HP: " + str(int(zombie_HP)), True, "white")
            time.sleep(0.1)
            screen.blit(surf_button_HP, (button_HP.x + 5, button_HP.y + 5))
            screen.blit(surf_button_HP2, (button_HP2.x + 5, button_HP2.y + 5))

    screen.blit(surf_button_attack, (button_attack.x + 5, button_attack.y + 5))

    if (
        button_defence.x <= a <= button_defence.x + 140
        and button_defence.y <= b <= button_defence.y + 60
    ):
        pygame.draw.rect(screen, (110, 110, 110), button_defence)
        if events.type == pygame.MOUSEBUTTONDOWN:
            if random_num == 0:
                player_num = 2
                time.sleep(0.1)
                animation_num = 0
                surf_button_text = font.render("Defence!", True, "white")
                random_num = random.randint(0, 10)
                if speed > zombie_speed and defense < 5:
                    surf_button_text = font.render(
                        "You used to defense.", True, "white"
                    )
                    HP = HP + 1
                    defense = defense + 1
                else:
                    surf_button_text = font.render("Zombie's faster.", True, "white")
                    HP = HP - zombie_strange
                    if HP <= 0:  # die
                        surf_button_text = font.render(
                            "You died! The zombie is so dangerous.", True, "white"
                        )
                        button_quit = pygame.Rect(267, 240, 110, 60)
                        button_play = pygame.Rect(267, 170, 110, 60)
                        button_attack = pygame.Rect(1206, 240, 110, 60)
                        button_defence = pygame.Rect(2186, 340, 110, 60)
                        button_HP = pygame.Rect(2206, 2240, 110, 60)
                        button_HP2 = pygame.Rect(2406, 2240, 110, 60)
                        button_text = pygame.Rect(4206, 2240, 110, 60)
                        HP = 100
                        strange = 2
                        speed = 0.8
                        lvl = 1
                        exp = 0
                        defense = 0
                        player_num = 1110
                        random_num = 1110
                        animation_num = 1110
            surf_button_HP = font.render("HP: " + str(int(HP)), True, "white")
            surf_button_HP2 = font.render("HP: " + str(int(zombie_HP)), True, "white")
            time.sleep(0.1)
            screen.blit(surf_button_HP, (button_HP.x + 5, button_HP.y + 5))
            screen.blit(surf_button_HP2, (button_HP2.x + 5, button_HP2.y + 5))

    screen.blit(surf_button_defence, (button_defence.x + 5, button_defence.y + 5))

    if button_HP.x <= a <= button_HP.x + 215 and button_HP.y <= b <= button_HP.y + 60:
        pygame.draw.rect(screen, (110, 110, 110), button_HP)

    else:
        pygame.draw.rect(screen, (110, 110, 110), button_HP)

    screen.blit(surf_button_HP, (button_HP.x + 5, button_HP.y + 5))

    if (
        button_HP2.x <= a <= button_HP2.x + 215
        and button_HP2.y <= b <= button_HP2.y + 60
    ):
        pygame.draw.rect(screen, (110, 110, 110), button_HP2)

    else:
        pygame.draw.rect(screen, (110, 110, 110), button_HP2)

    screen.blit(surf_button_HP2, (button_HP2.x + 5, button_HP2.y + 5))

    if button_text.x <= a <= button_text.x and button_text.y <= b <= button_text.y:
        pygame.draw.rect(screen, (110, 110, 110), button_text)

    else:
        pygame.draw.rect(screen, (110, 110, 110), button_text)

    screen.blit(surf_button_text, (button_text.x + 5, button_text.y + 5))
    # health_bar.update()
    pygame.display.update()
    clock.tick(60)
