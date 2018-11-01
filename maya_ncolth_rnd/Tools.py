# -*- coding: utf-8 -*-
"""
@author: 刘国财
@software: PyCharm 2018.1
@file: Tools.py
@time: 2018/10/30 13:28
"""

import maya.cmds as mc


def get_project_path():
    return mc.workspace(q=True, fn=True)
