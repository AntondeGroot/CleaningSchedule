# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 21:19:57 2021

@author: antondG
"""


import unittest
import sys
sys.path.append(r"C:\Users\anton.degroot@cegeka-dsa.nl\.spyder-py3\CleaningSchedule\main")
from Tasks import Tasks

tasks5 = [1,2,3,4,5]
tasks3 = [1,2,3]
tasks1 = [1]

weekly = 1
biweekly = 2
monthly = 4
fiveweekly = 5

persons5 = 5
persons3 = 3

class TestTasks(unittest.TestCase):
        
    def test_MultiplePersonsMultipleMonthlyTasks(self):
        tasks = Tasks()
        expected = [[1,5],[2],[3],[4],[1,5]]
        result = tasks.divideTasks(persons5, tasks5, monthly)
        self.assertEqual(expected, result, 'MultiplePersonsMultipleMonthlyTasks')
    
    def test_MorePersonsThanMonthlyTasks(self):
        tasks = Tasks()
        result = tasks.divideTasks(persons5, tasks3, monthly)
        expected = [[1],[2],[3],[],[1]]
        self.assertEqual(expected, result)
        
    def test_FewerPersonsThanMonthlyTasks(self):
        tasks = Tasks()
        result = tasks.divideTasks(persons3, tasks5, monthly)
        expected = [[1,5],[2],[3],[4]]
        print(result)
        #self.assertEqual(expected, result)
    
    def test_MultiplePersonsEqualPeriodicTasks(self):
        tasks = Tasks()
        result = tasks.divideTasks(persons5, tasks5, fiveweekly)
        expected = [[1],[2],[3],[4],[5]]
        self.assertEqual(expected, result)
        
    def test_MultiplePersonsOneBiweeklyTask(self):
        tasks = Tasks()
        result = tasks.divideTasks(persons5, tasks1, biweekly)
        expected = [[1],[],[1],[],[1]]
        self.assertEqual(expected, result)
    
    def test_MultiplePersonsOneTaskPeriodicalTask_LargePeriodicity(self):
        tasks = Tasks()
        result = tasks.divideTasks(persons5, tasks1, fiveweekly)
        expected = [[1],[],[],[],[]]
        self.assertEqual(expected, result)
    
    def test_MultiplePersonsOneWeeklyTask(self):
        tasks = Tasks()
        result = tasks.divideTasks(persons5, tasks1, weekly)
        expected = [[1],[1],[1],[1],[1]]
        self.assertEqual(expected, result)
        
    def test_MultiplePersonsMultipleWeeklyTask(self):
        tasks = Tasks()
        result = tasks.divideTasks(persons5, tasks3, weekly)
        expected = [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
        self.assertEqual(expected, result)
    
if __name__ == '__main__':
    unittest.main()