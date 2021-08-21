import turtle
import os
import math
import random

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
#wn.bgpic("space_invaders_background.gif")

#Register the shapes
#turtle.register_shape("invader.gif")
#turtle.register_shape("player.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-250,-250)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(500)
	border_pen.lt(90)
border_pen.hideturtle()	

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-270, 260)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
player.setposition(0, -230)
player.setheading(90)
player.speed = 0

#Choose a number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
	#Create the enemy
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("red")
	enemy.shape("turtle")
	enemy.penup()
	enemy.speed(0)
	enemy.setheading(270)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)

enemyspeed = 5


#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"


#Move the player left and right
def move_left():
	player.speed = -15

def move_right():
	player.speed = 15
	
def player_movement():
	x = player.xcor()
	x += player.speed
	if x > 230:
		x = 230
	if x < -230:
		x = - 230
	player.setx(x)
def fire_bullet():
	#Declare bulletstate as a global if it needs changed
	global bulletstate
	if bulletstate == "ready":
		#os.system("afplay laser.wav&")
		bulletstate = "fire"
		#Move the bullet to the just above the player
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()

#bullet_enemy_collision
def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False
#Create keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

#Main game loop
while True:
	

	player_movement()

	for enemy in enemies:
		#Move the enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#Move the enemy back and down
		if enemy.xcor() > 230:
			#Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 20
				e.sety(y)
			#Change enemy direction
			enemyspeed *= -1
		
		if enemy.xcor() < -230:
			#Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 20
				e.sety(y)
			#Change enemy direction
			enemyspeed *= -1
			
		#Check for a collision between the bullet and the enemy
		if isCollision(bullet, enemy):
			#os.system("afplay explosion.wav&")
			#Reset the bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			#Reset the enemy
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)
			#Update the score
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
		if isCollision(player, enemy):
			#os.system("afplay explosion.wav&")
			player.hideturtle()
			enemy.hideturtle()
			print ("Game Over")
			break

		#enemy increment
		    
	#Move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
	
	#Check to see if the bullet has gone to the top
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"

wn.update()