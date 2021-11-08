# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:53:52 2021

@author: antondG
"""
import math
import os
import logging
class Tasks():
    def __init__(self,filename = ''):
        self.tasklist = []
        if not filename:
            filename = 'tasks.txt'
        self.filepath = os.path.join(os.path.dirname(os.path.realpath (__file__)),filename)
        self.readFile()
        self.periodicities = {}
        
    def readFile(self):
        try:
            with open(self.filepath) as file : 
                for line in file:
                    if("#" not in line) and (',' in line):
                        period, task = self.splitFirstComma(line)                    
                        task = task.replace("\n", "")
                        task.strip()
                        if period:
                            self.tasklist.append([period,task])
            if not self.tasklist:
                logging.warning(f"{self.filepath} did not contain tasks")
        except ValueError:
            logging.warning(f"{self.filepath} could not be opened")
        
    def getTasks(self) -> list:
        return self.tasklist
    
    def splitFirstComma(self,line) -> list:
        result = [0,'']
        if line and type(line) == str:
            for i, char in enumerate(line):
                first = line[:i]
                last = line[i+1:]
                last = last.strip()
                if char == ',' and first.isdigit():
                    result = [int(first), last]
                    break
        return result
    
    def getCleaningTasks(self):
        if os.path.exists(self.filepath):
            print("file tasks.txt exists")
            tasksdict = {}
            with open(self.filepath) as file :
                for line in file:
                    line = line.strip()
                    if line and ("#" not in line) and ("," in line):
                        nr, task = line[:1],line[1+1:]
                        if nr not in tasksdict:
                            tasksdict[nr] = []
                        tasksdict[nr].append(task)
                        print(tasksdict)
            return tasksdict
        else:
            logging.warning("Error: file tasks.txt does not exist")
    
    def assignAllTasks(self):
        self.AllTasks = [None]*54
        for i,x in enumerate(self.AllTasks):
            self.AllTasks[i] = []
        from Tasks import Tasks
        periodictasks = Tasks().getCleaningTasks()
        periodicities = periodictasks.keys()
        self.periodicities = periodicities
        for weekId in range(1,54):
            print(f"week = {weekId}")
            for periodicity in periodicities:
                for i,tasks in enumerate(periodictasks[periodicity]):
                    #don't assign all periodic tasks (with period != 1) to the same week
                    offset = i
                    if (weekId+offset)%int(periodicity) == 0:
                        self.AllTasks[weekId].append(tasks)
    
    def checkRoulation(self,nrpersons):
        from Tasks import Tasks
        periodictasks = Tasks().getCleaningTasks()
        periodicities = periodictasks.keys()
        return (str(nrpersons) in periodicities)
        
    def getTasksByWeekNr(self, weekNr):
        return self.AllTasks[weekNr]
    
    