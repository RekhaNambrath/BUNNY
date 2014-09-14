import sys,random,pygame,math
from pygame.locals import *
class Carrot(pygame.sprite.Sprite):
	def _init_(self):
		pygame.sprite.Sprite._init_(self)
		#self.image=pygame.Surface([25,25])	
		self.image=pygame.image.load("carrot.png")
		self.image.set_colorkey(white)
		self.rect=self.image.get_rect()

pygame.init()
fps=30
width=800
height=600
size=(800,600)
#colors
black=(0,0,0)
white=(255,255,255)
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
cpos_x=0
cpos_y=0
status=False
carrot_pos=[cpos_x,cpos_y,status]
x=castle.get_height()
carrots=0
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
carrot=Carrot
def random_carrot():
	cpos_x=random.randint(200,750)
	cpos_y=random.randint(200,550)
	status=True
	#carrot.rect.x=cpos_x
	#carrot.rect.y=cpos_y
	carrot_pos=[cpos_x,cpos_y,status]	
	return carrot_pos

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
	if(carrot_pos[2]):
		
		if pos_x==cpos_x or pos_y==cpos_y:
			screen.blit(player[0],[pos_x,pos_y])
			status=False
			carrots+=1
		else:
			screen.blit(carrot.image,[carrot_pos[0],carrot_pos[1]])	
	else:		
		carrot_pos=random_carrot()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:		
			sys.exit()
		if event.type == pygame.KEYDOWN:
           		if event.key==K_DOWN:
                		keys[0]=True
				i=6
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
        		pos_y+=30
			screen.blit(player[i],[pos_x,pos_y])
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
