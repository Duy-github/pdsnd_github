import time
import pandas as pd
import numpy as np


#Simple math
xx = 1
yy = 2
zz = xx + yy
qq = xx + yy +zz

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Get all the cities from CITY_DATA
CITY = []
for city_key in CITY_DATA:
    CITY.append(city_key)

#Month dict
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    #Get all the cities from CITY_DATA
    CITYS = []
    for city_key in CITY_DATA:
        CITYS.append(city_key)

    while True:
        input_city = input("Please enter the city that you want to see (Ex: Chicago, New York City, Washington)")
        input_city = input_city.lower()
        if input_city in CITYS:
            city = input_city
            print('Input city= ', city)
            break
        else:
            print('Input is invalid, please enter again')

    # TO DO: get user input for month (all, january, february, ... , june)
    
    

    while True:
        input_month = input("Please enter the month that you want to see (Ex: all, january, february, ... , june)")
        input_month = input_month.lower()
        if input_month in MONTHS:
            month = input_month
            print('Input month= ', month)
            break
        else:
            print('Input is invalid, please enter again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday' , 'saturday', 'sunday']

    while True:
        input_day = input("Please enter the day of the week that you want to see (Ex: all, monday, tuesday, ... , sunday)")
        input_day = input_day.lower()
        if input_day in DAYS:
            day = input_day
            print('Input day= ', day)
            break
        else:
            print('Input is invalid, please enter again')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Load csv from selected city
    df = pd.read_csv(CITY_DATA[city])
    
    
    #Filter data by selected month
    df['Start Time'] = pd.to_datetime(df['Start Time']) #convert Start time to datetime type
    df['TripMonth'] = df['Start Time'].dt.month #create another column for better filter with selected month

    month = MONTHS.index(month)

    #0 = all, no need to filter
    if month != 0:
        df = df[df['TripMonth'] == month]



    #Filter data by selected day of the week
    df['TripWeekday'] = df['Start Time'].dt.day_name()
    df['TripWeekday']
    
    #if day = all, no need to filter
    if day != 'All':
        df = df[df['TripWeekday'] == day.capitalize()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    com_mon = df['TripMonth'].value_counts()
    com_mon = com_mon.idxmax()
    com_mon = MONTHS[com_mon]
    print("The most common month: ", com_mon.capitalize())

    # TO DO: display the most common day of week
    com_wd = df['TripWeekday'].value_counts()
    com_wd = com_wd.idxmax()
    print("The most common day of week: ", com_wd)


    # TO DO: display the most common start hour
    df['TripStartHour'] = df['Start Time'].dt.hour
    com_sh = df['TripStartHour'].value_counts()
    com_sh = com_sh.idxmax()
    print("The most common start hour: ", com_sh)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_ss = df['Start Station'].value_counts()
    com_ss = com_ss.idxmax()
    print("\nThe most commonnly used start station: ", com_ss)

    # TO DO: display most commonly used end station
    com_es = df['End Station'].value_counts()
    com_es = com_es.idxmax()
    print("\nThe most commonnly used end station: ", com_es)

    # TO DO: display most frequent combination of start station and end station trip
    com_trip = df['Start Station'] + " -> " +  df['End Station']
    com_trip = com_trip.value_counts()
    com_trip = com_trip.idxmax()
    print("\nThe most frequent combination of start station and end station trip: ", com_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tt = df['Trip Duration'].sum() / (60*60)
    total_tt = round(total_tt, 2)
    print("\nThe total travel time: ",total_tt,"hrs")


    # TO DO: display mean travel time
    mean_tt = df['Trip Duration'].mean() / (60*60)
    mean_tt = round(mean_tt, 2)
    print("\nThe mean travel time: ",mean_tt,"hrs")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    u_type = df['User Type'].value_counts()
    print("\nCounts of user types")
    print(u_type)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        u_gender = df['Gender'].value_counts()
        print("\nCounts of user gender")
        print(u_gender)
    else:
        print("\nThe city does not have info about gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Gender' in df.columns:
        earliest_yob = df['Birth Year'].min()
        print('\nThe earliest year of birth: ',int(earliest_yob))

        mostrecent_yob = df['Birth Year'].max()
        print('\nThe most recent year of birth: ',int(mostrecent_yob))

        mostcommon_yob = df['Birth Year'].value_counts()
        mostcommon_yob = mostcommon_yob.idxmax()
        print('\nThe most common year of birth: ',int(mostcommon_yob))

    else:
        print("\nThe city does not have info about birth")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    df = df.reset_index(drop=True)
    while True:
        load_permission = input('\nWould you like to load raw data\n')
        check =['no','yes']
        if load_permission.lower() in check:
            if  load_permission.lower() != 'no':
                #load first 5 row
                d_row = 0
                print(df.loc[d_row:d_row + 4])

                while (input('continue? ') != 'no'):
                    #if continue, load next 5 rows
                    d_row = d_row + 5
                    print(df.loc[d_row:d_row + 4,:])
                break

            else:
                break

        else:
            print('Input is invalid, please enter again')
            





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
