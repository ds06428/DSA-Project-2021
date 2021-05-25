import random
import pygame
import sys  # system
import os
import time


screenwidth = 650
screenheight = 650
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gold = (239, 229, 51)


def change():
    FileDir = os.path.dirname(os.path.abspath(__file__))
    cover_image = os.path.join(FileDir, "secscreen.jpg")
    cover = pygame.image.load(cover_image)
    #surface.fill((255, 255, 255))
    surface.blit(cover, [0, 0])
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    import Hanoi

                if event.key == pygame.K_2:
                    import codeforgame

                if event.key == pygame.K_3:
                    import guessinggame


def dijkstra(frm):
    to = "HUGD"
    graph = {'DHA': [('Gulberg', 5), ('Gulshan', 3), ('HUGD', 6)], 'Gulberg': [('DHA', 5), ('PECHS', 6)], 'PECHS': [('Gulberg', 6), ('Gulshan', 10), ('Sadar', 2)], 'Gulshan': [
        ('DHA', 3), ('PECHS', 10), ('Hasan Square', 8)], 'HUGD': [('DHA', 6), ('Hasan Square', 9)], 'Hasan Square': [('Gulshan', 8), ('HUGD', 9), ('Sadar', 10)], 'Sadar': [('PECHS', 2), ('Hasan Square', 10)]}
    shortestdist = {}
    parents = {}
    shortestpath = []

    for i in graph.keys():
        shortestdist[i] = 10**10
    shortestdist[frm] = 0

    while graph.keys():

        x = None

        for i in graph.keys():
            if x is None:
                x = i
            elif shortestdist[i] < shortestdist[x]:
                x = i

        for j in graph[x]:
            if shortestdist[x] + j[1] < shortestdist[j[0]]:
                shortestdist[j[0]] = shortestdist[x] + j[1]
                parents[j[0]] = x

        del graph[x]

    node = to

    while node != frm:
        shortestpath.append((parents[node], node))
        node = parents[node]

    if shortestdist[to] != 10**10:
        catch = shortestpath[::-1]
        # return catch
    lst = []
    for i in range(len(catch)):
        lst.append(catch[i][0])
    # lst.append(to)
    strg = ""
    for i in lst:
        strg += i+"-->"
    strg += to
    return strg


