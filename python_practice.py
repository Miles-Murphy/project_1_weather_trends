import pandas as pd
import numpy as np
import calendar
import datetime
import time

"""
Imports important libraries and sets up a dictionary to connect user input and the csv files

"""

city_temp_data = { 'edinburgh': 'edinburgh_temps.csv',
                    'dublin': 'dublin_temps.csv',
                    'raleigh': 'raleigh_temps.csv',
                    'rio de janeiro': 'rio_temps.csv',
                    'tokyo':, 'tokyo_temps.csv'}

global_temp_data = { 'global': 'global_temps.csv'}

def start_up():

"""

Greet the user and confirm program activation

"""
    print('\nHi! You have requested to examine temperature trends.')
    print('\nI can examine some aspects of the data from 5 cities and world as a whole!')
    print('\nWould you like to examien this data?')

    yes_or_no = ('yes', 'no')
    while True:
        start = input('\nPlease enter "yes" or "no": ').lower()
        if start not in yes_or_no:
            print('\nSorry, that is not an acceptable response. Please try again!)
        else:
            break
    return start

def select_data(start):
    """
    Asks the user what city(ies) and/or global temperature data they would like to view.

    Input:
        (str) start - confirms interest in running program

    Returns:
        (str) city(ies) - city(ies) the user would like to view
        (str) global - user's interst in viewing global data
    """

def main():
    while True:
        start = start_up()
        if start != 'yes':
            break
            #Ends program incase the user decided not to use it or started it in error!
        city, month, day = select_data(start)
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city, month, day)

        display_results_5(df)

        yes_or_no = ('yes', 'no')
        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n')

            if restart not in yes_or_no:
                print('\nSorry, that is not an acceptable response. Please try again')
            else:
                break
        if restart.lower() != 'yes':
            print('\nThanks for looking at bikeshare data with me today!')
            break
            #Ends the program without an error and says thanks to the user!

"""Websites such as Stackoverflow, Udacity Forums, Python Libraries, and other reference/discussion forums were used to trouble shoot problems, but no solutions were copied verbatim. All of this code was provided by Udacity at the start of the project or written by me with a lot of trial and error (generally after hours of reading about similar solutions or new techniques and adapting them to my line of thinking). Nothing was intentionally copied."""


if __name__ == "__main__":
	main()
