from turtle import Turtle

# Задать параметры))
eye_color = "green"
whiskers_lenth = 225

t = Turtle()
t.speed(0)
t.screen.setup(1200, 800)
t.screen.bgcolor("black")
t.shape("turtle")

t.up()
t.forward(80)

# Глаза
t.begin_fill()
t.fillcolor(eye_color)
t.down()
t.circle(50, 360)
t.up()
t.end_fill()
t.left(90)
t.forward(20)
t.down()
t.right(90)
t.begin_fill()
t.fillcolor("black")
t.circle(30, 360)
t.end_fill()
t.right(90)
t.up()
t.forward(20)

t.right(90)
t.forward(200)
t.right(180)

t.begin_fill()
t.fillcolor(eye_color)
t.down()
t.circle(50, 360)
t.up()
t.end_fill()
t.left(90)
t.forward(20)
t.down()
t.right(90)
t.begin_fill()
t.fillcolor("black")
t.circle(30, 360)
t.end_fill()
t.right(90)
t.up()
t.forward(20)

# Нос
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.down()
t.fillcolor("pink")
t.begin_fill()
t.left(90)
t.forward(30)
t.right(150)
t.forward(42.43)
t.right(60)
t.forward(42.43)
t.right(150)
t.end_fill()
t.forward(50)

# Ухо1
t.pencolor("white")
t.up()
t.forward(50)
t.left(90)
t.forward(180)
t.right(50)
t.down()
t.forward(134.16)
t.right(126)
t.forward(134.16)

# Щека1
t.left(20)
t.forward(150)
t.right(85)
t.forward(180)
t.setheading(180)
t.forward(20)
t.setheading(270)

# Язык
t.fillcolor("purple")
t.pencolor("purple")
t.begin_fill()
t.circle(-50, 180)
t.end_fill()
t.pencolor("white")

# Щека2
t.setheading(180)
t.forward(20)
t.setheading(151)
t.forward(180)
t.right(85)
t.forward(150)

# Ухо2
t.setheading(86)
t.forward(134.16)
t.setheading(-40)
t.forward(134.16)
t.setheading(0)
t.forward(109)

# Усы справа
t.setheading(270)
t.up()
t.forward(200)
t.setheading(25)
t.down()
t.forward(whiskers_lenth)
t.up()
t.setheading(205)
t.forward(whiskers_lenth)

t.setheading(270)
t.forward(10)
t.setheading(0)
t.down()
t.forward(whiskers_lenth)
t.up()
t.setheading(180)
t.forward(whiskers_lenth)

t.setheading(270)
t.forward(10)
t.setheading(-25)
t.down()
t.forward(whiskers_lenth)
t.up()
t.setheading(-205)
t.forward(whiskers_lenth)

# Усы слева
t.setheading(180)
t.forward(120)
t.setheading(205)
t.down()
t.forward(whiskers_lenth)
t.up()
t.setheading(25)
t.forward(whiskers_lenth)

t.setheading(-270)
t.forward(10)
t.setheading(180)
t.down()
t.forward(whiskers_lenth)
t.up()
t.setheading(0)
t.forward(whiskers_lenth)

t.setheading(-270)
t.forward(10)
t.setheading(155)
t.down()
t.forward(whiskers_lenth)
t.up()
t.setheading(-25)
t.forward(whiskers_lenth)

t.ht()
t.screen.exitonclick()
t.screen.mainloop()
