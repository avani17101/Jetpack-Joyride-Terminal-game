import os
import people
import global_var 
import config
import scenes
import global_funct
import random
import time
import obstacles
import shoot_objects
#tic = time.time()


from colorama import init, Fore, Back, Style


if __name__ == "__main__":

    os.system('tput reset')
    print("Please enter your name: ")
    global_var.username = input()
    os.system('tput reset')
    config.create_banner()
    global_var.tic = time.time()

    i=1
    mags = []
    hlist = []
    vblist = []
    sblist = []
    for i in range(5):
        x = random.randint(10,1000)
        y = random.randint(4,6)
        mag = obstacles.magnet(x,y)
        mag.create_magnet()
        mags.append(mag)

    for i in range(5):
        a = random.randint(1,700)
        x  = 4
        x += a
        y = random.randint(6,8)
        h = obstacles.hbeam(x,y)
        h.create_hbeam()
        hlist.append(h)
    for i in range(5):
        a = random.randint(1,5)
        x = 35
        x += a
        y = random.randint(8,10)
        vb1 = obstacles.vbeam(35,8)
        vb1.create_vbeam()
        c = vb1.check_bullet()  
        vblist.append(vb1)
    for i in range(5):
        x = random.randint(10,1000)
        y = random.randint(4,8)
        sb1 = obstacles.sbeam(45,12)
        sb1.create_sbeam()
        sb1.check_bullet()        
        sblist.append(sb1)

    din = people.din(int(config.columns/2), global_var.scenery.ground_level-4)
    din.render()

    y = (global_var.scenery.ground_level-11)
    dgan = people.dragon( 1000, y)
    dgan.render()

 
    global_var.scenery.render()

    sh =0   
    g = 0
    tic = 0
    tac = 0
    tic1 = 0
    tac1 = 0
    grav = [1,0.8,.6,.4,.2]
    stage = 0
    bullets_list = []
    iblist = [] 
    while True:
        for i in range(5):
            c = mags[i].check_bullet()
            if(c==1):
                mags[i].clear()
                mags.remove(mags[i])
                del(mag)
            c = vblist[i].check_bullet()  
            if(c==1):
                vblist[i].clear()
                vblist.remove(vblist[i])
                del(vblist[i])
            c = sblist[i].check_bullet()  
            if(c==1):
                sblist[i].clear()
                sblist.remove(sblist[i])
                del(sblist[i])
            c = hlist[i].check_bullet()  
            if(c==1):
                hlist[i].clear()
                hlist.remove(hlist[i])
                del(hlist[i])
            c = mags[i].check_bullet()  
            if(c==1):
                mags[i].clear()
                mags.remove(mags[i])
                del(mags[i])
        if din.get_lives() <= 0:
            global_funct.display_ending("YOU LOST!")
            break
        global_var.n = global_var.n-1   #decreasing timer
        #checking for collision
        for i in range(5):

            # mags[i].
            # hlist
            c = vblist[i].check_bullet()  
            if(c==1):
                vblist.remove(vblist[i])
                del(vblist[i])
            # sblist
        #din.collected_powerups()
        if(time.time()-sh > 10):
            # print("deactivating shield")
            din.deshield()
            din.render()
        #din.check_collision_iceball()
        if(global_var.n<0):
            global_funct.display_ending("TIME OVER!!! YOU LOST :(",din.get_lives())  
        global_funct.check_magnet(din)
        tac = time.time()
        #print(tac-tic)
        if(tic!=0 and tac-tic>grav[stage]):
            if(din.get_posy()<22):
                din.clear()
                din.set_posy(din.get_posy()+1)
                din.check_collisions_up()
                din.render()
                dgan.change_pos(din.get_posx(),din.get_posy()) 
                stage+= 1
                if(stage>4):
                    stage = 4
        if(global_var.n%5==0 and din.get_posx()>500):
            ib = shoot_objects.iceballs(dgan.get_posx(),dgan.get_posy(),din.get_posx(),din.get_posy(),din.get_din())
            iblist.append(ib)
        #ib.list.append(ib)move_left()        


        din.render()
        tac1 = time.time()
        if(tac1-tic1>global_var.speed):
            global_var.scenery.scene_start_index += 1
            global_funct.reset_scenery()
            din.check_right()
            tic1 = time.time()
        for ib in iblist:
            g = din.check_collision_iceball()
            #cd = dgan.dec_lives()
            if(g!=1):
                ib.move_left()
            else:
                g=0
                iblist.remove(ib)


        if global_var.quit_flag:
            global_funct.display_ending("YOU LOST!")
            break

        # global_funct.run_background(din)
        global_funct.check_magnet(din)
        event = config.get_key(config.get_input())
         
        if event == config.QUIT:
            global_funct.display_ending("YOU QUITTED!")
            break
        elif event == config.LEFT:
            #din.collected_powerups()
            din.check_left()
            #din.collected_powerups()

        elif event == config.RIGHT:
            #din.collected_powerups()
            din.check_right()
            #din.collected_powerups()
        #tic = time.time()
        elif event == config.UP:
            if(din.get_posy()>3):
                # din.collected_powerups()
                din.jump()
                dgan.change_pos(din.get_posx(),din.get_posy())
                tic = time.time()
                stage =0

        elif event == config.FIRE: 
            bt = shoot_objects.Bullet(din.get_posx()+din.get_width(), int(din.get_posy()+din.get_height()/2),dgan.get_drago())
            bullets_list.append(bt)
            #print("hi fire")

        for b in bullets_list:
            
            if b.get_posx() >= global_var.scenery.scene_length-int(config.columns/2)+2:
                    del b
                    global_var.dragon_lives -= 1
                    c = dgan.dec_lives()
                    global_var.score += 10
                    if dgan.get_lives() <= 0:
                        global_funct.display_ending("CONGRATULATIONS... YOU WON!")
                        break
                    else:
                        b.move_right()   
            g = b.check_collision()
            cd = dgan.dec_lives()
            if(g!=1 or cd!=1):
                b.move_right()
            else:
                for i in range(len(vblist)):
                    c = vblist[i].check_bullet()  
                    if(c==1):
                        vblist.remove(vblist[i])
                        del(vblist[i])
                bullets_list.remove(b)
                b.clear()
                del(b)
        if event == config.SHIELD:
            if(global_var.num_shield>0 and (sh-time.time()>70 or sh==0)):

                print("activating shield")
                sh = time.time()
                global_var.num_shield -= 1
                din.shield()
                din.render()
            else:
                if(global_var.num_shield<0 ):
                    print("no shield left")
                else:
                    print("wait for 60 seconds bro!!")
        global_funct.reset_scenery()
