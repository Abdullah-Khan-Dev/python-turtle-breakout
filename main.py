import turtle
import time

# Setup the screen
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -230)
ball.dx = 0.15
ball.dy = -0.15

# Bricks
bricks = []

brick_colors = ["red", "orange", "yellow", "green", "blue"]
y_pos = 250
for color in brick_colors:
    for i in range(-350, 400, 100):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(color)
        brick.shapesize(stretch_wid=1, stretch_len=5)
        brick.penup()
        brick.goto(i, y_pos)
        bricks.append(brick)
    y_pos -= 30


# Functions to move the paddle
def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -350:
        x = -350
    paddle.setx(x)


def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 350:
        x = 350
    paddle.setx(x)


# Keyboard bindings
win.listen()
win.onkeypress(paddle_left, "Left")
win.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision detection
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.goto(0, -230)
        ball.dy *= -1

    # Paddle collision detection
    if (ball.dy < 0) and (paddle.ycor() + 10 > ball.ycor() > paddle.ycor() - 10) and (
            paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(paddle.ycor() + 10)
        ball.dy *= -1

    # Brick collision detection
    for brick in bricks:
        if (ball.dy > 0) and (brick.ycor() - 10 < ball.ycor() < brick.ycor() + 10) and (
                brick.xcor() - 50 < ball.xcor() < brick.xcor() + 50):
            brick.goto(1000, 1000)
            bricks.remove(brick)
            ball.dy *= -1
            break

    # Delay
    time.sleep(0.01)
