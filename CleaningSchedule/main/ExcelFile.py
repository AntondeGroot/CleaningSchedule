# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 08:56:16 2021

@author: antondG
"""
import xlwt
from Calendar import Calendar
from Tasks import Tasks
from xlwt import Workbook
import logging

class ExcelFile():
    def __init__(self,dataList):
        self.row = 0
        self.row_temp = 0 #backup
        self.openFile()
        self.styleBold = xlwt.easyxf('font: bold 1;')
        self.styleRow = xlwt.easyxf("pattern: fore_colour gray25, pattern solid;")
        self.dataList = dataList
    
    def openFile(self):
        self.wb = Workbook()
        self.sheet = self.wb.add_sheet('Sheet 1')
        self.sheet.col(0).width = 11*367
        self.sheet.col(2).width = 30*367
        self.sheet.col(3).width = 30*367
        # set orientation to horizontal
        self.sheet.set_portrait(False)
        
    def closeFile(self):
        pass
        #def __when class closes / interrupts
        
    def saveFile(self):
        self.wb.save('CleaningSchedule.xls')        
    
    def addGarbageTasks(self,weekNr):
       
        nrtasks, datelist, garbagetype = self.findTaskByWeekNr(weekNr)
        print(f"Addgarbagetask week = {weekNr} , {datelist}")
        if nrtasks:
            for i in range(nrtasks):
                self.sheet.write(self.row_temp, 2, datelist[i],self.styleBold)
                self.nextRowTemporary()
                self.sheet.write(self.row_temp, 2, garbagetype[i])
                self.nextRowTemporary()  
            self.resetRow()
        else:
            logging.warning("No garbage tasks were found")
    
    def nextRowTemporary(self):
        self.row_temp += 1
    def nextRowDefinite(self):
        self.row_temp += 1
        self.row = self.row_temp
    def confirmRow(self):
        self.row = self.row_temp
        
    def resetRow(self):
        self.row_temp = self.row
        
    def drawRowSeparator(self):
        for col in range(4):
            self.sheet.write(self.row, col, '',self.styleRow)
        self.nextRowDefinite()
    
    def addDescription(self,desc):
        self.sheet.write(self.row, 0, desc)
        
    
    def SchedulePerson(self, person):
        self.sheet.write(self.row, 1, person)
        
    def addCleaningTasks(self, tasks):
        #tasks = Tasks()
        #tasksdict = tasks.getCleaningTasks()
        
        for task in tasks:
            self.sheet.write(self.row_temp, 3, task)
            self.nextRowTemporary()
        
        
    def findTaskByWeekNr(self, weekNr):
        nrtasks = 0
        datelist = []
        garbagetypelist = []
        calendar = Calendar()
        daylist = calendar.getTranslatedWeekdays(weekNr)
        print(f"\ndaylist = {daylist}\n")
        anyfound = False
        for day in daylist:
            found = False
            index = 0
            print(f"day is {day[3:]}")
            print(f"datalist = {self.dataList}")
            for line in self.dataList:
                if day[3:] in line: ## watch it "ma 13 okt" is not valid but "13 okt" is.
                    print(f"found match for day {day}")
                    found = True
                    anyfound = True
                    nrtasks += 1
                    break
                index += 1
            if found:
                if (index+1) < len(self.dataList):
                    garbagetype = self.dataList[index+1]
                    datelist.append(day)
                    garbagetypelist.append(garbagetype)  
        if not anyfound:
            logging.warning(f"No matching garbage pickupdates could be found for the entire week {weekNr}")
        
        
        return nrtasks, datelist, garbagetypelist

    def convertToPDF(self):
        #  https://stackoverflow.com/questions/16683376/print-chosen-worksheets-in-excel-files-to-pdf-in-python

        import win32com.client

        o = win32com.client.Dispatch("Excel.Application")
        o.Visible = False
        wb_path = r'C:\Users\anton.degroot@cegeka-dsa.nl\.spyder-py3\CleaningSchedule\main\CleaningSchedule.xls'
        wb = o.Workbooks.Open(wb_path)
        ws_index_list = [1] #say you want to print these sheets
        path_to_pdf = r'C:\Users\anton.degroot@cegeka-dsa.nl\.spyder-py3\CleaningSchedule\main\Schedule.pdf'
        wb.WorkSheets(ws_index_list).Select()
        wb.ActiveSheet.ExportAsFixedFormat(0, path_to_pdf)
        wb.Close(True)