def directions():
    d_screen_width = 650
    d_screen_height = 700
    pygame.init()  # initialization
    global surface
    surface = pygame.display.set_mode((d_screen_width, d_screen_height))
    FileDir = os.path.dirname(os.path.abspath(__file__))

    map = os.path.join(FileDir, "map.jpg")
    map = pygame.image.load(map)
    surface.fill((255, 255, 255))
    surface.blit(map, [0, 0])

    #caption and icon
    pygame.display.set_caption("Directions to HU Game Depo")
    icon_image = os.path.join(FileDir, "hulogo.jpg")
    s_icon = pygame.image.load(icon_image)
    pygame.display.set_icon(s_icon)  # for the icon
    c = True

    # EDGES
    pygame.draw.line(surface, (0, 0, 0), (90, 200),
                     (190, 50), 4)  # ------>HU to DHA

    # -----> HU to Hasan Sqr.
    pygame.draw.line(surface, (0, 0, 0), (90, 200), (190, 350), 4)

    pygame.draw.line(surface, (0, 0, 0), (190, 50),
                     (315, 200), 4)  # -----> DHA to GULSHAN

    # -------> Hasan Sqr. to Gulsahn
    pygame.draw.line(surface, (0, 0, 0), (190, 350), (315, 200), 4)

    # -------> Hasan Sqr to Saddar
    pygame.draw.line(surface, (0, 0, 0), (190, 350), (440, 350), 4)

    pygame.draw.line(surface, (0, 0, 0), (440, 350),
                     (540, 200), 4)  # -------> Saddar To PECHS

    pygame.draw.line(surface, (0, 0, 0), (315, 200),
                     (540, 200), 4)  # --------> Gulshan to PECHS

    pygame.draw.line(surface, (0, 0, 0), (440, 50),
                     (190, 50), 4)  # -----> Gulberg to DHA

    pygame.draw.line(surface, (0, 0, 0), (440, 50),
                     (540, 200), 4)  # -----> Gulberg to pechs

    # VERTICES

    # DHA
    DHA = pygame.draw.circle(surface, (82, 198, 247), (190, 50), 40)
    DHAn = pygame.font.SysFont('Corbel', 35)
    text = DHAn.render("DHA", True, (0, 0, 0))
    surface.blit(text, (190-35, 50-15))

    # HU GAME DEPOT
    HU = pygame.draw.circle(surface, (82, 198, 247), (90, 200), 40)
    HUn = pygame.font.SysFont('Corbel', 30)
    text = HUn.render("HUGD", True, (0, 0, 0))
    surface.blit(text, (90-38, 200-15))

    # HASAN SQUARE
    hasan_square = pygame.draw.circle(
        surface, (82, 198, 247), (190, 350), 40)
    hsn = pygame.font.SysFont('Corbel', 30)
    text = hsn.render("Hasan", True, (0, 0, 0))
    surface.blit(text, (190-38, 350-23))
    text = hsn.render("Sqr.", True, (0, 0, 0))
    surface.blit(text, (190-20, 350+10))

    # GULBERG
    gulberg = pygame.draw.circle(surface, (82, 198, 247), (440, 50), 40)
    gun = pygame.font.SysFont('Corbel', 25)
    text = gun.render("Gulberg", True, (0, 0, 0))
    surface.blit(text, (440-38, 50-15))

    # GULSHAN
    gulshan = pygame.draw.circle(surface, (82, 198, 247), (315, 200), 40)
    gln = pygame.font.SysFont('Corbel', 25)
    text = gln.render("Gulshan", True, (0, 0, 0))
    surface.blit(text, (315-38, 200-15))

    # PECHS
    PECHS = pygame.draw.circle(surface, (82, 198, 247), (540, 200), 40)
    pen = pygame.font.SysFont('Corbel', 27)
    text = pen.render("PECHS", True, (0, 0, 0))
    surface.blit(text, (540-38, 200-15))

    # SADAR
    sadar = pygame.draw.circle(surface, (82, 198, 247), (440, 350), 40)
    san = pygame.font.SysFont('Corbel', 30)
    text = san.render("Sadar", True, (0, 0, 0))
    surface.blit(text, (440-35, 350-15))

    # ALL THE BUTTONS
    stan = pygame.font.SysFont('Corbel', 30)
    DHA = stan.render("DHA", True, (0, 0, 0))
    back = stan.render("Exit", True, (0, 0, 0))
    Hasan = stan.render("Hasan Sqr", True, (0, 0, 0))
    gulshan = stan.render("Gulshan", True, (0, 0, 0))
    Saddar = stan.render("Saddar", True, (0, 0, 0))
    Pechs = stan.render("PECHS", True, (0, 0, 0))
    gulberg = stan.render("Gulberg", True, (0, 0, 0))

    pygame.draw.rect(surface, (161, 241, 255), [80, 430, 140, 40])
    surface.blit(DHA, (80, 430))
    pygame.draw.rect(surface, (161, 241, 255), [80, 510, 140, 40])
    surface.blit(Saddar, (80, 510))

    pygame.draw.rect(surface, (161, 241, 255), [250, 430, 140, 40])
    surface.blit(Hasan, (250, 430))
    pygame.draw.rect(surface, (161, 241, 255), [250, 510, 140, 40])
    surface.blit(gulshan, (250, 510))
    pygame.draw.rect(surface, (161, 241, 255), [250, 590, 140, 40])
    surface.blit(back, (250, 590))

    pygame.draw.rect(surface, (161, 241, 255), [420, 430, 140, 40])
    surface.blit(Pechs, (420, 430))
    pygame.draw.rect(surface, (161, 241, 255), [420, 510, 140, 40])
    surface.blit(gulberg, (420, 510))

    pygame.display.flip()
    c = True
    while c == True:
        p = "Please select an area"
        mousepos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 80 <= mousepos[0] <= 80+140 and 430 <= mousepos[1] <= 430+40:
                p = dijkstra("DHA")
                # print(p)
            if 80 <= mousepos[0] <= 80+140 and 510 <= mousepos[1] <= 510+40:
                p = dijkstra("Sadar")

            if 250 <= mousepos[0] <= 250+140 and 430 <= mousepos[1] <= 430+40:
                p = dijkstra("Hasan Square")
            if 250 <= mousepos[0] <= 250+140 and 510 <= mousepos[1] <= 510+40:
                p = dijkstra("Gulshan")
            if 250 <= mousepos[0] <= 250+140 and 590 <= mousepos[1] <= 590+40:
                pygame.quit()

            if 420 <= mousepos[0] <= 420+140 and 430 <= mousepos[1] <= 430+40:
                p = dijkstra("PECHS")
            if 420 <= mousepos[0] <= 420+140 and 510 <= mousepos[1] <= 510+40:
                p = dijkstra("Gulberg")

            if p != "Please select an area":
                c = False
    gln = pygame.font.SysFont('Corbel', 25)
    text = gln.render("The shortest Path is "+p, True, (0, 0, 0))
    surface.blit(text, (70, 650))
    pygame.display.update()
    while True:
        mousepos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 250 <= mousepos[0] <= 250+140 and 590 <= mousepos[1] <= 590+40:
                main()


