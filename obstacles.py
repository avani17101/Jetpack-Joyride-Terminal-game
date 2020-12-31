import scenes
import os
import people
import global_var
import global_funct
import random
import time
import obstacles

class obstacle(object):

    def __init__(self,x,y):
        
        self.__x = x
        self.__y = y


    def clear(self):
        
        for i in range(self.get_width()):
            for j in range(self.get_height()):
                global_var.scenery.scene_matrix[self.__y+i][self.__x+j] = " "
        del(self)   
    def get_posx(self):
        return self.__x
    def set_posx(self,x):
        self.__x = x
    def get_posy(self):
        return self.__y
    def check_bullet(self):
        for i in range(self.get_width()):
            for j in range(self.get_height()):
                if(">" in global_var.scenery.scene_matrix[self.__y+i][self.__x+j]):
                    self.clear()
                    return 1
        return 0

            
class magnet(obstacle):
    def __init__(self,x,y):
            obstacle.__init__(self,x,y)
            self.__magnet = [ [  '_', '_', ],
          [ '|', '|']]
            
            self.__width = 2
            
            self.__height = 2

    def get_height(self):
        return self.__height
    def get_width(self):
        return self.__width
    def get_magnet(self):
        return self.__magnet
            #magnet.create_magnet()
    def create_magnet(self):
        for i in range(self.__width):
            for j in range(self.__height):
                global_var.scenery.scene_matrix[self._obstacle__y+i][self._obstacle__x+j] = "\033[37m" + "\033[01m" + "\033[31m"+ self.__magnet[i][j]
            

class hbeam(obstacle):
    def __init__(self,x,y):
        obstacle.__init__(self,x,y)
        self.__hbeam = ['#','*','*','*','*','*','*','*','*','*','#']
        self.__width = len(self.__hbeam)
        
        self.__height = 1
        #magnet.create_magnet()
    def create_hbeam(self):
        for i in range(self.__width):
            global_var.scenery.scene_matrix[self._obstacle__y+i][self._obstacle__x] = "\033[37m" + "\033[93m"+ self.__hbeam[i]

    def get_height(self):
        return self.__height
    def get_width(self):
        return self.__width       


class vbeam(obstacle):
    def __init__(self,x,y):
        obstacle.__init__(self,x,y)
        self.__vbeam =          [['#'],
                                ['*'],
                                ['*'],
                                ['*'],
                                ['*'],
                                ['*'],
                                ['*'],
                                ['*'],
                                ['*'],
                                ['*'],
                                ['#']]
        self.__width = 1
        self.__height = len(self.__vbeam)

    def create_vbeam(self):
        for i in range(self.__width):
            for j in range(self.__height):
                global_var.scenery.scene_matrix[self._obstacle__y+i][self._obstacle__x+j] = "\033[37m" + "\033[93m"+ self.__vbeam[j][i]
    
    def get_height(self):
            return self.__height
    
    def get_width(self):
            return self.__width


class sbeam(obstacle):
    def __init__(self,x,y) :
        obstacle.__init__(self, x,y)
        self.__sbeam =  [       ['#',' ',' ',' ',' '],
                                [' ','*',' ',' ',' '],
                                [' ',' ','*',' ',' '],
                                [' ',' ',' ','*',' '],
                                [' ',' ',' ',' ','#']]
        self.__height = 5
        self.__width = 5
    
    def create_sbeam(self):
        for i in range(self.__width):
            for j in range(self.__height):
                global_var.scenery.scene_matrix[self._obstacle__y+i][self._obstacle__x+j] = "\033[37m" + "\033[93m"+ self.__sbeam[i][j]
    
    def get_height(self):
            return self.__height
    
    def get_width(self):
            return self.__width
    