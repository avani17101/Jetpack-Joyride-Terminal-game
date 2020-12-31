import config
import global_var
import global_funct
import random
import os
import scenes
import math
from colorama import init, Fore, Back, Style
import people
class Bullet(object):
    def __init__(self, x, y, drago):

        self.__posx = x
        self.__posy = y
        self.__bullet =  ">"
        self.__width = 1
        self.drago = drago
    def get_posx(self):
        return self.__posx
    def set_posx(self,posx):
        self.__posx = posx  
    def get_posy(self):
        return self.__posy
    def set_posy(self,posy):
        self.__posy = posy 

    def move_right(self):
        #while(self.__posx!= 1198):
        if '*' in global_var.scenery.scene_matrix[self.__posy][self.__posx+1]:   #
            global_var.scenery.scene_matrix[self.__posy][self.__posx+1] ="\033[33m" + "\033[45m" + " "  
            #while()
            return
        self.clear()
        self.__posx += 1
        self.render()
        #del(self)

    def check_collision(self):
        if(global_var.scenery.scene_matrix[self.__posy][self.__posx] == "\033[37m" + "\033[01m" + "\033[31m"+"-" or global_var.scenery.scene_matrix[self.__posy][self.__posx] == "\033[37m" + "\033[93m"+ "#" or global_var.scenery.scene_matrix[self.__posy][self.__posx] == "\033[37m" + "\033[93m"+ "*"):
            return 1
        return 0
    def __del__(self):
        self.clear()

    def get_width(self):
        return self.__width
    def render(self):
        global_var.scenery.scene_matrix[self.__posy][self.__posx] = "\033[32m" + "\033[40m" + "\033[1m" + self.__bullet

    def clear(self):
        for i in range(self.__width):
            if self.__posx <= global_var.scenery.scene_length-int(config.columns/2) - 1:
                global_var.scenery.scene_matrix[self.__posy][i+self.__posx] = "\033[37m" + "\033[40m" + " "
            else:
                global_var.scenery.scene_matrix[self.__posy][i+self.__posx] = "\033[37m" + "\033[40m" + " "
class iceballs(object):
    def __init__(self, posx,posy,dx,dy,din):
        self.__dx = dx
        self.__dy = dy
        self.__posx = posx
        self.__posy = posy
        self.__iceballs = "0"
        self.__width = 1
        self.__height = 1
        self.din = din
        #print(din)
        self.dinwidth = len(din[0])
        self.dinheight = len(din)
        #print(self.dinwidth,self.dinheight)
        
    def check_collision(self):
        if(global_var.scenery.scene_matrix[self.__posy][self.__posx] == "\033[37m" + "\033[01m" + "\033[31m"+"-" or global_var.scenery.scene_matrix[self.__posy][self.__posx] == "\033[37m" + "\033[93m"+ "#" or global_var.scenery.scene_matrix[self.__posy][self.__posx] == "\033[37m" + "\033[93m"+ "*"):
            return 1
        return 0



    def move_left(self):
            if global_var.scenery.scene_matrix[self.__posy][self.__posx-1] == "\033[33m" + "\033[45m" + " ":
                return
            self.clear()
            self.__posx -= 1
            self.render()
        # self.clear()
        # self.render()
    
    def __del__(self):
        self.clear()
    def get_height(self):
        return self.__height
    def get_width(self):
        return self.__width
        
    def render(self):
            global_var.scenery.scene_matrix[self.__posy][self.__posx] = '\033[34m' + '\033[47m'+ "\033[1m" + self.__iceballs
    def check_collision(self):
        if(global_var.scenery.scene_matrix[self.__posy][self.__posx] == "\033[37m" + "\033[01m" + "\033[31m"+"-" or global_var.scenery.scene_matrix[self.__posy][self.__posx] == "\033[37m" + "\033[93m"+ "#" or global_var.scenery.scene_matrix[self.__posy][self.__posx] == "\033[37m" + "\033[93m"+ "*"):
            return 1
    def clear(self):

                #print(type(self.__posx),self.__posx)
                if self.__posx <= (1200-60 - 1):
                    global_var.scenery.scene_matrix[self.__posy][self.__posx] = "\033[37m" + "\033[40m" + " "
                else:
                    global_var.scenery.scene_matrix[self.__posy][self.__posx] = "\033[37m" + "\033[40m" + " "