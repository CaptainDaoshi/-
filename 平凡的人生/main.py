import pygame
import sys
#import parameter
import player
from pygame.locals import *
from moviepy.editor import *
from tkinter import * 
from tkinter import messagebox 
Tk().wm_withdraw() #to hide the main window 
 

#变量 
bg_size = width,height = 1200,750

bg_image = 'images/background.jpg'





def main():
    pygame.init()

    #音乐音效
    pygame.mixer.init()   #混音器
    pygame.mixer.music.load('sounds/bgm.mp3')
    pygame.mixer.music.set_volume(0.3)        
    door_sound = pygame.mixer.Sound('sounds/开门声.wav')
    gameover_sound = pygame.mixer.Sound('sounds/替换MAV.wav')  #结束音乐
    pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(bg_size)   
    pygame.display.set_caption('什么都队')
    #开局背景
    start_backg = pygame.image.load('images/startgobackg.jpg').convert_alpha()
    
    background = pygame.image.load(bg_image).convert_alpha()   #背景图加入
    change1 = pygame.image.load('images/background1l.jpg').convert_alpha()  #第一次选择第一扇门
    #pygame.image.load('婴儿啼哭.jpg').convert_alpha()   #婴儿图
    ending = pygame.image.load('images/ending.png').convert_alpha()   #ending图
    ending_rect = ending.get_rect()
    ending_rect.left,ending_rect.top = 1500,1000


    c1_rect = change1.get_rect()
    c1_rect.left,c1_rect.top = 1000,1000

    mplayer = player.Player(bg_size)
    mplayer.rect.left,mplayer.rect.top = 520,450
    #player = pygame.image.load(ima_player)    #player
    #player2 = pygame.image.load(ima_player2)

    switch_image = True       #切换主角图片
    moving = False
    running = True
    startrun = True
    getstarted = True
    go = False
    
    flag = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0
    flag5 = 0 
    #主循环
    while running:
        while getstarted:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #检测键盘操作
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_SPACE]:
                getstarted = False
            get_start = pygame.image.load('images/priority.jpg').convert_alpha()
            screen.blit(get_start,(0,0))
            pygame.display.flip()
            
            
        #开局
        while startrun:                     
            #检测键盘操作
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            key_pressed = pygame.key.get_pressed() 

            if key_pressed[K_w]:
                #dosomething
                moving = True
                mplayer.moveup()
            elif key_pressed[K_s]:
                #dosomething
                moving = False
                mplayer.movedown()
            elif key_pressed[K_a]:
                mplayer.moveleft()
                moving = True
            elif key_pressed[K_d]:
                mplayer.moveright()
                moving = True

            if mplayer.rect.right >= 630 and mplayer.rect.right <= 680 and mplayer.rect.top >=30 and mplayer.rect.top <=200:
                #dosomething
                #start_backg = pygame.image.load('startgobackg.jpg').convert_alpha()
                messagebox.showinfo('你的人生即将启航!','冲！')
                door_sound.play()
                startrun = False
                mplayer.rect.left,mplayer.rect.top = 520,450 #重置player位置
                
            screen.blit(start_backg,(0,0))
            switch_image = not switch_image

            if switch_image:
                screen.blit(mplayer.imageyou,mplayer.rect)
            else:
                screen.blit(mplayer.imagezuo,mplayer.rect)
            pygame.display.flip()
            clock.tick(100)  #帧率

        #以上开局画面结束

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #print(1)
        
        #检测键盘操作
        key_pressed = pygame.key.get_pressed() 

        if key_pressed[K_w]:
            #dosomething
            moving = True
            mplayer.moveup()
        elif key_pressed[K_s]:
            #dosomething
            moving = False
            mplayer.movedown()
        elif key_pressed[K_a]:
            mplayer.moveleft()
            moving = True
        elif key_pressed[K_d]:
            mplayer.moveright()
            moving = True

        #print(mplayer.rect.left)
        
        #面对过程
        if not flag:
            if mplayer.rect.right >= 250 and mplayer.rect.right <= 295 and mplayer.rect.top >=110 and mplayer.rect.top <=200:
                background = pygame.image.load('images/background1l.jpg').convert_alpha()
                pygame.time.delay(50)#延迟（单位毫秒）
                mplayer.rect.right = 2000
                messagebox.showinfo('你选择辍学去打工？','是的')
                door_sound.play()
                mplayer.rect.left,mplayer.rect.top = 520,450
                flag = 1
            
            elif mplayer.rect.right >= 600 and mplayer.rect.right <= 700 and mplayer.rect.top >=110 and mplayer.rect.top <=200:
                background = pygame.image.load('images/background1m.jpg').convert_alpha()
                pygame.time.delay(50)#延迟（单位毫秒）
                mplayer.rect.right = 2000
                messagebox.showinfo('你选择进入中专、大专？','是的')
                door_sound.play()
                mplayer.rect.left,mplayer.rect.top = 520,450
                flag = 2

            elif mplayer.rect.right >= 900 and mplayer.rect.right <= 1000 and mplayer.rect.top >=110 and mplayer.rect.top <=200:
                background = pygame.image.load('images/background1r.jpg').convert_alpha()
                pygame.time.delay(50)#延迟（单位毫秒）
                mplayer.rect.right = 2000
                messagebox.showinfo('你选择坚持学习考入本科？','是的')
                door_sound.play()
                mplayer.rect.left,mplayer.rect.top = 520,450
                flag = 3
        else:
            if flag == 1:
                if not flag5:
                    flag5 += 1
                    messagebox.showinfo('平凡的人生','你早早结婚，生儿育女，平淡一生~')
                ending_rect.left,ending_rect.top = -50,0
                gameover_sound.play()
            elif flag == 2:
                if not flag2:
                    background = pygame.image.load('images/background2.jpg').convert_alpha()
                    if mplayer.rect.right >= 400 and mplayer.rect.right <= 500 and mplayer.rect.top >=160 and mplayer.rect.top <=220:
                        messagebox.showinfo('你选择专升本？','是的')
                        messagebox.showinfo('你成功进入了大学','好的')
                        background = pygame.image.load('images/background2l.jpg').convert_alpha()
                        flag2 = 1
                    elif mplayer.rect.right >= 815 and mplayer.rect.right <= 895 and mplayer.rect.top >=160 and mplayer.rect.top <=220:
                        messagebox.showinfo('你选择直接工作？','是的')
                        gameover_sound.play()
                        background = pygame.image.load('images/background2r.jpg').convert_alpha()
                        messagebox.showinfo('平凡的人生','你找工作四处碰壁')
                        ending_rect.left,ending_rect.top = -50,0
                        mplayer.rect.left = 2000     #消失
                        flag2 = 2
                elif flag2 == 1:
                    if flag4==0:
                        mplayer.rect.left,mplayer.rect.top = 520,450
                        flag4+=1
                    background = pygame.image.load('images/background3.jpg').convert_alpha()
                    if mplayer.rect.right >= 220 and mplayer.rect.right <= 300 and mplayer.rect.top >=160 and mplayer.rect.top <=180:
                        messagebox.showinfo('你选择考研？','是的')
                        gameover_sound.play()
                        background = pygame.image.load('images/background3l.png').convert_alpha()
                        messagebox.showinfo('平凡的一生','很遗憾你没考上！')
                        ending_rect.left,ending_rect.top = 0,0
                        messagebox.showinfo('平凡的一生','生儿育女，平淡一生~')
                        mplayer.rect.left = 2000     #消失
                        flag2 = 2
                    elif mplayer.rect.right >= 570 and mplayer.rect.right <= 650 and mplayer.rect.top >=160 and mplayer.rect.top <=180:
                        messagebox.showinfo('你选择考公？','是的')
                        gameover_sound.play()
                        background = pygame.image.load('images/background3m.png').convert_alpha()
                        messagebox.showinfo('平凡的一生','很遗憾你没考上！')
                        ending_rect.left,ending_rect.top = -50,0
                        messagebox.showinfo('平凡的一生','生儿育女，平淡一生~')
                        mplayer.rect.left = 2000     #消失
                        flag2 = 3
                    elif mplayer.rect.right >= 900 and mplayer.rect.right <= 970 and mplayer.rect.top >=160 and mplayer.rect.top <=180:
                        messagebox.showinfo('你选择就业？','是的')
                        gameover_sound.play()
                        background = pygame.image.load('images/background3r.png').convert_alpha()
                        messagebox.showinfo('平凡的一生','生儿育女，平淡一生~')
                        ending_rect.left,ending_rect.top = -50,0
                        mplayer.rect.left = 2000     #消失
            #大学
            elif flag == 3:
                if flag4==0:
                    mplayer.rect.left,mplayer.rect.top = 520,450
                    flag4+=1
                #messagebox.showinfo('','你坚持学习，考上了本科!')
                background = pygame.image.load('images/background3.jpg').convert_alpha()
                if mplayer.rect.right >= 220 and mplayer.rect.right <= 300 and mplayer.rect.top >=160 and mplayer.rect.top <=180:
                    messagebox.showinfo('你选择考研？','是的')
                    gameover_sound.play()
                    background = pygame.image.load('images/background3l.png').convert_alpha()
                    messagebox.showinfo('平凡的一生','恭喜你考上了！')
                    mplayer.rect.left = 2000     #消失
                elif mplayer.rect.right >= 570 and mplayer.rect.right <= 650 and mplayer.rect.top >=160 and mplayer.rect.top <=180:
                    messagebox.showinfo('你选择考公？','是的')
                    gameover_sound.play()
                    background = pygame.image.load('images/background3m.png').convert_alpha()
                    messagebox.showinfo('平凡的一生','恭喜你考上了！')
                    mplayer.rect.left = 2000     #消失
                elif mplayer.rect.right >= 900 and mplayer.rect.right <= 970 and mplayer.rect.top >=160 and mplayer.rect.top <=180:
                    messagebox.showinfo('你选择就业？','是的')
                    gameover_sound.play()
                    background = pygame.image.load('images/background3r.png').convert_alpha()
                    messagebox.showinfo('平凡的一生','就业岗位好，薪资高，跨越阶级，成为工薪阶级！')
                    mplayer.rect.left = 2000     #消失
                

        #刷新
        screen.blit(background,(0,0))
        
        #绘制player

        switch_image = not switch_image

        if switch_image:
            screen.blit(mplayer.imageyou,mplayer.rect)
        else:
            screen.blit(mplayer.imagezuo,mplayer.rect)

        #绘制其它东西
        screen.blit(change1,c1_rect)
        screen.blit(ending,ending_rect)
        pygame.time.delay(10)#延迟（单位毫秒）
        #更新界面
        pygame.display.flip()
        clock.tick(50)  #帧率   



if __name__ == '__main__':
    main()





