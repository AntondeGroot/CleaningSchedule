

"https://moonbooks.org/Articles/How-to-convert-month-index-to-name-in-python/#:~:text=To%20convert%20month%20index%20%281%2C%202%2C%203%2C%204%2C,%3E%3E%3E%20month_name%20%3D%20calendar.month_name%20%5Bmonth_idx%5D%20%3E%3E%3E%20month_name%20%27September%27"
"https://github.com/bartdorlandt/afvalwijzer/blob/master/Afvalwijzer/Afvalwijzer.py"
from ApiDataLayer import ApiDataLayer
from Calendar import Calendar
from ExcelFile import ExcelFile
from Persons import Persons
from Tasks import Tasks
import math
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('')

def AssignTasksByWeek(weekNr,persons,tasks):
    rotateTasks = 0
    if len(tasks) == len(persons):
        rotateTasks = math.floor(weekNr/len(persons))
    task = tasks[(weekNr + rotateTasks) % len(tasks)]
    return task 

#%% Get data
zipcode = '6851AV'
number = '41'

#%% get weeknumber
if __name__ == '__main__':
    api  = ApiDataLayer(zipcode, number)
    data = api.getData()
    persons = Persons()
    calendar = Calendar()         
    weekNrs  = calendar.getNextWeekNumbers()
    schedule = ExcelFile(data)
    nrPersons = persons.getNumberOfPersons()
    tasks = Tasks()
    tasks.assignAllTasks()
    roulatePersonsBool = tasks.checkRoulation(nrPersons)
    persons.assignPersons(roulatePersonsBool)
    
    for weekNr in weekNrs:
        weekTasks = tasks.getTasksByWeekNr(weekNr)
        schedule.drawRowSeparator()
        schedule.addDescription(calendar.getWeekDescription(weekNr))
        person = persons.getPersonByWeek(weekNr)
        schedule.SchedulePerson(person)
        schedule.addGarbageTasks(weekNr)
        schedule.addCleaningTasks(weekTasks)
        schedule.nextRowDefinite()
    schedule.drawRowSeparator()
    schedule.saveFile()
    schedule.convertToPDF()