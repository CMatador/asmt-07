from datetime import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
class Holiday:
    '''Holiday Class, enter date in YYYY-MM-DD format'''

    def __init__(self, name, date):
        #Your Code Here
        self.name = name
        self.date = datetime.strptime(date, '%Y-%m-%d').date()       
    
    def __str__ (self):
        # String output
        # Holiday output when printed.
        return f'{self.name} ({self.date})'

    def __eq__(self, other):
        return self.name == other.name

# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    '''Holiday List class'''

    def __init__(self):
        self.innerHolidays = []
   
    def addHoliday(self, holidayObj):
        # Make sure holidayObj is an Holiday Object by checking the type
        if isinstance(holidayObj, Holiday):
        # Use innerHolidays.append(holidayObj) to add holiday
            self.innerHolidays.append(holidayObj)
        # print to the user that you added a holiday
            print('Holiday added successfully.')

    def findHoliday(self, HolidayName, Date):
        pass
        # Find Holiday in innerHolidays
        # Return Holiday

    def removeHoliday(self, HolidayName, Date):
        pass
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday

    def read_json(self, filelocation):
        # Read in things from json file location
        with open(filelocation) as f:
            data = json.load(f)
        # Use addHoliday function to add holidays to inner list.
            for e in data['holidays']:
                x = Holiday(e['name'], e['date'])
                self.addHoliday(x)

    def save_to_json(self, filelocation):
        # Write out json file to selected file.
        with open (filelocation, 'w') as f:
            json.dump(self.innerHolidays, f, indent=4)
        
    def scrapeHolidays(self):
        for year in range(2020, 2025):
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/
        # Remember, 2 previous years, current year, and 2  years into the future. 
        # You can scrape multiple years by adding year to the timeanddate URL. 
        # For example https://www.timeanddate.com/holidays/us/2022
            response = requests.get(f'https://www.timeanddate.com/holidays/us/{year}')
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', attrs = {'id':'holidays-table'})
            tbody = table.find('tbody')

            for row in tbody.find_all('tr'):
                columns = row.find_all('td')
                bolds = row.find_all('th')
                holiday = {}
                if(columns != []):
                    holiday['name'] = columns[1].get_text()
                if(bolds != []):
                    holiday['date'] = bolds[0].get_text() + ' ' + str(year)
                    holiday['date'] = date_converter(holiday['date'])
                    holiday = Holiday(holiday['name'], holiday['date'])
        # Check to see if name and date of holiday is in innerHolidays array
                if holiday not in self.innerHolidays and holiday != {}:                    
        # Add non-duplicates to innerHolidays
                    self.addHoliday(holiday)
        # Handle any exceptions.     

    def numHolidays(self):
        print(len(self.innerHolidays))
        # Return the total number of holidays in innerHolidays
    
    def filter_holidays_by_week(self, year, week_number):
        pass
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays

    def displayHolidaysInWeek(self, holidayList):
        pass
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

    def getWeather(self, weekNum):
        pass
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    def viewCurrentWeek(self):
        pass
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results

    def display_menu(self):
        '''Displays the main menu'''
        print('')
        print('Holiday Menu')
        print('================')
        print('1. Add a Holiday')
        print('2. Remove a Holiday')
        print('3. Save Holiday List')
        print('4. View Holidays')
        print('5. Exit')
        print('')

    def navigator(self):
        while True:
            choice = input('Please make a selection: ')
            if choice == str(1):
                x = {}
                x['name'] = input('Input Holiday name: ')
                x['date'] = input('Input Holiday date in yyyy-mm-dd format: ')
                x = Holiday(x['name'], x['date'])
                if x not in self.innerHolidays:
                    self.addHoliday(x)
                    for i in range(len(self.innerHolidays)):
                        print(self.innerHolidays[i])
                    return
                else:
                    print('That holiday is already in the list.')
                    return
            else:
                print('Not a valid selection.')
                return

def date_converter(input):
    '''Converts from Mon dd yyyy format to yyyy-mm-dd'''
    return datetime.strptime(input, '%b %d %Y').strftime('%Y-%m-%d')

def main():
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    holidays = HolidayList()
    # 2. Load JSON file via HolidayList read_json function
    holidays.read_json('holidays.json')
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    holidays.scrapeHolidays()
    # 4. Create while loop for user to keep adding or working with the Calendar
    finished = False
    # print(holidays.innerHolidays[1])
    while not finished:
    # 5. Display User Menu (Print the menu)
        holidays.display_menu()
    # 6. Take user input for their action based on Menu and check the user input for errors
    # choice = input('Please make a selection: ')
        holidays.navigator()
    # 7. Run appropriate method from the HolidayList object depending on what the user input is
    # 8. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


if __name__ == "__main__":
    main();


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.





