import random

def doors_init():
	doors=[1,0,0]
	random.shuffle(doors)
	return doors


def player_first_step():
	player_choice =  random.randint(0,2)	
	return player_choice

def host_step(doors, player_choice):     
	while True:
		host_choice = random.randint(0,2)
		if host_choice == player_choice:
			continue
		if doors[host_choice] == 1:
			continue
		break	
	return host_choice

def player_second_step(doors, host_choice, player_choice, mode):   
	if mode == 0:
		player_choice = player_choice #don't change
	if mode == 1:
		set_choices = {0,1,2}
		set_choices.remove(player_choice)
		set_choices.remove(host_choice)
		player_choice = set_choices.pop()
	if doors[player_choice] == 1:		return True
	else:
		return False

def simulation(size):      
        count_NotChange = 0
        count_Change = 0
        print size, "iterations begin"
        for i in range(size):
                doors = doors_init()
                player_choice = player_first_step()
                host_choice = host_step(doors, player_choice)
                if player_second_step(doors, host_choice, player_choice, 1):
                        count_Change += 1
                if player_second_step(doors, host_choice, player_choice, 2):
                        count_NotChange += 1                      
        return (count_Change, count_NotChange)

size = 100000
(count_Change, count_NotChange) = simulation(size)
print "If change the choice, then win percent:",float(count_Change)/size
print "If don't change the choice, then win percent:",float(count_NotChange)/size
