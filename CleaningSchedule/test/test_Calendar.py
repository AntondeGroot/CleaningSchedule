# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 21:01:39 2021

@author: antondG
"""

import sys
sys.path.append(r"C:\Users\anton.degroot@cegeka-dsa.nl\.spyder-py3\CleaningSchedule\main")
import unittest
from Calendar import Calendar


class TestCalendar(unittest.TestCase):
    
    def test_distinctweeks(self):
        calendar = Calendar()
        calendar.setYear(2021)
        self.assertEqual(calendar.getWeekDescription(30), calendar.getWeekDescription(30))
        self.assertNotEqual(calendar.getWeekDescription(20), calendar.getWeekDescription(21))
        
    def test_nextyear(self):
        calendar = Calendar()
        calendar.setYear(2021)
        calendar2 = Calendar()
        calendar2.setYear(2022)
        self.assertNotEqual(calendar.getWeekDescription(1), calendar.getWeekDescription(53))
        self.assertEqual(calendar.getWeekDescription(53), calendar2.getWeekDescription(1),"The calendar does not go to the next year correctly week53 != week 1 of the new year")
        
    def test_translatedweeks(self):
        pass
        
if __name__ == '__main__':
    unittest.main()