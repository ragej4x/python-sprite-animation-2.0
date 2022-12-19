#python 3.10

import pygame as pg
import animation


pg.init()


#WINDOW//DISPLAY
width,height = 600,400
display = pg.display.set_mode((width,height))
#CREATING SURFACE FOR RENDER SCALING
window_surface = pg.Surface((400,400))

pg.display.set_caption("animation 2.0")
fps = pg.time.Clock()


#VAR
loop = True
triger = False
def event_handler():
    global loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False
    

    surface = pg.transform.scale(window_surface,(width,height))
    display.blit(surface,(0,0))

    
    pg.display.flip()
    #RUNNING AT 60 FRAMES
    fps.tick(60)

while loop == True:
    window_surface.fill((100,100,100))
    

    
    #user input then update the frame
    keyinput = pg.key.get_pressed()
    if keyinput[pg.K_q]:
        triger = True
    if triger == True:
        animation.animate.frame += 0.2
    if animation.animate.frame >= 6:
        triger = False
        animation.animate.frame = 0
    #calling the class function on loop
    animation.animate.update(pg, window_surface)
    

    event_handler()



