'''
1. Búa til breytur til að geyma kortið
2. Búa til pos breytu
3. Búa til function sem segir manni hvar hann má fara og leyfir notenda að gera það
4. Búa til if og else clause sem kemur í veg fyrir error-a
5. Búa til while loopu-sem keyrir á meðan notandi er ekki búinn að vinna
'''

def nav(x, y, z):
    return 0

def options(x, y):
	North = False
	South = False
	East = False
	West = False
	
	if x == 1 and y == 1:
		North = True
		return North
	elif x == 1 and y == 2:
		North = True
		South = True
		East = True
		return North, South, East
		
	elif x == 1 and y == 3:
		South = True
		East = True
		return South, East
		
	elif x == 2 and y == 1:
		North = True
		return North
		
	elif x == 2 and y == 2:
		West = True
		South = True
		return West, South
	
	elif x == 2 and y == 3:
		West = True
		East = True
		return West, East
	
	elif x == 3 and y == 2:
		North = True
		South = True
		return North, South
		
	elif x == 3 and y == 3:
		West = True
		South = True
		return West, South

    return 0

x = 1
y = 1

while x != 3 and y != 1:
	options(x, y)
	print(nav(options))