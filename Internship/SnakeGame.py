import turtle
import time
import random

delay = 0.1 
score  = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0 High Score : 0",align = "center", font=("Courier", 24,"normal"))

# Functions to move Snake
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"
        
def go_left():
    if head.direction != "right":
        head.direction = "left"
        
def go_right():
    if head.direction != "left":
        head.direction = "right"
        
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
# Keyboard bindings

wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

# Main game loop
try:
    while True:
        wn.update()
    
    # Check for collision with the border
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
               time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        # Hide the segments
        for segment in segments:
            segment.goto(1000,1000)
            
        segments.clear()
        score = 0
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score,high_score), align = "center", font=("Courier", 24, "normal"))
        
        # Check for collision with food
    
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)
        
        score += 10
        if score > high_score:
            high_score = score
            
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score,high_score), align= "center", font= ("Courier", 24, "normal"))
        
        # Move the segments first in reverse order
        
    for index in range(len(segments) -1 , 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
        
        # Move the segments 0 to where the head is
        
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        
    move()
    # Check fo collision with the body
    
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            # Hide the segments 
            for segment in segments:
                segment.goto(1000,1000)
                
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score : {} High Score : {}".format(score,high_score), align = "center", font=("Courier", 24, "normal"))
    time.sleep(delay)
    

except turtle.Terminator:
    print("Game Over: Turtle window was closed.")   
    
wn.mainloop()

        
# 