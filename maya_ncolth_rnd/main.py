# -*- coding: utf-8 -*-
"""
@author: 刘国财
@software: PyCharm 2018.1
@file: main.py
@time: 2018/10/30 11:26
"""
import maya.cmds as mc
import ncolth_rnd as rnd


reload(rnd)


def _exec():
    if mc.window('Ncloth_win', q=True, exists=True):
        mc.deleteUI('Ncloth_win')
    win = rnd.MyWin()
    win.show()



