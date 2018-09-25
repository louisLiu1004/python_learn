# coding: utf-8 
__author__ = '財'
__time__ = '2018/9/21 21:31'

import turtle

def regular_polygon(side_nums, side_length):
    if side_nums >= 3 and side_length > 0:
        for i in range(side_nums):
            draw.forward(side_length)
            draw.left(360.0 / side_nums)
    else:
        print('side_nums, side_length ERROR')
        for i in range(3):
            draw.forward(20)
            draw.left(360.0 / 3)


if __name__ == '__main__':
    draw = turtle.Turtle()
    while 1:
        try:
            nums, length = int(float(raw_input('nums:'))), float(raw_input('length:'))
            regular_polygon(nums, length)
            break
        except ValueError:
            print('please Don\'t enter characters other than numbers')

    turtle.done()
