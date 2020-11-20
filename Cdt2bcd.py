#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Cdt2bcd
# An Experimental Command Line Tool To Try And Convert Super Mario Maker 1 Course Data Table Files (course_data.cdt, course_data_sub.cdt) To Super Mario Maker 2 Format (course_data_000.bcd).
# Version 0.2
# Created By MarioPossamato With Help From Tarnadas (https://github.com/Tarnadas)

# This File Is Part Of Cdt2bcd.

#==== Module and library imports ====#
import sys             # Built-in module
import os              # Built-in module
import io              # Built-in module
import Encryption
#====================================#
# Super Mario Maker Course
class SuperMarioMaker1Course(dict):
    def __init__(self):
        pass
    class Sprite(dict):
        def __init__(self):
            pass
        def Load(self, data):
            self['SpritePositionXAxis'] = data[0x0:0x4]           #==== Sprite X Position ====#
            self['SpritePositionZAxis'] = data[0x4:0x8]           #==== Sprite Z Position ====#
            self['SpritePositionYAxis'] = data[0x8:0xa]           #==== Sprite Y Position ====#
            self['SpriteWidth'] = data[0xa:0xb]                   #==== Sprite Width ====#
            self['SpriteHeight'] = data[0xb:0xc]                  #==== Sprite Height ====#
            self['ParentSpriteFlags'] = data[0xc:0x10]            #==== Parent Sprite Flags ====#
            self['ChildSpriteFlags'] = data[0x10:0x14]            #==== Child Sprite Flags ====#
            self['ExtendedSpriteData'] = data[0x14:0x18]          #==== Extended Sprite Data ====#
            self['ParentSpriteType'] = data[0x18:0x19]            #==== Parent Sprite Type ====#
            self['ChildSpriteType'] = data[0x19:0x1a]             #==== Child Sprite Type ====#
            self['SpriteLinkID'] = data[0x1a:0x1c]                #==== Sprite Link ID ====#
            self['SpriteEffectIndex'] = data[0x1c:0x1e]           #==== Sprite Effect Index ====#
            self['ChildSpriteTransformationID'] = data[0x1f:0x20] #==== Child Sprite Transformation ID ====#
    def Load(self, data):
        self.bs = io.BytesIO(data)
        self.bs.seek(0x11b) #==== Start Y Axis ====#
        self["StartYAxis"]    = self.bs.read(1)
        self.bs.seek(0x15b) #==== Goal Y Axis ====#
        self["GoalYAxis"]     = self.bs.read(1)
        self.bs.seek(0x159) #==== Goal X Axis ====#
        self["GoalXAxis"]     = self.bs.read(2)
        self.bs.seek(0x70)  #==== Time Limit ====#
        self["TimeLimit"]      = self.bs.read(2)
        self.bs.seek(0x10)  #==== Creation Year, Month, Day, Hour and Minute ====#
        self["CreationYear"]   = self.bs.read(2)
        self["CreationMonth"]  = self.bs.read(1)
        self["CreationDay"]    = self.bs.read(1)
        self["CreationHour"]   = self.bs.read(1)
        self["CreationMinute"] = self.bs.read(1)
        self.bs.seek(0x6a)  #==== Game Style ====#
        self["GameStyle"]      = self.bs.read(3)
        self.bs.seek(0x29)  #==== Course Name ====#
        self["CourseName"]     = self.bs.read(64)
        self.bs.seek(0x6d)  #==== Course Theme ====#
        self["CourseTheme"]    = self.bs.read(1)
        self.bs.seek(0x72)  #==== Autoscroll ====#
        self["Autoscroll"]      = self.bs.read(1)
        self.bs.seek(0xec)  #==== Sprite Count ====#
        self["SpriteCount"]    = self.bs.read(4)
        for i in range(2600):         #==== Read Sprites ====#
            self.bs.seek(0xF0+32*i)
            self['Sprite '+str(i)] = self.Sprite()
            self['Sprite '+str(i)].Load(self.bs.read(32))

#==== Super Mario Maker 2 Course ====#
class SuperMarioMaker2Course(dict):
    def __init__(self):
        pass
    def load(self, q):
        return
