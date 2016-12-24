# mouse speed by kevdotcom

import os
import sys
import time

global turn
global low
global mid
global high
global lap
turn = 0
low = 0
mid = 0
high = 0
lap = 0

def start():
	os.system('cls' if os.name == 'nt' else 'clear')
	global turn
	global low
	global mid
	global high

	print (46 * '-')
	print (' Welcome to the Mouse Sensitivity Calculator.')
	print (46 * '-')
	turn = float(raw_input(' Enter your 360 Sensitivity: '))
	low = turn * .5
	mid = turn
	high = turn * 1.5
	try:
		turn = float(turn)
	except:
		start()
	if turn > 0:
		calc()
	else:
		start()


def calc():
	os.system('cls' if os.name == 'nt' else 'clear')
	global turn
	global low
	global mid
	global high
	global lap



	# print"360: ", float(turn)
	while high - low > 0.1:
		os.system('cls' if os.name == 'nt' else 'clear')
		print (31 * '-')
		print (' Mouse Sensitivity Calculator.')
		print (31 * '-')
		print (31 * '-')
		print " High Sensitivity: ", float(high)
		print " Mid Sensitivity: ", float(mid)
		print " Low Sensitivity: ", float(low)
		print (52 * '-')
		print " Try out the Low and High Setting for 5 Minutes."
		print " Then choose the one you aim more comfortably with."
		print " Repeat this until you can't spot a difference anymore."
		# print " Lap: ", lap
		print (52 * '-')
		choice = int(input(" Enter 1 for Low or 2 for High..."))

		if choice == 1:
			high = mid
			if lap == 0:
				low = low * .8
			if lap >= 1:
				low = low * .95
			mid = (mid + low) * .5
			lap = lap + 1

		if choice == 2:
			low = mid
			if lap == 0:
				high = high * 1.2
			if lap >= 1:
				high = high * 1.05
			mid = (mid + high) * .5
			lap =+ 1
		
		else:
			calc()

		calc()

	start()

start()