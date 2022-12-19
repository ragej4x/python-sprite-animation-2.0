#############
#python 3.10#
#############

class animation_class():#CLASS
    def __init__(self):
        self.xpos = 130
        self.ypos = 200
        self.animation_l = []
        self.frame = 0

    def update(self, pg, window,):
        #LOADING AN IMAGE
        for num in range(1,5 + 1):
            image = pg.image.load(f"animation/atk_cmb_1 ({num}).anim")
            image = pg.transform.scale(image , (150,150))
            self.animation_l.append(image)
            window.blit(self.animation_l[int(self.frame)], (self.xpos , self.ypos))            



animate = animation_class()



#END OF CODE
