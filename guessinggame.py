import pygame
import sys  # system
import os
screen_width = 489
screen_height = 645
surface = pygame.display.set_mode((screen_width, screen_height))


def binary_search(arr):
    low = 0
    high = len(arr) - 1
    mid = 0
    text_B = pygame.font.SysFont('sans serif', 40)
    while low <= high:
        surface.fill((255, 158, 54))
        mid = (high + low) // 2

        text = text_B.render("If your number is " +
                             str(arr[mid])+" press Y", True, (0, 0, 0))
        surface.blit(text, (10, 100))

        text = text_B.render(
            "If your number is greater than ", True, (0, 0, 0))
        surface.blit(text, (10, 300))
        text = text_B.render(str(arr[mid]) + " press G", True, (0, 0, 0))
        surface.blit(text, (10, 350))

        text = text_B.render("If your number is less than ", True, (0, 0, 0))
        surface.blit(text, (10, 500))
        text = text_B.render(str(arr[mid])+" press L", True, (0, 0, 0))
        surface.blit(text, (10, 550))

        pygame.display.update()
        test = True
        while test:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        surface.fill((59, 24, 84))
                        text = text_B.render(
                            "HAHA I Figured out your number!!", True, (255, 255, 255))
                        surface.blit(text, (20, 200))
                        text = text_B.render(
                            "Your number was "+str(arr[mid])+" wasn't it ;)", True, (255, 255, 255))
                        surface.blit(text, (20, 400))
                        pygame.display.update()
                    elif event.key == pygame.K_g:
                        low = mid + 1
                        test = False
                    elif event.key == pygame.K_l:
                        high = mid - 1
                        test = False
    while True:
        surface.fill((59, 24, 84))
        text = text_B.render(
            "HAHA I Figured out your number!!", True, (255, 255, 255))
        surface.blit(text, (20, 200))
        text = text_B.render(
            "Your number was "+str(arr[mid])+" wasn't it ;)", True, (255, 255, 255))
        surface.blit(text, (20, 400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


arr = []
for i in range(0, 200):
    arr.append(i)


def starting():
    pygame.init()
    global surface
    global arr
    FileDir = os.path.dirname(os.path.abspath(__file__))

    #caption and icon
    pygame.display.set_caption("Magic Guessing Game")
    icon_image = os.path.join(FileDir, "hulogo.jpg")
    s_icon = pygame.image.load(icon_image)
    pygame.display.set_icon(s_icon)  # for the icon

    # start image
    cover_image = os.path.join(FileDir, "magic.png")
    cover = pygame.image.load(cover_image)
    surface.blit(cover, [0, 0])
    pygame.display.flip()

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    surface.fill((59, 24, 84))
                    pygame.display.update()
                    binary_search(arr)


starting()
