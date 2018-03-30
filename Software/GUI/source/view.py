#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Creation:    26.05.2013
# Last Update: 07.04.2015
#
# Copyright (c) 2013-2015 by Georg Kainzbauer <http://www.gtkdb.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#

from RGB import*


class view():
    
    def __init__(self, pygame, screen):
        
        self.pygame=pygame
        self.screen=screen
        self.color_background=WHITE
        
    def set_background(self,color):
        self.screen.fill(color)
        self.color_background=color   
        
    def delete(self)
        
    def imagen(self, imagen, escala,time):
        image = self.pygame.image.load(imagen)
        image = self.pygame.transform.scale(image, (escala[0],escala[1]))
        self.screen.blit(image, (0 , 0))
        self.pygame.display.update()
        self.pygame.time.wait(time)
        
    def displaytext(self,text,size,pos,color,clearscreen=False,antialias=False):
        posx=pos[0]
        posy=pos[1]
        if clearscreen:
            self.screen.fill(WHITE)

        font = self.pygame.font.Font(None,size) #Crea un objeto para las letras
        text = font.render(text,antialias,color)
        rotated = self.pygame.transform.rotate(text,0)
        width,height = rotated.get_size()
        posx=posx+width/2
        posy=posy+height
        textpos = rotated.get_rect(center=(posx,posy))
        #textpos.centery = 200,100
        self.screen.blit(rotated,textpos)
        self.pygame.display.update()
        self.pygame.time.wait(3000) 
 
