# -*- coding: utf-8 -*-
import sys
from task import Task
from Settings import Settings


if __name__ == '__main__':

    s=Settings()
    s.setSettings("setings.csv")
    settings=s.getSettings()
    for i in settings:
        task=Task(i)
        task.getHtml()
