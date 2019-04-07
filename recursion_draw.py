import turtle
import random

myTurtle = turtle.Turtle()
myWin = myTurtle.screen


def draw_spiral(myTurtle, linelen):
    if linelen > 0:
        myTurtle.forward(linelen)
        myTurtle.right(90)
        draw_spiral(myTurtle, linelen - 5)


# draw_spiral(myTurtle, 150)
# myWin.exitonclick()


def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-15, t)
        t.right(20)
        t.backward(branchLen)


def tree_2(branchLen, t):
    t.width(branchLen * 0.04)
    if branchLen > 5:
        t.width(branchLen * 0.04)
        rand = random.randint(1, 100)
        t.forward(branchLen)
        t.right(rand)
        tree(branchLen - 15, t)
        t.left(rand)
        tree(branchLen - 15, t)
        t.right(rand)
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree_2(100, t)
    myWin.exitonclick()


main()

