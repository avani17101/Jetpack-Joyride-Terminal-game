import config
import global_var
import global_funct
import random
import os
import scenes
import math
from colorama import init, Fore, Back, Style

class Person(object):

    """ Characters of the game """

    def __init__(self, x, y):
        self.__posx = x
        self.__posy = y
    def get_posx(self):
        return self.__posx
    def set_posx(self,posx):
        self.__posx = posx  
    def get_posy(self):
        return self.__posy
    def set_posy(self,posy):
        self.__posy = posy  


class din(Person):
    def __init__(self,x,y):
        Person.__init__(self,x,y)
        self.__ideal_din = [[" ", "@", " "],
                         ["/", "|", "\\"],
                         [" ", "|", " "],
                         ["/", " ", "\\"]]
        self.__din = self.__ideal_din
        self.__shielded_din = [
         ["|", "Q", "|"],
         ["/", "|", "\\"],
         [" ", "|", " "],
         ["/", " ", "\\"]]

        self.__height = 4
        self.__width = 3
        self.v = 0
        self.g = 1
        self.a = 0
        self.__lives = 100

    def get_din(self):
        return self.__din

    def get_lives(self):
        return self.__lives

    def shield(self):
        global_var.activated_shield = 1
        self.__din = self.__shielded_din

    def deshield(self):
        global_var.activated_shield = 0
        self.__din = self.__ideal_din 

    def collected_powerups(self):
        for i in range(self.__width-1,self.__width+1):
            for j in range(self.__height-1,self.__height+1):
                if("S" in global_var.scenery.scene_matrix[j+self._Person__posy][i+self._Person__posx]):
                    global_var.num_shield += 1
                    #print("Coolllll")
                if("B" in global_var.scenery.scene_matrix[j+self._Person__posy][i+self._Person__posx]):
                    global_var.speed *= 1/2
    
    def get_height(self):
            return self.__height
    
    def get_width(self):
            return self.__width
        
    #to check if __din is on ground
    def on_ground(self):
        if(self._Person__posy == global_var.scenery.ground_level - self.__height):
            return 1
    
    def die(self):
        #print(self._Person__posx, self._Person__posy)
        if(global_var.activated_shield!=1):
            #os.system('aplay mariodies.wav&')
            self.__lives -= 1
            global_var.lives -= 1
            self.clear()
            self._Person__posy = 5
        else:
            self.deshield()

    def render(self):
        for i in range(self.__width):
            for j in range(self.__height):
                global_var.scenery.scene_matrix[j+self._Person__posy][i+self._Person__posx] =  "\033[31m" + "\033[40m" + "\033[1m" +  self.__din[j][i]

    #when iceball moving, din rendering with scene or staying at one place
    def check_collision_iceball(self):
        for i in range(self.__width):
            for j in range(self.__height):
                        if global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx+self.__width] == '\033[34m' + '\033[47m'+ "\033[1m" + "0": 
                            #print("collided with iceball in check_collision_iceball func")
                            self.die()
                            return 1
        return 0


    def clear(self):
        for i in range(self.__width):
            for j in range(self.__height):
                global_var.scenery.scene_matrix[j+self._Person__posy][i+self._Person__posx] = "\033[37m" + "\033[40m" + " "

    def move_left(self):
        for i in range(self.__height):
            if global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx-1] == "\033[33m" + "\033[45m" + " ":
                return
        self.clear()
        self._Person__posx -= 1
        self.render()

    
    def check_left(self):
        for i in range(self.__height-1):
            if global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx-1] == "\033[37m" + "\033[93m" + "#":  
                self.die()
                return
            elif global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx-1] == "\033[37m" + "\033[93m" + "*":
                self.die()     
                return
            if "$" in global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx-1]:
                global_var.score += 1
                #print(global_var.score)
                #global_funct.create_footer()
            if "B" in global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx-1]:
                global_var.speed *= 1/2
            if "S" in global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx-1]:
                global_var.num_shield += 1
            elif global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx-1] == '\033[34m' + '\033[47m'+ "\033[1m" + "0": 
                self.die()
                return
                
        if self._Person__posx == global_var.scenery.scene_start_index:
            return
        self.move_left()


    def move_right(self):
        for i in range(self.__height):
            if global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx+self.__width] == "\033[33m" + "\033[45m" + " ":
                return
        self.clear()
        self._Person__posx += 1
        self.render()

    def check_right(self):

        for i in range(self.__height-1):
            if global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx+self.__width] == "\033[37m" + "\033[93m" + "#":
                self.die()
                return
            elif global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx+self.__width] == "\033[37m" + "\033[93m" + "*":
                self.die()
                return
            elif global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx+self.__width] == '\033[34m' + '\033[47m'+ "\033[1m" + "0": 
                self.die()
                return
        for i in range(self.__height):
            #print(global_var.num_shield)
            if global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx+self.__width] == "\033[33m" + "\033[45m" + " ":
                return
            if "$" in global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx+self.__width]  :
                global_var.score += 1
                #print(global_var.score)
                #global_funct.create_footer()
            if "B" in global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx+self.__width]:
                global_var.speed *= 1/2
            if "S" in global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx+self.__width] :
                global_var.num_shield += 1
        if self._Person__posx + self.__width >= global_var.scenery.scene_length - int(config.columns/2) - 2:
            return
        if (self._Person__posx - global_var.scenery.scene_start_index) >= int(config.columns/2):
            self.clear()
            global_var.scenery.scene_start_index += 1
            self._Person__posx += 1
            self.render()
            return
        self.move_right()
    def check_collisions_up(self):
        for i in range(self.__width):
            if global_var.scenery.scene_matrix[self._Person__posy+self.__height][self._Person__posx+i] == "\033[33m" + "\033[45m" + " ":
                return
            if "$" in global_var.scenery.scene_matrix[self._Person__posy+self.__height][self._Person__posx+i] :
                global_var.score += 1
                #print(global_var.score)
                #global_funct.create_footer()
            if "B" in global_var.scenery.scene_matrix[self._Person__posy+self.__height+1][self._Person__posx+i]:
                global_var.speed *= 1/2
            #print("dgdsgshhh    dsggsj")
            #print(self._Person__posy+self.__height+1,self._Person__posy)
            if "S" in global_var.scenery.scene_matrix[self._Person__posy+self.__height+1][self._Person__posx+i] :
                
                global_var.num_shield += 1
            if global_var.scenery.scene_matrix[self._Person__posy+self.__height][self._Person__posx+i] == "\033[31m" + "\033[40m" + " ":
                self.die()
                return
            elif global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx+self.__width] == '\033[34m' + '\033[47m'+ "\033[1m" + "0": 
                self.die()
                return
        if self._Person__posy == global_var.scenery.ground_level:
            return
    def gravity(self):
        for i in range(self.__width):
            if global_var.scenery.scene_matrix[self._Person__posy+self.__height][self._Person__posx+i] == "\033[33m" + "\033[45m" + " ":
                return
            if "$" in global_var.scenery.scene_matrix[self._Person__posy+self.__height][self._Person__posx+i]:
                global_var.score += 1
                ##print(global_var.score)
                #global_funct.create_footer()
            if "B" in global_var.scenery.scene_matrix[self._Person__posy+self.__height+1][self._Person__posx+i]:
                global_var.speed *= 1/2

            #print(self._Person__posy+self.__height+1,self._Person__posy)
            if "S" in global_var.scenery.scene_matrix[self._Person__posy+self.__height+1][self._Person__posx+i] :
                
                global_var.num_shield += 1
            if global_var.scenery.scene_matrix[self._Person__posy+self.__height][self._Person__posx+i] == "\033[31m" + "\033[40m" + " ":
                self.die()
                return
            elif global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx+self.__width] == '\033[34m' + '\033[47m'+ "\033[1m" + "0": 
                self.die()
                return
        if self._Person__posy == global_var.scenery.ground_level:
            return
        
         
        self.v += self.g
        s = self._Person__posy + self.v
        self.clear()
        self._Person__posy = min(s,22)
        self.render()
         
    def check_iceball(self):
        for i in range(self.__width):
            for j in range(self.__height):
                if "0"  in global_var.scenery.scene_matrix[self._Person__posy+i][self._Person__posx+self.__width]: 
                    self.die()
        self.render()

    def jump(self):
        y = self._Person__posy
        while self._Person__posy > y - 2*len(config.platform)+3 and self._Person__posy > 3:
            flag = 1
            for i in range(self.__width):
                if global_var.scenery.scene_matrix[self._Person__posy-1][self._Person__posx+i] == "\033[33m" + "\033[45m" + " ":
                        flag = 0
                        break
                if global_var.scenery.scene_matrix[self._Person__posy-1][self._Person__posx+i] == "\033[37m" + "\033[93m" + "#":
                    self.die()
                    return
                if global_var.scenery.scene_matrix[self._Person__posy-1][self._Person__posx+i] == "\033[37m" + "\033[93m" + "*":
                    self.die()
                    return
                elif global_var.scenery.scene_matrix[self._Person__posy-1][self._Person__posx+i] == '\033[34m' + '\033[47m'+ "\033[1m" + "0": 
                    self.die()
                    return
                if "$" in global_var.scenery.scene_matrix[self._Person__posy-1][self._Person__posx+i] :
                    global_var.score += 1
                    #global_funct.create_footer()
                
                if "B" in global_var.scenery.scene_matrix[self._Person__posy-1][self._Person__posx+i]:
                    global_var.speed *= 1/2
                if "S" in global_var.scenery.scene_matrix[self._Person__posy-1][self._Person__posx+i] :
                    global_var.num_shield += 1   
            if not flag:

                for i in range(4,character.posy):
                    if global_var.scenery.scene_matrix[character.posx][i]== "\033[37m" + "\033[01m" + "\033[31m"+ "-":
                        character.posy -= i
                        character.render()
            self.clear()

            self._Person__posy -= 1
            self.render()

            global_funct.check_input(self)
            if global_var.quit_flag:
                return


