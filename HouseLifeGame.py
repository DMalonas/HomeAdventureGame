import time


def valid_input(prompt, options):
	while True:
		response = input(prompt).lower()
		for option in options:
			if option in response:
				return option
		print_pause("Sorry, I don't understand.")

		
		
		
def garden(items, times):
	valid_garden_inputs = ["1", "2", "3", "4"]
	if times == 0:
		print("You unlock the door and get out\n"
			  "in the garden. The air is cool. You\n"
			  "have many different plants that need\n"
			  "taken care of.\n")
		times = 1
	print("You are in the garden\n")
	response = valid_input("What do you want to do?\n"
			  "1. Water the flowers\n"
			  "2. Pick up crops\n"
			  "3. Transfer lillies in a bigger pot\n"
			  "4. Go inside\n", valid_garden_inputs)
	if response == "1":
		print("You water the flowers\n")
	elif response == "2":
		print("You need a basket. You recall\n"
			  "seeing your basket inside the shelf\n"
			  "under the sink\n")
	else:
		return

		
def kitchen(items, times):
	valid_kitchen_inputs = ["1", "2", "3", "4"]
	if times == 0:
		times = 1
		print("You are standing in the kitchen\n"
		"in front of the sink. On your left\n"
		"your left you have a kettle, and on\n"
		"your right the stove\n")
	else:
		print("You are standing in the kitchen\n"
		     "in front of the sink\n")
	response = valid_input("What do you want to do?\n"
				"1. Make tea\n"
				"2. Cook breakfast\n"
				"3. Get the basket\n"
				"   that is in the\n"
				"   shelf under the\n"
				"   sink\n"
				"4. Go to the living room\n", valid_kitchen_inputs)
	if response == "1":
		if "cup" in items:
			print("You already had a cup of tea\n"
			      "Drinking more could upset your\n"
				  "stomach.")
		else:
			items.append("cup")
			print("You pick up your cup. You boil\n"
   			    "some water in the kettle and then\n"
  				"prepare some jasmine tea. You enjoy \n"
				"it with a piece of chocolate.\n")
	elif response == "2":
		if "pan" not in items:
			items.append("pan")
			print("You use your new copper pan\n"
			      "to cook breakfast. You slow\n"
				  "fry in olive olive five tomatoes\n"
				  "cut in half. You also add one whole\n"
				  "garlic finely chopped, as well as \n"
				  "black pepper, and salt. In the end\n"
				  "you add four eggs on top of that mix\n"
				  "and you allow them to get cooked but \n"
				  "not too much. You enjoy your breakfast.\n")
		else:
			print("You already had breakfast.\n"
				  "Eating again would not be the\n"
				  "healthiest choice\n")
			if "cup" in items:
				print("You could do some activity\n"
					  "I believe that there are lot of \n"
					  "unfinished activities left in\n"
					  "the garden.")
			else:
				print("You could have a cup of tea with\n"
				      "some chocolate for dessert\n")
	elif response == "3":
		if "basket" in items:
			print("You have already taken the basket\n"
			      "out of the shelf\n")
		else:
			items.append("bakset")
			print("You pick up the basket\n")
	else:
		living_room(items, 1)
	kitchen(items, 1)
	
def living_room(items, times):
	accepted_living_room_inputs = ["1", "2", "3"]
	if times == 1:
		print("You are standing in the living room\n"
			  "in front of the door to the garden\n")

	response = valid_input("What do you want to do?\n"
		"1. Go out\n"
		"2. Sit down\n"
		"3. Go to the kitchen\n", accepted_living_room_inputs)

	if response == "1":
		if "keys" in items:
			garden(items, 0)
		else:
			print("You dont have keys and the door is locked\n")
			living_room(items, 0)
	elif response == "2":
		desk(items, 0)
	else:
		kitchen(items, 0)
	

	
def desk(items, times):
		
	valid_desk_inputs = ["1", "2", "3"]
	if times == 0:
		if "keys" not in items:
			print("You sit down on your desk,\n"
				  "that is next to the window.In\n"
				  "a little box on your right you\n"
				  "see the keys for the garden door.\n"
				  "as well as some pencils and papers\n")
		else:
			print("You sit down on your desk,\n"
				  "that is next to the window.In\n"
				  "front of you, you see the paper\n"
				  "with the drawings you did earlier.\n")

		times = 1
	if "keys" not in items:
		response = valid_input("1. Pick keys up\n"
						"2. Draw a picture\n"
						"3. Stand up\n", valid_desk_inputs)
		if response == "1":
			print("You pick up the keys and put\n"
				   "them in your pocket\n")
			items.append("keys")
		elif response == "2":
			print("You do some drawing")
		elif response == "3":
			living_room(items, 1)
		desk(items, times)
	else:
		response =valid_input("1. Draw a picture\n"
			  "2. Stand up\n", ["1", "2"])
		if response == "1":
			print("You have no more paper left")
			desk(items, times)
		else:
			living_room(items, 1)

def instructions(times):
	if times == 0:
		times = 1
		print_pause("Welcome to GARDEN!\n\n"
				"Developed by Dimitrios Malonas\n"
				)
	print_pause("\nTo play the game you make choices\n"
			    "based on the different menu options.\n"
			    "To see what you are carrying at any\n"
				"moment type inventory. Beyond the menu\n"
				"options you can try using short phrases,\n"
				"such  as Drink water, or Take break, for\n" 
				"additional activities.\n")
	response = valid_input("Do you need more instructions?\n"
				"1. Yes\n2. No\n", ["yes", "no"])
	if response == "yes":
		instructions(times)
	
	
def intro(items):
	print_pause("You are going to spend a Saturday morning"
				"\nrelaxing at home. It is a sunny day.\n"
				"\nYou are standing in the living room in\n"	
				"\nfront of the door that leads to the garden\n")
	living_room(items, 0)
























def print_pause(string_input):
	time.sleep(1)
	print(string_input.center(40))
	print("\n")


def play_game():
	times = 0
	items = []

	instructions(times)
	intro(items)
	






play_game()