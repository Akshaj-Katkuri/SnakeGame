import turtle
import random
import time
import winsound

wn = turtle.Screen()

# To play sound file
winsound.PlaySound("SBMusic.wav", winsound.SND_ASYNC)

with open("alltime_hs.txt", 'r') as f:
    at_highscore = f.read()
at_highscore = int(at_highscore)

# variables
wn.bgcolor("Green")
wn.setup(width=600, height=600)
wn.title("Snake Game")
wn.tracer(0)
delay = 0.2
score = 0
lives = 3
high_score = 0
body = []

# Start up text turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.clear()
pen.pu()
pen.color("Gold")
pen.write("Snake Game", align='center', font=('Times Roman', 65, 'bold'))
time.sleep(1)
pen.clear()
pen.write("Get ready to play", align='center', font=('Times Roman', 30, 'bold'))
time.sleep(1.5)
pen.clear()
for i in range(5, 0, -1):
    pen.clear()
    pen.write(f"{i}", align='center', font=('Times Roman', 150, 'bold'))
    time.sleep(1)
pen.clear()
pen.write("Gooo.....", align='center', font=('Times Roman', 30, 'bold'))
time.sleep(1)
pen.clear()

# food turtle

food = turtle.Turtle()
food.pu()
food.shape("circle")
food.color("Red")


def randomize():
    x = random.randint(-285, 285)
    y = random.randint(-285, 285)
    food.hideturtle()
    food.goto(x, y)
    food.showturtle()


randomize()
# snake turtle

sn = turtle.Turtle()
sn.pu()
sn.shape("triangle")
sn.color("deepskyblue")
sn.direction = 'stop'


def move_snake():
    if sn.direction == 'up':
        y = sn.ycor()
        sn.sety(y + 20)
    if sn.direction == 'down':
        y = sn.ycor()
        sn.sety(y - 20)
    if sn.direction == 'right':
        x = sn.xcor()
        sn.setx(x + 20)
    if sn.direction == 'left':
        x = sn.xcor()
        sn.setx(x - 20)


def left():
    if sn.direction != 'right':
        sn.direction = 'left'
        sn.setheading(180)


def right():
    if sn.direction != 'left':
        sn.direction = 'right'
        sn.setheading(0)


def up():
    if sn.direction != 'down':
        sn.direction = 'up'
        sn.setheading(90)


def down():
    if sn.direction != 'up':
        sn.direction = 'down'
        sn.setheading(270)


def respawn():
    time.sleep(1)
    sn.goto(0, 0)
    randomize()
    winsound.PlaySound("error.wav", winsound.SND_ASYNC)
    sn.setheading(0)
    sn.direction = 'stop'


wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(down, "Down")
wn.onkeypress(up, "Up")
pen.goto(0, 260)
pen.clear()
pen.write(f"Score = {score}, High Score = {high_score}, Lives = {lives}", align='center',
          font=('Times Roman', 20, 'bold'))

while True:
    wn.update()
    time.sleep(delay)
    if sn.ycor() > 290 or sn.ycor() < -290 or sn.xcor() > 290 or sn.xcor() < -290:
        lives -= 1
        for i in body:
            i.goto(400, 400)
        body.clear()
        if lives == 0:
            pen.clear()
            pen.goto(0, 70)
            pen.write("Gameover", align='center', font=('Times Roman', 65, 'bold'))
            pen.goto(0, -5)
            pen.write(
                f"Score = {score}, High Score = {high_score}, Lives = {lives}, Alltime High Score = {at_highscore}",
                align='center', font=('Times Roman', 10, 'bold'))
            sn.goto(-400, -400)
            food.goto(400, -400)
            winsound.PlaySound("Congratulations.wav", winsound.SND_ASYNC)
            break
        respawn()
        score = 0
    if sn.distance(food) < 20:
        score += 1
        if score > high_score:
            high_score = score
        if high_score > at_highscore:
            at_highscore = high_score
            with open('alltime_hs.txt', 'wr') as f:
                f.write(str(at_highscore))
        pen.clear()
        pen.write(f"Score = {score}, High Score = {high_score}, Lives = {lives}", align='center',
                  font=('Times Roman', 20, 'bold'))
        winsound.PlaySound("Eat.wav", winsound.SND_ASYNC)
        randomize()
        new = turtle.Turtle()
        body.append(new)
        new.pu()
        new.speed(0)
        new.shape("square")
        new.color("darkblue")

    for i in range(len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)
    if len(body) > 0:
        x = sn.xcor()
        y = sn.ycor()
        body[0].goto(x, y)
    move_snake()
    for i in body:
        if i.distance(sn) < 20:
            lives -= 1
            for i in body:
                i.goto(400, 400)
            body.clear()
            if lives == 0:
                pen.clear()
                pen.goto(0, 70)
                pen.write("Gameover", align='center', font=('Times Roman', 65, 'bold'))
                pen.goto(0, -5)
                pen.write(
                    f"Score = {score}, High Score = {high_score}, Lives = {lives}, Alltime High Score = {at_highscore}",
                    align='center',
                    font=('Times Roman', 20, 'bold'))
                sn.goto(-400, -400)
                food.goto(400, -400)
                winsound.PlaySound("Congratulations.wav", winsound.SND_ASYNC)
                break
            respawn()
            score = 0

wn.mainloop()
