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


from .widget import*
from .RGB   import*

class sonda():
    def __init__(self,screen,name="Sonda 1"):
        self.screen=screen
        self.list_view={}
        self.name=name
        self.backcolor=WHITE
        
    def set_backcolor(self,color):
        self.backcolor=color
        

    def add_label(self, name, pos,text,size,color,fondo):
        label=widget_text(self.screen, name,pos[0],pos[1],text,size,color,back_color=fondo,global_color=self.backcolor)
        self.list_view[name]=label
        
    def add_imagen(self, name, ruta, escala,pos,angulo):
        imagen=widget_imagen(self.sreen, ruta,escala,name,pos[0],pos[1],angulo,self.backcolor)
        self.list_view[name]=imagen
        
    def set_text(self,name,text):
        a=self.list_view[name]
        a.set_text(text)
        a.update()
    
    def plantilla(self):
        self.add_label("TITLE",[50,0],self.name,50,RED1,WHITE)
        self.add_label("TEM",[0,60],"TEMP = ", 50,BLUE,WHITE)
        self.add_label("TEM_U",[260,60],chr(176)+"C",50,BLUE,WHITE)
        self.add_label("HUM",[0,120],"HUME = ", 50,BLUE,WHITE)
        self.add_label("TEM_U",[280,120],"%",50,BLUE,WHITE)
        self.add_label("VAL_TEM",[130,50],"23.5", 80,BLUE,WHITE)
        self.add_label("VAL_HUM",[130,110],"78.9",80,BLUE,WHITE)