def main():
    pygame.init()  # initialization
    global surface
    surface = pygame.display.set_mode((screenwidth, screenheight))
    clock = pygame.time.Clock()
    FileDir = os.path.dirname(os.path.abspath(__file__))

    #caption and icon
    pygame.display.set_caption("HU Game Depo")
    icon_image = os.path.join(FileDir, "hulogo.jpg")
    s_icon = pygame.image.load(icon_image)
    pygame.display.set_icon(s_icon)  # for the icon

    cover_image = os.path.join(FileDir, "arcade.png")
    cover = pygame.image.load(cover_image)
    #surface.fill((255, 255, 255))
    surface.blit(cover, [0, 0])
    pygame.display.flip()

    height = 400
    width = 225
    height2 = 500
    width2 = 225
    textcolor = (225, 225, 225)
    # light shade of the button
    color_light = (65, 105, 225)

    # dark shade of the button
    color_dark = (2, 0, 145)

    smallfont = pygame.font.SysFont('Corbel', 35)
    smallfont2 = pygame.font.SysFont('Corbel', 35)

    # rendering a text written in
    # this font
    text = smallfont.render("Enter", True, textcolor)
    text2 = smallfont2.render("Directions", True, textcolor)
    c = True
    while c == True:
        mousepos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button the game is terminated
                if width <= mousepos[0] <= width+150 and height <= mousepos[1] <= height+50:
                    change()

                if width2 <= mousepos[0] <= width2+150 and height2 <= mousepos[1] <= height2+50:
                    directions()

        if width <= mousepos[0] <= width+150 and height <= mousepos[1] <= height+50:
            pygame.draw.rect(surface, color_light, [width, height, 150, 50])

        else:
            pygame.draw.rect(surface, color_dark, [width, height, 150, 50])

        # superimposing the text onto our button
        surface.blit(text, (width+40, height+10))

        if width2 <= mousepos[0] <= width2+150 and height2 <= mousepos[1] <= height2+50:
            pygame.draw.rect(surface, color_light, [width2, height2, 150, 50])

        else:
            pygame.draw.rect(surface, color_dark, [width2, height2, 150, 50])

        surface.blit(text2, (width2+5, height2+10))

        pygame.display.update()


print("start")
main()