class dragon(Person):

    def __init__(self, x,y):
        self.__lives = 4
        self.collision = 0

        Person.__init__(self, x, y)
        self.__iceballs = '0'
        self.__drago = [list("              \_|// .   /||\\\  `~~~~`---.___./       "), 
        list("           _-~o  `\/    |||  \\\           _,'`       "),
        list("         ;_,_,/ _-'|-   |`\   \\\        ,'           "),
        list("           '',/~7  /-   /||   `\.     /               "),   
        list("         / |    |   `\_   ,^             /\           "),
        list("    _,-' _/'\ ,-'~____-'`-/                 ``===\    "),
        list("   ((->/'    \|||' `.     `\.  ,                _||   "),
        list("              \_     `\      `~---|__i__i__\--~'_/    "),
        list("             __-^-_    `)  \-.______________,-~'      "),
        list("            ///,-'~`__--^-  |-------~~~~^'            "),
        list("                   ///,--~`-\                         ")]
        self.__height = len(self.__drago)
        self.__width = len(self.__drago[0])
        self.a = 0
    def __del__(self):
        del(self)
    def get_drago(self):
        return self.__drago
    def get_height(self):
        return self.__height
    def get_lives(self):
        return self.__lives
    def get_width(self):
        return self.__width
        #print(self.__width)
    def clear(self):
        for i in range(self.__width):
            for j in range(self.__height):
                global_var.scenery.scene_matrix[j+self._Person__posy][i+self._Person__posx] = "\033[37m" + "\033[40m" + " "

    def render(self):
        #print(self._Person__posx,self._Person__posy)
        for i in range(self.__width):
            for j in range(self.__height):
                if self.__drago[j][i] != " ":
                    global_var.scenery.scene_matrix[j+self._Person__posy][i+self._Person__posx] =  "\033[33m" + "\033[40m" + "\033[1m" + self.__drago[j][i]
    def change_pos(self, dx, dy):
        
        self.clear()
        self._Person__posy = min(dy,22)
        #print(self._Person__posx,self._Person__posy)
        self.render()



    def dec_lives(self): 

        for i in range(self.__width):
            for j in range(self.__height):
                if ">" in global_var.scenery.scene_matrix[self._Person__posy+j][self._Person__posx+i] :
                    self.__lives -=  1
                    self.collision = 1
                    if(self.__lives<=0):
                        self.clear()
            return self.collision

    