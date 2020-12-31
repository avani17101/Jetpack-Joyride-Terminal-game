import config
import random
import time
import global_var
from colorama import init, Fore, Back, Style

class Scene(object):

    """ Scenes and levels """

    scene_height = int(config.rows)
    scene_length = int(config.columns*10)
    ground_level = int(config.rows/1.3)

    def __init__(self):
        self.scene_start_index = 0
        self.scene_matrix = [[" " for x in range(Scene.scene_length)] for y in range(Scene.scene_height)]
        self.create_sky()
        self.create_coins()
        self.create_boost()
        self.create_ground()
        self.create_shield()
    def render(self):

        for y in range(3, Scene.scene_height):
            pr = []
            for x in range(self.scene_start_index, self.scene_start_index+config.columns):
                pr.append(self.scene_matrix[y][x]+Style.RESET_ALL)
            print(''.join(pr))


    def create_ground(self):
        for y in range(Scene.ground_level, Scene.scene_height):
            for x in range(500):
                self.scene_matrix[y][x] = "\033[37m" + "\033[44m" + " "
        for y in range(Scene.ground_level, Scene.scene_height):
            for x in range(500, Scene.scene_length):
                self.scene_matrix[y][x] = "\033[37m" + "\033[44m" + "-"
        for y in range(Scene.ground_level, Scene.scene_height):
            for x in range(Scene.scene_length-int(config.columns/2), Scene.scene_length):
                self.scene_matrix[y][x] = "\033[37m" + "\033[44m" + " "

    def create_shield(self):
        x = 1
        while x < (Scene.scene_length-2*config.columns):
            offset = random.randint(5, int(config.columns/2.5))
            x += offset
            y = random.randint(int(Scene.scene_height/3)-3, self.ground_level-3)
            for i in range(len(config.shield)):
                for j in range(len(config.shield[0])):
                    self.scene_matrix[y+i][x+j] = "\033[33m" + "\033[40m" + "\033[1m" + config.shield[i][j]
  
    def create_boost(self):
        x = 1
        while x < (Scene.scene_length-2*config.columns):
            offset = random.randint(5, int(config.columns/2.5))
            x += offset
            y = random.randint(int(Scene.scene_height/3)-3, self.ground_level)
            for i in range(len(config.boost)):
                for j in range(len(config.boost[0])):
                    self.scene_matrix[y+i][x+j] = "\033[32m"+ "\033[40m" + config.boost[i][j]
    
    def create_sky(self): 
        for y in range(1, Scene.ground_level):
            for x in range(Scene.scene_length):
                self.scene_matrix[y][x] = "\033[37m" + "\033[40m" + " "
        for y in range(1, Scene.ground_level):
            for x in range(Scene.scene_length-int(config.columns/2), Scene.scene_length):
                self.scene_matrix[y][x] = "\033[37m" + "\033[40m" + " "


    def create_coins(self):
        x = 1
        while x < (Scene.scene_length-2*config.columns):
            offset = random.randint(5, int(config.columns/2.5))
            x += offset
            y = random.randint(int(Scene.scene_height/3)-3, self.ground_level)
            for i in range(len(config.coin)):
                for j in range(len(config.coin[0])):
                    self.scene_matrix[y+i][x+j] = "\033[33m" + "\033[40m" + "\033[1m" + config.coin[i][j]

    def create_coins2(self):
        x = 1
        while x < (Scene.scene_length-2*config.columns):
            offset = random.randint(5, int(config.columns/2.5))
            x += offset
            y = random.randint(int(Scene.scene_height/3)-3, self.ground_level)
            for i in range(len(config.coin2)):
                for j in range(len(config.coin2[0])):
     
                    self.scene_matrix[y+i][x+j] = "\033[33m" + "\033[40m" + "\033[1m" + config.coin2[i][j]
    def create_boost(self):
        x = 1
        while x < (Scene.scene_length-(config.columns*3)):
            offset = random.randint(50, 60)
            x += offset
            y = random.randint(int(Scene.scene_height/3)-3, self.ground_level)
            for i in range(len(config.boost)):
                for j in range(len(config.boost[0])):
                    self.scene_matrix[y+i][x+j] = "\033[31m" + "\033[47m" + "\033[1m" + config.boost[i][j]




            
    
