# -*- coding: utf-8 -*-
class Settings():

    def __init__(self):
        self.settings=[]
        pass

    def setSettings(self,path):
        file=open(path,'r')

        for line in file:
            oneTask=line.split('~')
            oneTask[1]=oneTask[1].split(' ')
            oneTask[2]=oneTask[2].split(' ')
            oneTask[4]=oneTask[4].split(' ')

            self.settings.append(oneTask)
        print self.settings
        file.close()
        pass

    def getSettings(self):
        return self.settings


Settings