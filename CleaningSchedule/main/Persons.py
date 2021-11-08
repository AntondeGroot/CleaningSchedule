# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:04:59 2021

@author: antondG
"""
import logging
import math
class Persons():
    def __init__(self):
        
        try:
            with open("./persons.txt") as file : 
                lines = []
                for line in file:
                    if("#" not in line):
                        line = line.replace("\n", "")
                        line.strip()
                        lines.append(line)
            self.persons = lines        
            if not self.persons:
                logging.warning("Persons.txt did not contain persons")
        except Exception:
            logging.warning("Persons.txt could not be opened")
        
    def AssignPersonByWeek(self,weekNr):
        return self.persons[weekNr % len(self.persons)]
    
    def getPersonByWeek(self,weekNr):
        return self.assignedPersons[weekNr]
     
    def GetPersons(self):
        return self.persons
    def getNumberOfPersons(self):
        return len(self.persons)
    
    def assignPersons(self,roulate=False):
        weeks = range(1,54)
        nrpersons = len(self.persons)
        self.assignedPersons = []
        for i,week in enumerate(weeks):
            period = 0
            if roulate:    
                period = math.ceil(week/nrpersons)%nrpersons
            self.assignedPersons.append(self.persons[(week+period)%nrpersons])
            if i%(nrpersons)==nrpersons-1:
                print()