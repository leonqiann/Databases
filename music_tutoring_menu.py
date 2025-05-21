# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'music_tutoring.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

# This is the filename of the database to be used
DB_NAME = 'music_tutoring.db'
    # This is the SQL to connect to all the tables in the database
TABLES = (" music_lessons "
           "LEFT JOIN gender ON music_lessons.gender_id = gender.gender_id "
           "LEFT JOIN instrument ON music_lessons.instrument_id = instrument.instrument_id "
           "LEFT JOIN lesson_day ON music_lessons.lesson_day_id = lesson_day.lesson_day_id "
           "LEFT JOIN parent_info ON music_lessons.parent_info_id = parent_info.parent_info_id "
           "LEFT JOIN school ON music_lessons.school_id = school.school_id ")

def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()  




menu_choice = ''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the cars database\n\n'
                        'Type the letter for the information you want\n'
                        "A: Child's first name, school the child attends, parent's first name and contact number, the instrument the child is learning to play, what time the lesson is, on a Monday\n"
                        "B: Child's first name, school the child attends, parent's first name and contact number, the instrument the child is learning to play, what time the lesson is, on a Wednesday\n"
                        'C: First name, last name, and contact phone number of parent, how much has been paid, and how much is owed\n'
                        'D: All lessons on a certain day\n'
                        'Z: Exit\n\n'
                        'Type option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('monday')
    elif menu_choice == 'B':
        print_query('wednesday')
    elif menu_choice == 'C':
        print_query('term 1')
    elif menu_choice == 'D':
        lesson_day = input('Which day do you want to see? : ')
        lesson_day = lesson_day.title()
        print_parameter_query("child_first, school, parent_first, parent_phone, instrument, lesson_time", "lesson_day = ? ORDER BY lesson_time, lesson_day",lesson_day)
    