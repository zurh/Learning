#Title: Awake c:\Users\zurh\Desktop\PyDepo\Awake\Awake.py


###functions###

#get out of bed
def getOutOfBed():
	if yesOrNo() == True:
		print("You get out of bed. ");
	else:
		print("You decide to lay down a bit longer. ");
		print("A day goes by. ");
		print("Get out of bed? ");
		return getOutOfBed()

#you drink
def drink():
	choice = input("drink the glass of water. yes or no: ")
	if choice == ("yes"):
		print("You drink the glass of water ");
		print("You feel a bit better");
	elif choice ==("no"):
		print("You decide not to drink the glass of water. ");
	else:
		print("times seems to slip by as you make a decision ");
		return drink()
		
#yes or no
def yesOrNo(prompt="(Y/N)?"): # prompt needs to be defined
	while 1:
		answer = input(prompt)
		answer = answer.strip()
		answer = answer.lower()
		yes = ['yes', 'y', 'yes']
		no =['no', 'n', 'nope']
		if answer in yes:
			return True
		elif answer in no:
			return False
		else:
			continue
	return False


#text and background color
text_color=(0,0,255);
background_color=(0,0,0);


###Player Info###
player = ("name", "gender", "role")
#name = input("Enter your name: ")
#gender = input("Are you male or female: ")
#role = knight, mage, archer, monk, thief


###Player Stats###
#playerStats = hp, attack, defense
#hp = none
#attack = none
#defense = none


###Items###
#weapons = sword, staff, bow, gloves, dagger
#projectiles = arrows, throwing daggers, spears 
#armor = shields, chest, head, legs/feet, arms/hands 
#potions = health, magic, invisible, strength, defense
	
	
#intro
print("You awake from dreams of fortune and adventure ")
print("Your head hurting from a sharp pain. ")


#beginning
print("Examining your situation you relize you lay in a bed. ")
print("To your left is a glass of water. ")
print("Do you drink the glass of water ")
drink() #Runs func/ you drink
print("")
print("A brisk and cold breeze flows from an open window. ")
print("Get out of the bed? ")
getOutOfBed() #Runs func/ get out of bed
print("your legs feeling wobbly as if youve been sleeping for months. ")
print("You examin the room but dont notice anything out of the ordinary. ")
print("Straight ahead of you is a door leading to a hall. ")
print("To your right is a door leading into a bathroom. ")
print("There is a dresser to your left with random objects spread across the top. ")
#need to add game options/actions like {examine, inventory, pick up, drop, equip, etc}




#quit()
