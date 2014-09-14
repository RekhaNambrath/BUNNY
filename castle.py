import sys,random,pygame,math
from pygame.locals import *
pygame.init()
fps=30
width=800
height=600
size=(800,600)
#colors
black=(0,0,0)
clock = pygame.time.Clock()
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Game")
s = pygame.display.get_surface()
screen.fill(black)
keys=[False,False,False,False]
grass=pygame.image.load("grass2.jpg")
castle=pygame.image.load("castle1.jpg")
pos_x=100
pos_y=100
player_pos=[pos_x,pos_y]
x=castle.get_height()
arrows=25
accuracy=[0,0]
i=0
y=0
x=0
a=pygame.image.load("player.png")
b=pygame.image.load("player2.png")
c=pygame.image.load("player4.gif")
d=pygame.image.load("player5.png")
e=pygame.image.load("player6.png")
f=pygame.image.load("player7.png")
g=pygame.image.load("player8.gif")
player=[a,b,c,d,e,f,g]
arrow=pygame.image.load("arrow.png")

while True:
	screen.fill(black)
	for x in range(width/grass.get_width()+10):
        	for y in range(height/grass.get_height()+10):
           		screen.blit(grass,(x*170,y*100))
   	   		screen.blit(castle,(0,x))
    			screen.blit(castle,(0,x+150))
    			screen.blit(castle,(0,x+300))
    			screen.blit(castle,(0,x+450))	
	
	screen.blit(player[i],[pos_x,pos_y])
	for event in pygame.event.get():
		if event.type==pygame.QUIT:		
			sys.exit()
		if event.type == pygame.KEYDOWN:
           		if event.key==K_DOWN:
                		keys[0]=True
            		elif event.key==K_UP:
               			keys[1]=True
				i=4
            		elif event.key==K_LEFT:
               			 keys[2]=True
            		elif event.key==K_RIGHT:
                		keys[3]=True
				i=2
       		if event.type == pygame.KEYUP:
            		if event.key==pygame.K_DOWN:
                		keys[0]=False
            		elif event.key==pygame.K_UP:
                		keys[1]=False
            		elif event.key==pygame.K_LEFT:
                		keys[2]=False
            		elif event.key==pygame.K_RIGHT:
                		keys[3]=False
		if keys[0]:
        		pos_y+=15
    		elif keys[1]:
			pos_x+=45
			pos_y-=30					
			screen.blit(player[i],[pos_x,pos_y])
			pos_x+=100
			pos_y+=30
			screen.blit(player[i+1],[pos_x,pos_y])
			i=0				
    		elif keys[2]:
        		pos_x-=15
    		elif keys[3]:			
			screen.blit(player[i],[pos_x,pos_y])
			pos_x+=25
			pygame.display.flip()		
	pygame.display.update()
	clock.tick(50)	
