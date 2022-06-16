import pygame
import time
import sys
import random


car = random.randint(1,3)

pygame.init()
screen = pygame.display.set_mode([1200, 800])
white = [255, 255, 255]
red = [255, 0, 0]
screen.fill(white)
pygame.display.set_caption("Monty hall")
pygame.display.flip()

one = pygame.image.load('1.png')
one = pygame.transform.scale(one, (50, 50))

two = pygame.image.load('2.png')
two = pygame.transform.scale(two, (50, 50))

three = pygame.image.load('3.png')
three = pygame.transform.scale(three, (50, 50))

closed = pygame.image.load('closed.png')
closed = pygame.transform.scale(closed, (200, 400))

win = pygame.image.load('win.png')
win = pygame.transform.scale(win, (200, 400))

lose = pygame.image.load('lose.png')
lose = pygame.transform.scale(lose, (200, 400))

running = 1

screen.blit(one, (300, 0))
screen.blit(two, (600, 0))
screen.blit(three, (900, 0))
screen.blit(closed, (225, 100))
screen.blit(closed, (525, 100))
screen.blit(closed, (825, 100))
pygame.display.flip()


  
color = (255,255,255)
color_light = (170,170,170)
color_dark1 = (100,100,100)
color_dark2 = (100,100,100)
color_dark3 = (100,100,100)
color_dark_lock = (100, 100, 100)
color_darkk = (100,100,100)


x1 = 300
y1 = 550

x2 = 600
y2 = 550

x3 = 900
y3 = 550

x_lock = 525
y_lock = 700

clicked_one = False
clicked_two = False
clicked_three = False
lock = False

smallfont = pygame.font.SysFont('Corbel',50)
text1 = smallfont.render('1' , True , color)
text2 = smallfont.render('2' , True , color)
text3 = smallfont.render('3' , True , color)
text_lock = smallfont.render('LOCK' , True , color)

while running:
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            ##b1
            if x1 <= mouse[0] <= x1+50 and y1 <= mouse[1] <= y1+50 and lock == False:
                if color_dark1 == color_darkk:
                    color_dark1 = color_light
                    clicked_one = True
                else:
                    color_dark1 = color_darkk
                    clicked_one = False
                    
                if clicked_two:
                    clicked_two = False
                    color_dark2 = color_darkk
                if clicked_three:
                    clicked_three = False
                    color_dark3 = color_darkk
                    
            ##b2
            if x2 <= mouse[0] <= x2+50 and y2 <= mouse[1] <= y2+50 and lock == False:
                if color_dark2 == color_darkk:
                    color_dark2 = color_light
                    clicked_two = True
                else:
                    color_dark2 = color_darkk
                    clicked_two = False
                    
                if clicked_one:
                    clicked_one = False
                    color_dark1 = color_darkk
                if clicked_three:
                    clicked_three = False
                    color_dark3 = color_darkk
                    
            ##b3
            if x3 <= mouse[0] <= x3+50 and y3 <= mouse[1] <= y3+50 and lock == False:
                if color_dark3 == color_darkk:
                    color_dark3 = color_light
                    clicked_three = True
                else:
                    color_dark3 = color_darkk
                    clicked_three = False
                    
                if clicked_one:
                    clicked_one = False
                    color_dark1 = color_darkk
                if clicked_two:
                    clicked_two = False
                    color_dark2 = color_darkk

            ## b_lock
            if x_lock <= mouse[0] <= x_lock+200 and y_lock <= mouse[1] <= y_lock+200 and lock == False:
                if clicked_one or clicked_two or clicked_three:
                    lock = True
                    color_dark_lock = color_light

        mouse = pygame.mouse.get_pos()
        ##b1
        if x1 <= mouse[0] <= x1+50 and y1 <= mouse[1] <= y1+50:
            pygame.draw.rect(screen,color_light,[x1,y1,50,50])
        else:
            pygame.draw.rect(screen,color_dark1,[x1,y1,50,50])
        screen.blit(text1 , (x1+ 15,y1))

        
        ##b2
        if x2 <= mouse[0] <= x2+50 and y2 <= mouse[1] <= y2+50:
            pygame.draw.rect(screen,color_light,[x2,y2,50,50])
        else:
            pygame.draw.rect(screen,color_dark2,[x2,y2,50,50])
        screen.blit(text2 , (x2+ 15,y2))

        ##b3
        if x3 <= mouse[0] <= x3+50 and y3 <= mouse[1] <= y3+50:
            pygame.draw.rect(screen,color_light,[x3,y3,50,50])
        else:
            pygame.draw.rect(screen,color_dark3,[x3,y3,50,50])
        screen.blit(text3 , (x3+ 15,y3-7))

        ##b_lock
        if x_lock <= mouse[0] <= x_lock+200 and y_lock <= mouse[1] <= y_lock+50:
            pygame.draw.rect(screen,color_light,[x_lock,y_lock,200,50])
        else:
            pygame.draw.rect(screen,color_dark_lock,[x_lock,y_lock,200,50])
        screen.blit(text_lock , (x_lock+ 40,y_lock))



        if lock == True:
            time.sleep(5)
            if clicked_one:
                clicked = 1
            if clicked_two:
                clicked = 2
            if clicked_three:
                clicked = 3
            
            if clicked == 1 and car == 1:
                if random.randint(0,1) == 0:
                    screen.blit(lose, (525, 100))
                else:
                    screen.blit(lose, (825, 100))
            if clicked == 1 and car == 2:
                screen.blit(lose, (825, 100))
            if clicked == 1 and car == 3:
                screen.blit(lose, (525, 100))

            if clicked == 2 and car == 2:
                if random.randint(0,1) == 0:
                    screen.blit(lose, (225, 100))
                else:
                    screen.blit(lose, (825, 100))
            if clicked == 2 and car == 1:
                screen.blit(lose, (825, 100))
            if clicked == 2 and car == 3:
                screen.blit(lose, (225, 100))

            if clicked == 3 and car == 3:
                if random.randint(0,1) == 0:
                    screen.blit(lose, (225, 100))
                else:
                    screen.blit(lose, (525, 100))
            if clicked == 3 and car == 1:
                screen.blit(lose, (525, 100))
            if clicked == 3 and car == 2:
                screen.blit(lose, (225, 100))
  
            
        pygame.display.update()
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
