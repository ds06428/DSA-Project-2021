import pygame, sys, time #libraries used

pygame.init() #intitalises pygame
width = 640 #desired width of the game screen
height = 500 #desired height of the game screen
display = pygame.display.set_mode((width, height)) #creates the screen display
pygame.display.set_caption("Towers of Hanoi")
clock = pygame.time.Clock()
#colors used
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gold = (239, 229, 51)

n_disks = 3 #number of disks
disks = []

steps = 0 #used to keep track of the number of steps the user takes

towers_midx = [120, 320, 520] #midpoints for drawing towers
#pointer variables
pointing_at = 0
floating = False
floater = 0

framerate = 60

display.fill(white)
closed = False #used to check if the user wants to close the game

def display_text(display, text, midtop, aa=True, font=None, font_name = None, size = None, color=(255,0,0)): #function to display text on screen
    if font is None:   #used to make the code more efficent if the same font has to be reused                                 
        font = pygame.font.SysFont(font_name, size)     
    font_surface = font.render(text, aa, color)  #renders into text
    font_rect = font_surface.get_rect() #cretaes text rectangles for use
    font_rect.midtop = midtop #midpoint of the font
    display.blit(font_surface, font_rect) #updates the game display 

def start_display(): #function to display the start screen before the main game
    global display, n_disks, closed #calls the global variables
    start_done = False #variable to check if all the processes of the start menu are exectuted
    while not start_done:
        display.fill(white)
        #displays text
        display_text(display, 'Towers of Hanoi', (320,120), font_name='sans serif', size=90, color=black)
        display_text(display, 'To move a disk first press the up key to lift it', (320, 280), font_name='sans_serif', size=30, color=black)
        display_text(display, 'Use the left or right to postion it on the required tower', (320, 310), font_name='sans_serif', size=30, color=black)
        display_text(display, 'Press the down key to place the disk', (320, 340), font_name='sans_serif', size=30, color=black)
        display_text(display, 'Press ENTER to continue', (320, 370), font_name='sans_serif', size=30, color=black)
        for event in pygame.event.get(): #gets event logs
            # checks if  key pressed it enter
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_done = True
        pygame.display.flip() #updates the game display                    
    
def win_display(): #function to display the screen after winning
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

def draw_towers(): #fuction to draw the twoers where disks are placed
    global display
    for xpos in range(40, 461, 200): #loop to draw the horizontal base and vertical line for each tower. xpos is the x coordinate 
        pygame.draw.rect(display, green, pygame.Rect(xpos, 400, 160 , 20)) #drwas the base 
        pygame.draw.rect(display, black, pygame.Rect(xpos+75, 200, 10, 200)) #drwas the tower
    display_text(display, 'Tower 1', (towers_midx[0], 403), font_name='mono', size=14, color=black)
    display_text(display, 'Tower 3', (towers_midx[2], 403), font_name='mono', size=14, color=black)

def make_disks(): #dunction to define the elements of the sdiks
    global disks
    disks = []
    height = 20
    ypos = 397 - height
    width = 69
    for i in range(3):
        disk = {} #a dictionary to store the disk details
        disk['rect'] = pygame.Rect(0, 0, width, height) #disk heught and width
        disk['rect'].midtop = (120, ypos) #disk midpoint
        disk['val'] = 3-i #which disk is it
        disk['tower'] = 0 #which tower its on
        disks.append(disk) #add it to the list of disks
        ypos -= height+3
        width -= 23

def draw_disks():
    global display, disks
    for disk in disks:
        pygame.draw.rect(display, blue, disk['rect']) #draws the disk
    return

def draw_ptr(): #draws the pointer for towers
    ptr_points = [(towers_midx[pointing_at]-7 ,440), (towers_midx[pointing_at]+7, 440), (towers_midx[pointing_at], 433)] #three different pointer poistions
    pygame.draw.polygon(display, red, ptr_points)
    return

def check_won():
    global disks
    over = True
    for disk in disks: #checks if every disk is placed on tower two
        if disk['tower'] != 2: 
            over = False
    if over:
        time.sleep(0.2)
        win_display()    

start_display()
make_disks()
#main game loop
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
    if not floating:
        check_won()
    clock.tick(framerate)
pygame.quit()
