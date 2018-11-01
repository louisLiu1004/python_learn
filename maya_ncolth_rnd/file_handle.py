# -*- coding: utf-8 -*-
"""
@author: 刘国财
@software: PyCharm 2018.1
@file: file_handle.py
@time: 2018/10/31 11:00
"""

import datetime, os, shutil
import maya.cmds as  mc


def file_check(dir, name):
    if os.path.isdir(dir):
        file_creat_time = datetime.datetime.fromtimestamp(os.path.getctime(dir)).strftime('%Y%m%d_%H-%M-%S')
        folder__name = file_creat_time + '_' + name
        print(dir)
        print(os.path.dirname(dir))
        print(os.path.join(os.path.dirname(dir), folder__name))
        shutil.move(dir, os.path.join(os.path.dirname(dir), folder__name))


def file_save(dir, node):
    with open(dir + '\\attrbute.txt', 'w') as f:
        f.write('stretchResistance' + ':' + str(mc.getAttr(node + '.stretchResistance')) + '\n')
        f.write('compressionResistance' + ':' + str(mc.getAttr(node + '.compressionResistance')) + '\n')
        f.write('bendResistance' + ':' + str(mc.getAttr(node + '.bendResistance')) + '\n')
        f.write('bendAngleDropoff' + ':' + str(mc.getAttr(node + '.bendAngleDropoff')) + '\n')
        f.write('shearResistance' + ':' + str(mc.getAttr(node + '.shearResistance')) + '\n')
        f.write('restitutionAngle' + ':' + str(mc.getAttr(node + '.restitutionAngle')) + '\n')
        f.write('restitutionTension' + ':' + str(mc.getAttr(node + '.restitutionTension')) + '\n')
        f.write('rigidity' + ':' + str(mc.getAttr(node + '.rigidity')) + '\n')
        f.write('deformResistance' + ':' + str(mc.getAttr(node + '.deformResistance')) + '\n')
        f.write('inputMeshAttract' + ':' + str(mc.getAttr(node + '.inputMeshAttract')) + '\n')
        f.write('inputAttractDamp' + ':' + str(mc.getAttr(node + '.inputAttractDamp')) + '\n')
        f.write('inputMotionDrag' + ':' + str(mc.getAttr(node + '.inputMotionDrag')) + '\n')
        f.write('restLengthScale' + ':' + str(mc.getAttr(node + '.restLengthScale')) + '\n')
        f.write('bendAngleScale' + ':' + str(mc.getAttr(node + '.bendAngleScale')) + '\n')
        f.write('pointMass' + ':' + str(mc.getAttr(node + '.pointMass')) + '\n')
        f.write('lift' + ':' + str(mc.getAttr(node + '.lift')) + '\n')
        f.write('drag' + ':' + str(mc.getAttr(node + '.drag')) + '\n')
        f.write('tangentialDrag' + ':' + str(mc.getAttr(node + '.tangentialDrag')) + '\n')
        f.write('damp' + ':' + str(mc.getAttr(node + '.damp')) + '\n')
        f.write('stretchDamp' + ':' + str(mc.getAttr(node + '.stretchDamp')) + '\n')
