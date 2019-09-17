'''
1. Búa til breytur til að geyma kortið
2. Búa til pos breytu
3. Búa til function sem segir manni hvar hann má fara og leyfir notenda að gera það
4. Búa til if og else clause sem kemur í veg fyrir error-a
5. Búa til while loopu-sem keyrir á meðan notandi er ekki búinn að vinna
'''
def move_n(x, y):
	y += 1
	return x, y

def move_e(x, y):
	x += 1
	return x, y

def move_s(x, y):
	y -= 1
	return x, y

def move_w(x, y):
	x -= 1
	return x, y

def nav(n, e, s, w):
	choice = input("Direction: ")
	if n and choice == "n" or choice == "N":
		return move_n(x, y)
	if e and choice == "e" or choice == "N":
		return move_e(x, y)
	if s and choice == "s" or choice == "S":
		return move_s(x, y)
	if w and choice == "w" or choice == "W":
		return move_w(x, y)


def options(x, y):
	North = False
	South = False
	East = False
	West = False
	
	if x == 1 and y == 1:
		North = True
		print("You can travel: (N)orth.")
		return North, East, South, West
	elif x == 1 and y == 2:
		North = True
		South = True
		East = True
		print("You can travel: (N)orth or (E)ast or (S)outh.")
		return North, East, South, West
		
	elif x == 1 and y == 3:
		South = True
		East = True
		print("You can travel: (E)ast or (S)outh.")
		return North, East, South, West
		
	elif x == 2 and y == 1:
		North = True
		print("You can travel: (N)orth.")
		return North, East, South, West
		
	elif x == 2 and y == 2:
		West = True
		South = True
		print("You can travel: (S)outh or (W)est.")
		return North, East, South, West
	
	elif x == 2 and y == 3:
		West = True
		East = True
		print("You can travel: (E)ast or (W)est.")
		return North, East, South, West
	
	elif x == 3 and y == 2:
		North = True
		South = True
		print("You can travel: (N)orth or (S)outh.")
		return North, East, South, West
		
	elif x == 3 and y == 3:
		West = True
		South = True
		print("You can travel: (S)outh or (W)est.")
		return North, East, South, West


x = 1
y = 1

while x != 3 and y != 1:
	options(x, y)
	print(nav(options))