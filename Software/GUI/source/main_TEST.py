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

import os
import sys
import time
import pygame

from .widget import *

from .RGB import *



os.environ["SDL_FBDEV"] = "/dev/fb0"
os.environ['SDL_VIDEODRIVER']="fbcon"


class screen():
    
    def __init__(self,path):
        #super(screen, self).__init__()
        self.path=path
        pygame.init()
        self.screen = pygame.display.set_mode((320,240))
        self.backcolor=WHITE
        self.screen.fill(self.backcolor)
        pygame.mouse.set_visible(False)
        
        """(screen, nombre del label, posx,posy,texto a dibujar,color del texto,angulo, antialias,fodo del label, fondo de la pantalla)"""
        self.view=widget_text(self.screen,"text1",100,0,"a  marlon",40,RED1,0,0,BLUE,self.backcolor)
        self.view.update()
        pygame.time.wait(3000) 
        self.view.set_text("hola mundo")
        self.view.rotar(-45)
        self.view.set_size(35)
        self.view.set_color(BLACK)
        self.view.set_bold(True)
        self.view.set_italic(True)
        #self.view.set_text("marl on")
        #self.view.delete()
        self.view.update()
        
        pygame.time.wait(3000) 
        self.view.rotar(45)
        self.view.move(200,100)
        self.view.update()
        pygame.time.wait(3000) 
        self.view.delete()
        self.imagen=widget_imagen(self.screen,self.path+"/imagenes/ECOTEC.png",[200,200],"IMAGEN_1",angulo=45,background=self.backcolor)
        self.imagen.rotar()
        self.imagen.scale()
        self.imagen.update()
        pygame.time.wait(3000) 
        
        #self.imagen.move(30,40)
        #pygame.time.wait(3000) 
        
        self.imagen.delete()
        pygame.time.wait(3000) 
        #pygame.draw.rect(self.screen,BLACK,[55, 50, 100, 150],0)
        #pygame.display.flip()
        #print("rect")
        #pygame.time.wait(3000) 
        #self.view.displaytext("FrosTool",40,[0,200],[0,0,255],True)
        
        
    
        
        
        
        
