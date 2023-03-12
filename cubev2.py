from rubik.cube import Cube
import pygame
import time
import sys
from random import randint
randomstart=False
try:
	if sys.argv[1]=="T":
		randomstart=True
except Exception as e: 
	print(e)
B=(0,0,255)
G=(0,255,0)
R=(255,0,0)
O=(255, 89, 0)
Y=(255, 213, 0)
W=(255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((800, 500))



#moves
#['B', 'Bi', 'D', 'Di', 'E', 'Ei', 'F', 'Fi', 'L', 'Li',
#'M', 'Mi', 'R', 'Ri', 'S', 'Si', 'U', 'Ui',
# 'X', 'Xi', 'Y', 'Yi',
#'Z', 'Zi',]


c=Cube("YYYYYYYYYGGGOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRWWWWWWWWW")


def getcolorcode(c):
	if c=="B":
		return B
	elif c=="R":
		return R
	elif c=="G":
		return G
	elif c=="Y":
		return Y
	elif c=="O":
		return O
	elif c=="W":
		return W
	else:
		return (100,100,100)
def makerandom(returnv=False,reverse=None):
	a=randint(0,10) if reverse == None else (reverse+1 if reverse%2 == 0 else reverse-1)
	if a==0:
		c.R()
	elif a==1:
		c.Ri()
	elif a==2:
		c.U()
	elif a==3:
		c.Ui()
	elif a==4:
		c.L()
	elif a==5:
		c.Li()
	elif a==6:
		c.F()
	elif a==7:
		c.Fi()
	elif a==8:
		c.D()
	elif a==9:
		c.Di()

	if returnv:
		return a

if randomstart:
	for i in range(randint(0,5)):
		makerandom()


line1=[(300,200),(350,200),(400,200)]
line2=[(300,250),(350,250),(400,250)]
line3=[(300,300),(350,300),(400,300)]
line4=[(150,350),(200,350),(250,350),(300,350),(350,350),(400,350),(450,350),(500,350),(550,350),(600,350),(650,350),(700,350)]
line5=[]
for i in line4:
	line5.append((i[0],i[1]+50))

line6=[]
for i in line5:
	line6.append((i[0],i[1]+50))

line7=[]
line8=[]
line9=[]
for i in line3:
	line7.append((i[0],i[1]+200))
	line8.append((i[0],i[1]+250))
	line9.append((i[0],i[1]+300))

linepos=[line1]+[line2]+[line3]+[line4]+[line5]+[line6]+[line7]+[line8]+[line9]
linecolors=[]
def setcolors():
	global linecolors
	linecolors=[]
	cube=c.__str__().replace(" ","")
	lines=cube.splitlines()
	
	for i in lines:
		for a in list(i):
			linecolors.append(getcolorcode(a))
texts=[["Is cube solved",(0,0),(255,255,255),17],["%{}",(0,20),(0,50,255),15]]
def drawtext():
	screen.fill((0,0,0))
	global texts
	print(texts[1][0])
	for i in texts:
		font=pygame.font.Font(pygame.font.get_default_font(),i[3])
		text_surface=font.render(i[0],True,i[2])
		screen.blit(text_surface,dest=i[1])



def puttext(text,pos,color=(255,255,255),punto=36):
	global texts
	for i in texts:
		if i[0] == text:
			break
	else:
		texts.append([text,pos,color,punto])
#puttext("Hello",(15,15),punto=20,color=(x,y))

def drawcube():
	t=0
	for i in linepos:

		for a in i:
			pygame.draw.rect(screen,linecolors[t],(a[0],a[1]-150,40,40))
			t=t+1
setcolors()
full = linecolors
def issolved():
	global full
	x=0
	for i in range(54):
		if linecolors[i]==full[i]:
			x=x+1
	
	return f"%{round(x*100/54,2)}"


def resetcube():
	screen.fill((0,0,0))
	drawtext()
	setcolors()
	#puttext(f"Is cube solved:{c.is_solved()}",(0,0),punto=20)
	texts[0][0]="Is cube solved:{}".format(c.is_solved())
	#puttext(issolved(),(0,20),color=(0,50,255),punto=15)
	texts[1][0]=issolved()
	drawcube()



def autosolvecube():
	#make random move
	#if random move is worked keep going
	#else random move isnt worked undo
	temp=0
	while True:
		
		if c.is_solved()==True:
			break
		temp=float(issolved().replace("%",""))
		move=makerandom(returnv=True)
		resetcube()
		pygame.display.update()
		now=float(issolved().replace("%",""))
		
		if now<temp:
			makerandom(reverse=move)
			resetcube()
			pygame.display.update()
		
	

ai=False # you dont wanna open this
while True:
	if ai:
		autosolvecube()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			# Keys UP:W RIGHT:D LEFT:A DOWN:S ### UP':Arrow UP \ RIGHT':Arrow RIGHT \ LEFT':Arrow LEFT \ DOWN': Arrow DOWN
			#FRONT:Q \ FRONT': E
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				c.L()
			if event.key == pygame.K_w:
				c.U()
			if event.key == pygame.K_d:
				c.R()
			if event.key == pygame.K_s:
				c.D()

			if event.key == pygame.K_UP:
				c.Ui()
			if event.key == pygame.K_DOWN:
				c.Di()
			if event.key == pygame.K_LEFT:
				c.Li()
			if event.key == pygame.K_RIGHT:
				c.Ri()

			if event.key == pygame.K_q:
				c.F()
			if event.key == pygame.K_e:
				c.Fi()
	resetcube()
	pygame.display.update()



