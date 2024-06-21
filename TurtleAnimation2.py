import turtle
import random

# Create a turtle screen
screen = turtle.Screen()
screen.setup(width=800, height=600)

# Draw a racing track
track_turtle = turtle.Turtle()
track_turtle.speed(0)  # Fastest speed
track_turtle.hideturtle()

track_turtle.penup()
track_turtle.goto(0, -200)
track_turtle.pendown()

track_turtle.circle(200)  # Draw a circle for the track

# Draw start and finish lines
track_turtle.penup()
track_turtle.goto(-200, 200)
track_turtle.pendown()
track_turtle.goto(200, 200)  # Draw a line for the start point

track_turtle.penup()
track_turtle.goto(-200, -200)
track_turtle.pendown()
track_turtle.goto(200, -200)  # Draw a line for the finish point

# Create multiple turtles for racing
racers = []
colors = ["red", "green", "blue", "yellow", "orange"]

for i in range(5):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(colors[i])
    racer.penup()
    racer.goto(-200, 150 - (i * 50))  # Position at the start line
    racer.setheading(0)  # Face toward the finish line
    racers.append(racer)

# Set random speeds for each turtle
for racer in racers:
    speed = random.randint(1, 5)
    racer.speed(speed)

# Move turtles forward
finish_line = 200
winner = None

while winner is None:
    for racer in racers:
        distance = random.randint(5, 20)
        racer.forward(distance)
        if racer.xcor() >= finish_line:
            winner = racer
            break

# Print the winner
print(f"The winner is the {winner.color()[0]} turtle!")

# Keep the window open
turtle.done()