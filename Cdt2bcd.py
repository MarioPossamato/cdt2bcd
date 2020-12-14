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
from SMM2 import encryption
from SMM2 import keytables
from SMM2 import streams
#====================================#
# Super Mario Maker Course
class SuperMarioMaker1Course(dict):
    def __init__(self, data=None):
        if not data:
            return None
        else:
            self.load(data)

    def load(self, data=None):
        if not data:
            return None
        else:
            self.data = data
            stream = streams.StreamIn(self.data)
            stream.seek(0x11b) #==== Start Y Axis ====#
            self["StartYAxis"]     = stream.read(1)
            stream.seek(0x15b) #==== Goal Y Axis ====#
            self["GoalYAxis"]      = stream.read(1)
            stream.seek(0x159) #==== Goal X Axis ====#
            self["GoalXAxis"]      = stream.read(2)
            stream.seek(0x70)  #==== Time Limit ====#
            self["TimeLimit"]      = stream.read(2)
            stream.seek(0x10)  #==== Saved Year, Month, Day, Hour and Minute ====#
            self["SavedYear"]      = stream.read(2)
            self["SavedMonth"]     = stream.read(1)
            self["SavedDay"]       = stream.read(1)
            self["SavedHour"]      = stream.read(1)
            self["SavedMinute"]    = stream.read(1)
            stream.seek(0x6a)  #==== Game Style ====#
            self["GameStyle"]      = stream.read(3)
            stream.seek(0x29)  #==== Course Name ====#
            self["CourseName"]     = stream.read(64)
            stream.seek(0x6d)  #==== Course Theme ====#
            self["CourseTheme"]    = stream.read(1)
            stream.seek(0x72)  #==== Autoscroll ====#
            self["Autoscroll"]     = stream.read(1)
            stream.seek(0xec)  #==== Sprite Count ====#
            self["SpriteCount"]    = stream.read(4)
            for i in range(2600):         #==== Read Sprites ====#
                stream.seek(0xF0+32*i)
                self['Sprite '+str(i)] = self.Sprite()
                self['Sprite '+str(i)].Load(stream.read(32))

        class Sprite(dict):
            def __init__(self, data=None):
                if not data:
                    return None
                else:
                    self.load(data)
            def load(self, data=None):
                if not data:
                    return None
                else:
                    self.data = data
                    self.stream = streams.StreamIn(self.data)
                    self['SpritePositionXAxis'] = self.stream.readUInt32()        #==== Sprite X Position ====#
                    self['SpritePositionZAxis'] = self.stream.readUInt32()        #==== Sprite Z Position ====#
                    self['SpritePositionYAxis'] = self.stream.readUInt16()        #==== Sprite Y Position ====#
                    self['SpriteWidth'] = self.stream.readUInt8()                 #==== Sprite Width ====#
                    self['SpriteHeight'] = self.stream.readUInt8()                #==== Sprite Height ====#
                    self['ParentSpriteFlags'] = self.stream.readBytes(0x4)        #==== Parent Sprite Flags ====#
                    self['ChildSpriteFlags'] = self.stream.readBytes(0x4)         #==== Child Sprite Flags ====#
                    self['ExtendedSpriteData'] = self.stream.readBytes(0x4)       #==== Extended Sprite Data ====#
                    self['ParentSpriteType'] = self.stream.readUInt8()            #==== Parent Sprite Type ====#
                    self['ChildSpriteType'] = self.stream.readUInt8()             #==== Child Sprite Type ====#
                    self['SpriteLinkID'] = self.stream.readUInt16()               #==== Sprite Link ID ====#
                    self['SpriteEffectIndex'] = self.stream.readUInt16()          #==== Sprite Effect Index ====#
                    self.stream.skip(0x1)                                         #==== Unknown ====#
                    self['ChildSpriteTransformationID'] = self.stream.readUInt8() #==== Child Sprite Transformation ID ====#

#==== Super Mario Maker 2 Course ====#
class SuperMarioMaker2Course(dict):
    def __init__(self, data=None):
        if not data:
            return None
        else:
            self.load(data)
    def load(self, data=None):
        if not data:
            return None
        else:
            self.data = data
            self.stream = streams.StreamIn(self.data)
