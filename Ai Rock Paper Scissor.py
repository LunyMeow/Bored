import random
import sys
import os
import time

debug=False
if len(sys.argv)>1:
	debug=True if sys.argv[1] == "-d" else False
choices = ['rock', 'paper', 'sci']

userp=0
ai=0

sindex=int(input("Search weird number \"The less the smarter\" (3-100)..:"))


def play(a,user): #a is for winning
	global userp,ai
	computer_choice=a if a!=None else  random.choice(choices)
	print("Computer is ",computer_choice)
	print("You are ",user)
	if computer_choice == user_choice:
		print('Tie')
	elif user_choice == 'rock' and computer_choice == 'sci':
		print('User Win')
		userp+=1
	elif user_choice == 'paper' and computer_choice == 'rock':
		print('User Win')
		userp+=1
	elif user_choice == 'sci' and computer_choice == 'paper':
		print('User Win')
		userp+=1
	else:
		print('Ai smarter than you :)')
		ai+=1
	print(f"User :{userp}")
	print(f"AI   :{ai}")

a=[]

def findlocations(list,item):
	t=0
	lista=[]
	for i in list:
		if i==item:
			lista.append(t)
		t+=1
	return lista
def guessuser(x): #x is user input
	a.append(x)
	"""
	a.append(x)
	rockp=(a.count("rock")/len(a))*100
	paperp=(a.count("paper")/len(a))*100
	scip=(a.count("sci")/len(a))*100
	"""
	rockp=0
	paperp=0
	scip=0
	
	rockafterpaper=0
	rockaftersci=0
	rockafterrock=0

	paperafterrock=0
	paperafterpaper=0
	paperaftersci=0

	sciafterpaper=0
	sciafterrock=0
	sciaftersci=0

	timer=1 
	templist=findlocations(a,"rock")
	templist = templist[-sindex:]
	while timer<len(templist):
		if a[templist[timer]-1]=="paper":
			rockafterpaper+=1
		elif a[templist[timer]-1]=="rock":
			rockafterrock+=1
		elif a[templist[timer]-1]=="sci":
			rockaftersci+=1
		
		timer+=1
		
	
	timer=1 
	templist=findlocations(a,"paper")
	templist = templist[-sindex:]
	while timer<len(templist):
		if a[templist[timer]-1]=="paper":
			paperafterpaper+=1
		elif a[templist[timer]-1]=="rock":
			paperafterrock+=1
		elif a[templist[timer]-1]=="sci":
			paperaftersci+=1
		timer+=1
	timer=1 
	templist=findlocations(a,"sci")
	templist = templist[-sindex:]
	while timer<len(templist):
		if a[templist[timer]-1]=="paper":
			sciafterpaper+=1
		elif a[templist[timer]-1]=="rock":
			sciafterrock+=1
		elif a[templist[timer]-1]=="sci":
			sciaftersci+=1
		timer+=1
	if paperafterrock>paperafterpaper and paperafterrock>paperaftersci:
		rockp=paperafterrock
	elif paperafterpaper>paperaftersci and paperafterpaper>paperafterrock:
		paperp=paperafterpaper
	elif paperaftersci>paperafterrock and paperaftersci>paperafterpaper:
		scip=paperaftersci

	if rockafterrock>rockafterpaper and rockafterrock>rockaftersci:
		rockp=rockafterrock
	elif rockafterpaper>rockaftersci and rockafterpaper>rockafterrock:
		paperp=rockafterpaper
	elif rockaftersci>rockafterrock and rockaftersci>rockafterpaper:
		scip=rockaftersci

	if sciafterrock>sciafterpaper and sciafterrock>sciafterrock:
		rockp=sciafterrock
	elif sciafterpaper>sciafterrock and sciafterpaper>sciaftersci:
		paperp=sciafterpaper
	elif sciaftersci>sciafterrock and sciaftersci>sciafterpaper:
		scip=sciaftersci

	if debug:
		#print(f"Paper {round(paperp,3)}: Rock {round(rockp,3)}: Sci {round(scip,3)}")
		print(f"Paper :{paperafterrock} {paperaftersci} {paperafterpaper}")
		print(f"Rock  :{rockafterrock} {rockaftersci} {rockafterpaper}")
		print(f"Sci   :{sciafterrock} {sciaftersci} {sciafterpaper}")

	if rockp>paperp and rockp > scip:
		return "paper"
	elif paperp > rockp and paperp > scip:
		return "sci"
	elif scip > rockp and scip > paperp:
		return "rock"
	return None



while True:
	#user_choice=random.choice(choices)
	#time.sleep(0.05)
	user_choice = input("Enter rock, paper, or sci:\n")
	os.system("clear")
	play(guessuser(user_choice),user_choice)


