import random


print("                         <in this game you will have one help chance>                       ")
print()
s_number=random.randint(0,7)
life=0
life_limit=3
help_=0
help_limit=1

print("Please guess a number among 0-7: ")
g_number=int(input())

def function0(life,life_limit):
		print("Please guess a number among 0-7: ")
		g_number=int(input())					
		function3(life,life_limit)


def function3(life,life_limit):
	global g_number,s_number
	if life<=life_limit:
		if g_number==s_number:
			print()
			print("!! ALHUMDOLILLAAH ,You have done it !!")
			print()
			while True:
				print("Do you want to play again ?(y/n)")
				aggrement= input()
				if aggrement.lower()=="y":
					print("                         <in this game you will have one help chance>                       ")
					print()
					s_number=random.randint(0,7)
					life=0
					life_limit=3
					help_=0
					help_limit=1

					print("Please guess a number among 0-7: ")
					g_number=int(input())
					function4(help_,help_limit)
				else:
					print("____________________")
					print("Thanks for Guessing")
					print("------- :) ---------")
					exit()
			
		elif g_number>s_number:
			print()
			print(" INSHA'ALLAAH, you will do it next time !")
			print()
			print("you have "+str(life_limit-life)+" lifes")
			print()
			life+=1
			function0(life,life_limit)			
		elif g_number<s_number:
			print()
			print(" INSHA'ALLAAH, you will do it next time !")
			print()
			print("you have "+str(life_limit-life)+" lifes")
			print()
			life+=1
			function0(life,life_limit)

	else:
		print("You Losse !!! number was "+str(s_number))
		print()

		#do u want to play again?
		while True:
			print("Do you want to play again ?(y/n)")
			aggrement= input()
			if aggrement.lower()=="y":
				print("                         <in this game you will have one help chance>                       ")
				print()
				s_number=random.randint(0,7)
				life=0
				life_limit=3
				help_=0
				help_limit=1

				print("Please guess a number among 0-7: ")
				g_number=int(input())
				function4(help_,help_limit)
			else:
				print("____________________")
				print("Thanks for Guessing")
				print("------- :) ---------")
				exit()
def function2(help_,help_limit):
	global life,life_limit
	while help_==help_limit:
		if g_number==s_number:
			print()
			print("MASHA'ALLAAH, You have done a great job.")
			print()
			exit()
		else:	
			print()
			print("wrong!!!! you have no help & "+str(life_limit-life)+" lifes !")
			print()
			life+=1
			break
	function1(life,life_limit)
	function3(life,life_limit)


def function1(life,life_limit):
	global g_number
	if life<life_limit:

		print("Please guess among 0-7 :")
		g_number=int(input())

def function5(life,life_limit):
	life=0
	life_limit=3
	help_=0
	help_limit=1

def function4(help_,help_limit):
	global g_number,s_number
	if g_number==s_number:
		print()
		print(" MASHA'ALLAAH, You have done a great job .")
		while True:
			print("Do you want to play again ?(y/n)")
			aggrement= input()
			if aggrement.lower()=="y":
				print("                         <in this game you will have one help chance>                       ")
				print()
				s_number=random.randint(0,7)
				function5(life,life_limit)

				print("Please guess a number among 0-7: ")
				g_number=int(input())
				function4(help_,help_limit)
			else:
				print("____________________")
				print("Thanks for Guessing")
				print("------- :) ---------")
				exit()

	elif g_number>s_number or g_number<s_number:

		if(g_number>s_number):
			print()

			if help_<help_limit :
				print("your guess is higher")
				help_+=1

			function1(life,life_limit)	
			function2(help_,help_limit)
						
		elif(g_number<s_number):
			print()
			if help_<help_limit :
				print("Your guess is lower")
				help_+=1
			function1(life,life_limit)	
			function2(help_,help_limit)

			# function1(life,life_limit)


if help_==0:
	function4(help_,help_limit)

print()