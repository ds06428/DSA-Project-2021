import pygame, sys, time 

pygame.init()
width = 640
height = 500
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Towers of Hanoi")
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gold = (239, 229, 51)

n_disks = 3
disks = []

steps = 0

towers_midx = [120, 320, 520]
pointing_at = 0
floating = False
floater = 0

framerate = 60

display.fill(white)
closed = False

def display_text(display, text, midtop, aa=True, font=None, font_name = None, size = None, color=(255,0,0)):
    if font is None:                                   
        font = pygame.font.SysFont(font_name, size)     
    font_surface = font.render(text, aa, color)
    font_rect = font_surface.get_rect()
    font_rect.midtop = midtop
    display.blit(font_surface, font_rect)

def start_display():
    global display, n_disks, closed
    start_done = False
    while not start_done:
        display.fill(white)
        display_text(display, 'Towers of Hanoi', (320,120), font_name='sans serif', size=90, color=black)
        display_text(display, 'To move a disk first press the up key to lift it', (320, 280), font_name='sans_serif', size=30, color=black)
        display_text(display, 'Use the left or right to postion it on the required tower', (320, 310), font_name='sans_serif', size=30, color=black)
        display_text(display, 'Press the down key to place the disk', (320, 340), font_name='sans_serif', size=30, color=black)
        display_text(display, 'Press ENTER to continue', (320, 370), font_name='sans_serif', size=30, color=black)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_done = True
        pygame.display.flip()                    
    
def win_display(): 
    global display, steps
    display.fill(white)
    min_steps = 2**n_disks-1
    display_text(display, 'You Won!', (320, 200), font_name='sans serif', size=72, color=gold)
    display_text(display, 'Your Steps: '+str(steps), (320, 360), font_name='mono', size=30, color=black)
    display_text(display, 'Minimum Steps: '+str(min_steps), (320, 390), font_name='mono', size=30, color=red)
    if min_steps==steps:
        display_text(display, 'You finished in minumum steps!', (320, 300), font_name='mono', size=26, color=green)
    pygame.display.flip()
    time.sleep(2)    
    pygame.quit()   
    sys.exit()

def draw_towers():
    global display
    for xpos in range(40, 460+1, 200):
        pygame.draw.rect(display, green, pygame.Rect(xpos, 400, 160 , 20))
        pygame.draw.rect(display, black, pygame.Rect(xpos+75, 200, 10, 200))
    display_text(display, 'Tower 1', (towers_midx[0], 403), font_name='mono', size=14, color=black)
    display_text(display, 'Tower 3', (towers_midx[2], 403), font_name='mono', size=14, color=black)

def make_disks():
    global n_disks, disks
    disks = []
    height = 20
    ypos = 397 - height
    width = n_disks * 23
    for i in range(n_disks):
        disk = {}
        disk['rect'] = pygame.Rect(0, 0, width, height)
        disk['rect'].midtop = (120, ypos)
        disk['val'] = n_disks-i
        disk['tower'] = 0
        disks.append(disk)
        ypos -= height+3
        width -= 23

def draw_disks():
    global display, disks
    for disk in disks:
        pygame.draw.rect(display, blue, disk['rect'])
    return

def draw_ptr():
    ptr_points = [(towers_midx[pointing_at]-7 ,440), (towers_midx[pointing_at]+7, 440), (towers_midx[pointing_at], 433)]
    pygame.draw.polygon(display, red, ptr_points)
    return

def check_won():
    global disks
    over = True
    for disk in disks:
        if disk['tower'] != 2:
            over = False
    if over:
        time.sleep(0.2)
        win_display()    

start_display()
make_disks()
while not closed:
    display.fill(white)
    draw_towers()
    draw_disks()
    draw_ptr()
    display_text(display, 'Steps: '+str(steps), (320, 20), font_name='mono', size=30, color=black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                closed = True
            if event.key == pygame.K_RIGHT:
                pointing_at = (pointing_at+1)%3
                if floating:
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 100)
                    disks[floater]['tower'] = pointing_at
            if event.key == pygame.K_LEFT:
                pointing_at = (pointing_at-1)%3
                if floating:
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 100)
                    disks[floater]['tower'] = pointing_at
            if event.key == pygame.K_UP and not floating:
                for disk in disks[::-1]:
                    if disk['tower'] == pointing_at:
                        floating = True
                        floater = disks.index(disk)
                        disk['rect'].midtop = (towers_midx[pointing_at], 100)
                        break
            if event.key == pygame.K_DOWN and floating:
                for disk in disks[::-1]:
                    if disk['tower'] == pointing_at and disks.index(disk)!=floater:
                        if disk['val']>disks[floater]['val']:
                            floating = False
                            disks[floater]['rect'].midtop = (towers_midx[pointing_at], disk['rect'].top-23)
                            steps += 1
                        break
                else: 
                    floating = False
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 400-23)
                    steps += 1
            if event.type == pygame.QUIT:
                closed = True
    pygame.display.flip()
    if not floating:check_won()
    clock.tick(framerate)
pygame.quit()
