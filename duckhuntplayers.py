#This module contains all the player classes and their respecsctive helper classes.
##====================================================
class Player(object):
	
	#Player class constructor
	def __init__(self):
		
		#Initializes score to zero.
		self.score = 0
		self.name = "P"
		
		self.num_bullets = 3
	
	#Returns a 2-tuple with the location at which
	#the player shot at the screen.
	def shot_at(self):
		return (0,0)
		
	def update_score(self, points):
		self.score += points
		
	def update(self):
		pass
		
	def getName(self):
		pass
		
	def __eq__(self , other):
		self.name == other.name
		
	def get_num_bullets(self):
		return self.num_bullets
		
	def get_score(self):
		return self.score
		
	def clear_score(self):
		self.score = 0
	

##====================================================

##====================================================
class InteractivePlayer(Player):
	
	#Player class constructor
	def __init__(self):
		Player.__init__(self)
		self.name = "P1"
		
	#Returns a 2-tuple with the location at which
	#the player shot at the screen.
	def shot_at(self, event):
		self.num_bullets -= 1
		return event.pos
		
	def update(self):
		pass
		
	def getName(self):
		return self.name

##====================================================

##====================================================
#Class that represents the robot that will play as this game's player.
class Robot(Player):
	
	def __init__(self):
		Player.__init__(self)
		self.name = "R"
		
	def shot_at(self):
		return (0,0)
		
	def update():
		pass
		
##====================================================