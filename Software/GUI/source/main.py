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

from .sonda import sonda

from .RGB import *
 


os.environ["SDL_FBDEV"] = "/dev/fb0"
os.environ['SDL_VIDEODRIVER']="fbcon"


class screen():
    
    def __init__(self,path):
        #super(screen, self).__init__()
        self.path=path
        pygame.init()
        self.screen = pygame.display.set_mode((320,240))
        self.backcolor=WHITE        #es el colo de fondo por defecto para todas las inicializaciones
        self.screen.fill(self.backcolor)
        pygame.mouse.set_visible(False)

        sond=sonda(self.screen,"SONDA NORTE")
        sond.plantilla()
        pygame.display.flip()
        pygame.time.wait(3000) 
        sond.set_text("VAL_TEM","18.2")
        pygame.time.wait(3000) 
    
