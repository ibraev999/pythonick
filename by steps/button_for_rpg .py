import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Button!")
main_font = pygame.font.SysFont("cambria", 50)


class Button:
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1
        ] in range(self.rect.top, self.rect.buttom):
            print("Button press!")

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1
        ] in range(self.rect.top, self.rect.buttom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "green")


button_surface = pygame.image.load(r"by steps\textures\health.png")
button_surface = pygame.transform.scale(button_surface, (400, 400))

button = Button(button_surface, 0, 0, "")

while True:
    a, b = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if 0 <= a and 0 <= b:
            if a <= 60 and b <= 60:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()

    screen.fill("white")

    button.update()
    button.changeColor = pygame.mouse.get_pos()
    pygame.display.update()
