# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 20:57:14 2021

@author: antondG
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:04:59 2021

@author: antondG
"""
import os
from datetime import datetime
import logging
from AfvalwijzerCustom import AfvalwijzerCustom
class ApiDataLayer():
    def __init__(self, zipcode, housenumber):
        print("afvaldata loaded\n")
        self.data = []
        self.zipcode = zipcode
        self.housenumber = housenumber
        self.filepath = os.path.join(os.path.dirname(os.path.realpath (__file__)),'data.txt')
        if os.path.exists(self.filepath):
            print("file exists")
            mtime = os.path.getmtime(self.filepath)
            mtimedate = datetime.utcfromtimestamp(mtime).date() 
            datetoday = datetime.today().date()
            if mtimedate == datetoday:
                with open(self.filepath) as file :
                    for line in file:
                        self.data.append(line)
            else:
                print(f"date ctime = {mtimedate}")
                print(f"date datetoday = {datetoday}")
                #file exists but is out of data
                self.getAPIData()
                self.writeData()
                
        else:
            logging.warning('API - Afvalwijzerdata has already been loaded to the data.txt file')
            #wijzer = AfvalwijzerCustom(self.zipcode, self.housenumber)
            self.getAPIData()
            self.writeData()
            
        if not self.data:
            logging.warning("API - Afvalwijzer data could not be loaded")
    
    def getAPIData(self):
        wijzer = AfvalwijzerCustom(self.zipcode, self.housenumber)
        self.data = wijzer.getData()
        
    def writeData(self):
        print("data = ")
        print(self.data)
        with open(self.filepath, 'w') as f:
            for line in self.data:
                try:
                    f.write(line)
                    f.write("\n")
                except UnicodeEncodeError:
                    logging.warning(f"API - AfvalwijzerData could not decode a character in {line}")
                    
    def getData(self):
        if not self.data:
            Exception("API - api layer does not return data")
        print(f"api data = {self.data}")
        return self.data