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

import pygame
from .RGB import*

class model_widget():

    def __init__(self,name="wieget",x=0,y=0,tipo="Text",angulo=0.0):
        self.tipos_widget ={"Text":"TEXT","Plot":"PLOT", "Image":"IMAGE"}
        
        self.name=name
        self.tipo=self.tipos_widget[tipo]
        self.x=x
        self.y=y
        self.pos = [self.x,self.y]
        self.angulo = angulo
        
    def set_angulo(self, angulo):
        self.angulo = angulo

    def set_name(self, name):
        self.name=name
        
    def set_pos(self,x,y):
        self.pos[0]=x
        self.x=x
        self.pos[1]=y
        self.y=y
        
    def set_x(self,x):
        self.x=x
        
    def set_y(self,y):
        self.y=y
        
    def get_pos(self):
        return self.pos
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_angulo(self):
        return self.angulo
    
    
class widget_text(model_widget):
    
    def __init__(self,screen,name,x,y,text,size=14,color = BLACK,angulo=0,antialias=0,back_color=WHITE,global_color=BLACK):
        model_widget.__init__(self,name,x,y,"Text",angulo)
        self.screen = screen
        self.msm=text
        self.color=color
        self.background=back_color
        self.global_color=global_color
        self.size=size
        self.bold=False
        self.italic=False
        self.antialias=antialias
        self.create_font()
        
        
    def create_font(self):
        self.font = pygame.font.Font(None,self.size) #Crea un objeto para las letras
        self.font.set_italic(self.italic)
        self.font.set_bold(self.bold)
        self.text = self.font.render(self.msm,self.antialias,self.color,self.background)
        self.rotated=pygame.transform.rotate(self.text,self.get_angulo())
        width,height = self.rotated.get_size()
        x=self.get_x()+width/2
        y=self.get_y()+height/2
        self.textpos = self.rotated.get_rect(center=(x,y))
        self.screen.blit(self.rotated,self.textpos)
        #self.font.set_italic(True)
        #self.pygame.update()
        
    def rotar(self,angulo):
        self.delete()
        self.set_angulo(angulo)
        self.rotated=pygame.transform.rotate(self.text,angulo)
        self.screen.blit(self.rotated,self.textpos)
               
    def move(self,x,y):
        self.delete()
        self.set_x(x)
        self.set_y(y)
        self.create_font()
        #width,height = self.rotated.get_size()
        #x=x+width/2
        #y=y+height/2
        #self.textpos = self.rotated.get_rect(center=(x,y))
        #self.screen.blit(self.rotated,self.textpos)
        
    def update(self):
        pygame.display.update()
            
    def set_text(self,text):
        self.delete()
        self.msm=text
        self.create_font()
        
    def set_color(self,color):
        self.delete()
        self.color=color
        self.create_font()
        
    def set_bold(self, bold):
        self.delete()
        self.bold=bold
        self.create_font()
        #self.font.set_bold(bold)
        
    def set_italic(self,italic):
        self.delete()
        self.italic=italic
        self.create_font()
        #self.create_font()
        #self.font.set_italic(italic)
        
    def set_background(self,color):
        self.delete()
        self.background=color 
        
    def set_size(self,size=14):
        self.delete()
        self.size=size
        self.create_font()
        
    def get_text(self):
        return self.msm
    
    def get_color(self):
        return self.color
    
    def get_bold(self):
        return self.font.get_bold()
    
    def get_italic(self):
        return self.font.get_italic
    
    def get_size(self):
        return self.size
    
    def delete(self):
        self.text = self.font.render(self.msm,self.antialias,self.global_color,self.global_color)
        self.rotated=pygame.transform.rotate(self.text,self.get_angulo())
        width,height = self.rotated.get_size()
        x=self.get_x()+width/2
        y=self.get_y()+height/2
        self.textpos = self.rotated.get_rect(center=(x,y))
        self.screen.blit(self.rotated,self.textpos)
        #self.msm=a
        #self.create_font()
        
    
    
class widget_imagen(model_widget):
    
    def __init__(self,screen,ruta,escala,name="IMAGE",x=0,y=0,angulo=0,background=WHITE):
        model_widget.__init__(self,name,x,y,"Image",angulo)
        self.screen=screen
        self.background=background
        self.ruta=ruta
        self.escala=escala
        self.load()
    
    def rotar(self):
        self.imagen=pygame.transform.rotate(self.imagen,self.get_angulo())
    
    def load(self):
        self.imagen=pygame.image.load(self.ruta)
        
    def scale(self):
        self.imagen=pygame.transform.scale(self.imagen,(self.escala[0],self.escala[1]))
        
    def move(self,x,y):
        self.set_x(x)
        self.set_y(y)
        self.update()
        
    def update(self):
        self.delete()
        self.screen.blit(self.imagen,(self.get_x(),self.get_y()))
        pygame.display.update()
        
    def delete(self):
        superficie=pygame.Surface((self.escala[0],self.escala[1]))
        superficie.fill(self.background)
        rotated=pygame.transform.rotate(superficie,self.get_angulo())
        self.screen.blit(superficie, (self.get_x(),self.get_y()))
        #A=rotated.get_rect()
        #rect=pygame.draw.rect(self.screen,BLACK,[self.get_x(), self.get_y(), A[2], A[3] ],0)
        #rotated=pygame.transform.rotate(rect,self.get_angulo())
        pygame.display.update()
        
    
