import pygame
from settings import *
from button import Button
from game import Game

def start():
	global buttons, easyBtn, mediumBtn, hardBtn, main_surf, sc
	buttons = [easyBtn, mediumBtn, hardBtn]
	pygame.draw.rect(main_surf, (0, 0, 0), (int(WIDTH * 0.25), int(HEIGHT * 0.3), int(WIDTH * 0.5), int(HEIGHT * 0.4)))
	for i in buttons:
		i.render()
	sc.blit(main_surf, (0, 0))
	pygame.display.update()

def resetButtons():
	global buttons
	buttons = [startBtn, exitBtn]
	pygame.draw.rect(main_surf, (0, 0, 0), (int(WIDTH * 0.25), int(HEIGHT * 0.3), int(WIDTH * 0.5), int(HEIGHT * 0.4)))
	for i in buttons:
		i.render()

def easy():
	g = Game(5, 3, 4)
	g.play()
	resetButtons()

def medium():
	g = Game(5, 5, 5)
	g.play()
	resetButtons()

def hard():
	g = Game(5, 6, 7)
	g.play()
	resetButtons()

main_surf = pygame.Surface((720, 1450))
startBtn = Button(main_surf, 200, int(HEIGHT * 0.4), "Играть", 32, command=start, width= 320)
easyBtn = Button(main_surf, 200, int(HEIGHT * 0.35), "Легко", 32, command=easy, width=320)
mediumBtn = Button(main_surf, 200, int(HEIGHT * 0.45), "Нормально", 32, command=medium, width=320)
hardBtn = Button(main_surf, 200, int(HEIGHT * 0.55), "Сложно", 32, command=hard, width=320)
exitBtn = Button(main_surf, 200, int(HEIGHT * 0.5), "Выход", 32, command=pygame.quit, width=320)
buttons = [startBtn, exitBtn]
startBtn.render()
exitBtn.render()
sc.blit(main_surf, (0, 0))
pygame.display.update()

while True:
        for i in pygame.event.get():
                if i.type == pygame.MOUSEBUTTONDOWN:
                        for i in buttons:
                                if i.in_rect(*pygame.mouse.get_pos()):
                                        flash_surf = pygame.Surface((int(WIDTH * 0.5), int(HEIGHT * 0.5)))
                                        flash_surf.fill((0, 0, 0))
                                        flash_surf.set_alpha(0)
                                        for j in range(80):
                                                flash_surf.set_alpha(j)
                                                sc.blit(flash_surf, (int(WIDTH * 0.25), int(HEIGHT * 0.3)))
                                                pygame.display.update()
                                                clock.tick(60)
                                        i.command()
                                        sc.blit(main_surf, (0, 0))
                                        pygame.display.update()
                elif i.type == pygame.QUIT:
                        pygame.quit()
        clock.tick(60)
