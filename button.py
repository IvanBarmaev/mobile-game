import pygame

pygame.font.init()
class Button:
    def __init__(self, surf, x, y, text, size, command=None, description=None, width=None, height=None):
        self.font = pygame.font.SysFont("Lucida Console", size)
        self.description = description
        self.command = command
        self.surf = surf
        self.x = x
        self.y = y
        self.text = text
        self.txt = self.font.render(text, True, (10, 20, 30))
        self.rect = self.txt.get_rect(topleft=(x, y))
        self.rect.width += 10
        if width:
            self.rect.width = width
            self.width = width
        if height:
            self.rect.height = height
        else:
            self.rect.height += self.rect.height // 2

    def render(self, shift_y=0):
        pygame.draw.rect(self.surf, (200, 200, 200), (self.rect.x, self.rect.y + shift_y, self.rect.right-self.rect.left, self.rect.height))
        self.surf.blit(self.txt, (self.rect.x + self.rect.width // 2 - self.txt.get_rect().width // 2, self.rect.y + shift_y + self.rect.height // 12))

    def change_text(self, text):
        self.text = text
        self.txt = self.font.render(text, True, (10, 20, 30))
        self.rect = self.txt.get_rect(topleft=(self.x, self.y))
        self.rect.width = self.width
        self.rect.height += self.rect.height // 2

    def in_rect(self, x, y, shift_y=0):
         if x in range(self.rect.left, self.rect.right) and y in range(self.rect.y + shift_y, self.rect.y + self.rect.height + shift_y):
             return True
         return False

    def draw_rect(self, shift_y=0):
        pygame.draw.rect(self.surf, (255, 0, 0), (self.rect.x, self.rect.y + shift_y, self.rect.width, self.rect.height), 2)

    @classmethod  #Метод класса для получения высоты кнопки
    def get_height(cls, size):
        new_font = pygame.font.SysFont("Lucida Console", size)
        return int(new_font.render("hi", True, (0, 0, 0)).get_rect().height * 1.5)
