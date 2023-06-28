import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(5)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15  # Ball's x-axis speed
ball.dy = -0.15  # Ball's y-axis speed

# Bricks
bricks = []
colors = ["yellow", "yellow", "green", "green", "orange", "orange", "red", "red"]
for row in range(4):
    for column in range(8):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        x = -350 + column * 100
        y = 250 - row * 40
        brick.goto(x, y)
        bricks.append(brick)

# Score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(-350, 260)
score_pen.write("Score: 0", align="left", font=("Courier", 16, "normal"))


# Move the paddle
def move_paddle_left():
    x = paddle.xcor()
    if x > -340:
        x -= 20
    paddle.setx(x)


def move_paddle_right():
    x = paddle.xcor()
    if x < 340:
        x += 20
    paddle.setx(x)


# Keyboard bindings
screen.listen()
screen.onkeypress(move_paddle_left, "Left")
screen.onkeypress(move_paddle_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball and wall collisions
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Ball and paddle collision
    if (ball.ycor() < -240) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Ball and brick collisions
    for brick in bricks:
        if brick.distance(ball) < 40:
            brick.goto(1000, 1000)  # Move brick off the screen
            bricks.remove(brick)  # Remove brick from the list
            score += 1
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="left", font=("Courier", 16, "normal"))

    # Game over condition

