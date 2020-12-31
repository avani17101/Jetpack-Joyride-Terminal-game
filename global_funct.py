import config
import random
import scenes
import os
import main
import people
import global_var
from colorama import Fore, Back, Style
import time
import scenes
import obstacles

def create_footer():
    print( Fore.WHITE + Back.RED + Style.BRIGHT + ("SCORE: " + str(global_var.score) + "|LIVES: " + str(global_var.lives))+"|TIMER: "+ str(global_var.n)+"|SHIELD: "+str(global_var.num_shield),end='')
    print(Style.RESET_ALL,end="")
def reset_scenery():
    config.create_banner()
    global_var.scenery.render()
    create_footer()
            
def check_magnet(character):
    x = character.get_posx()

    for i in range(x+1, x+5):
        for j in range(4,character.get_posy()-1):

            if(global_var.scenery.scene_matrix[j][i] == "\033[37m" + "\033[01m" + "\033[31m"+ "_" or global_var.scenery.scene_matrix[j][i] == "\033[37m" + "\033[01m" + "\033[31m"+ "|"):
                x = character.get_posx()
                character.clear()
                character.render()
                if(x<i):
                    x += 1
                    character.clear()
                    character.set_posx(x)
                    
                    character.render()
                else:
                    x -= 1
                    character.clear()
                    character.set_posx(x)
                y = character.get_posy()

                if(y>j):

                    y -= 1
                    character.clear()
                    character.set_posy(y)
                    
                    character.render()

def display_ending(message):
    os.system('tput reset')
    print(Fore.CYAN + Style.BRIGHT + ("SCORE: " + str(global_var.score)).center(config.columns))
    print(Fore.CYAN + Style.BRIGHT + ("LIVES: " + str(global_var.lives)).center(config.columns))
    print(Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + (message).center(config.columns))
    print(Style.RESET_ALL)
    global_var.quit_flag = 1
    return

# Check input while jumping
def check_input(character):
    if global_var.lives <= 0:
        global_var.quit_flag = 1  
        return
    event = config.get_key(config.get_input())
    if event == config.LEFT:
        character.check_left()
    elif event == config.RIGHT:
        character.check_right()
    elif event == config.QUIT:
        global_var.quit_flag = 1  
        return
    reset_scenery()

