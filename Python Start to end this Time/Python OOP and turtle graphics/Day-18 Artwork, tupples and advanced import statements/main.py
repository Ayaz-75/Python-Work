from turtle import Turtle, Screen
# from turtle import Turtle as t, Screen as s

timmy = Turtle()
# #######################
# timmy.shape("turtle")
# timmy.color('green')
# def move_90():
#     timmy.fd(100)
#     timmy.right(90)
#     timmy.fd(100)
# #######################
# move_90()
# timmy.right(90)
# move_90()
# #######################
# for tim in range(4):
#     timmy.fd(100)
#     timmy.left(90)
# #######################
# screen = Screen()
# screen.exitonclick()
# screen.mainloop()

for _ in range(10):
    timmy.fd(10)
    timmy.pu()
    timmy.fd(10)
    timmy.pd()


screen = Screen()
screen.exitonclick()
screen.mainloop()

print("Done")
