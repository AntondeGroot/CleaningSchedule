# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 08:54:08 2021

@author: antondG
"""
import datetime
from babel.dates import format_date # $ pip install babel
import isoweek

class Calendar():
    def __init__(self):
        my_date = datetime.date.today()
        self.year, weekNr, day_of_week = my_date.isocalendar()
        self.nextWeekNr = weekNr + 1   
        
    def getNextWeekNumbers(self):
        return range(self.nextWeekNr,self.nextWeekNr+4)
    
    def getWeekDescription(self,weekNr,language = 'nl') -> str:
        #check for new year
        self.nextWeekNr = weekNr
        daylist = self.getListOfWeekdays()
        d11 = format_date(daylist[0], "dd", locale = language) #01 oktober (monday)
        d12 = format_date(daylist[0], "MMM", locale = language) #01 oktober (monday)
        d21 = format_date(daylist[-1], "dd", locale = language) #08 oktober
        d22 = format_date(daylist[-1], "MMM", locale = language) #08 oktober
        return f"{d11} {d12} t/m {d21} {d22}"
    
    def getListOfWeekdays(self) -> list:
        week = isoweek.Week(self.year, self.nextWeekNr)
        return week.days()
    
    def getTranslatedWeekdays(self,weekNr=0,language='nl'):
        results = []
        if weekNr:
            print(f"translated weeknr = {weekNr}")
            self.nextWeekNr = weekNr
        
        days = self.getListOfWeekdays()
        for day in days:
            dayTranslated = format_date(day, "EEE", locale = language) #sunday 01 oktober
            dateTranslated = format_date(day, "dd MMM", locale = language).replace('.','') #sunday 01 oktober
            results.append(dayTranslated+" "+dateTranslated)    
        return results
    def setWeekNr(self,weekNr):
        self.nextWeekNr = weekNr
    
    def setYear(self,year):
        self.year = year
