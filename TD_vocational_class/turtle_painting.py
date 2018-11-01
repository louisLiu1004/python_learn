# coding: utf-8 
__author__ = '財'
__time__ = '2018/9/15 17:40'
import turtle


def little_star(index):
    screen.begin_fill()
    for i in range(5):
        screen.forward(index)
        screen.left(216)
    screen.end_fill()

def big_star(index):
    for i in range(5):
        screen.forward(100)
        little_star(index)
        screen.forward(index)
        screen.left(216)


if __name__ == '__main__':
    screen = turtle.Turtle()
    screen.color('blue', 'yellow')
    big_star(30)
    turtle.done()
