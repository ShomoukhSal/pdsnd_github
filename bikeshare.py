import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("\n Hello! Let\'s explore some US bikeshare data!\n")
    print()

    # To get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    chosen_city= input("Please,write the city you want to see its Data: Chicago, New York, washington: ").lower()
    print()
    while chosen_city not in CITY_DATA.keys():
        print("Sorry, that's not in the opions")
        chosen_city= input("Please,write the city you want to analyze the data from: Chicago, New York, washington").lower()
        print()
    # To get user input for month (all, january, february, ... , june)
    MONTHS=['january', 'fabreuary', 'march','april', 'may', 'june']
    while True:
        chosen_month = input("Please, write the month in which you want the analysis from, or write 'All' to display all months. \nNote: Our Database has only the first six months i.e. January, Fabreuary, March, April, May or June.\n").lower()
        print()
        if chosen_month != 'all' and chosen_month not in MONTHS:
            print("Sorry, that's not in the opions")
            print("Please, choose one of the following options:(january, fabreuary, march, april, may, june) or enter 'All' to display all months")
            print()
        else:
            break

    # To get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS= ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    while True:
        chosen_day = input("Please, write a day of the week in which you want the data from, or write 'All' to display all days: ").lower()
        print()
        if chosen_day != 'all' and chosen_day not in DAYS:
            print("Sorry, that's not in the opions")
            print("Please, choose one of the following options:(Sunday, Monday, Tuesday, Wednesday, Thurday, friday), or enter 'All' to display all days.")
            print()
        else:
            break

    print('-'*40)
    return chosen_city, chosen_month, chosen_day

def load_data(chosen_city, chosen_month, chosen_day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) chosen_city - name of the city to analyze
        (str) chosen_month - name of the month to filter by, or "all" to apply no month filter
        (str) chosen_day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[chosen_city])
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract the months from the Start Time column to create a MONTH column
    df['Month'] = df['Start Time'].dt.month
    # Extract days from the Start Time column to create a Day_of_week column
    df['Day_of_week'] = df['Start Time'].dt.day_name()
    # Extract hours from the Start Time column to create an Hour column
    df['Hour'] = df['Start Time'].dt.hour

    #Filter by month (if the user selected a certain month)
    if chosen_month !='all':
        MONTHS = ['january', 'fabreuary', 'march','april', 'may', 'june']
        chosen_month = MONTHS.index(chosen_month) +1
        #Create new dataframe
        df = df[df['Month']== chosen_month]

    # Filter by day of week (if the user selected a certain day)
    if chosen_day != 'all':
        #Create new DataFrame
        df = df[df['Day_of_week'] == chosen_day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # To display the most common month
    Popular_Month = df['Month'].mode()[0]
    print("\n* The most popular month to start using bikeshare:", Popular_Month)

    # To display the most common day of week
    Popular_Day = df['Day_of_week'].mode()[0]
    print("\n* The most popular day of the week to start using bikeshare:", Popular_Day)

    # To display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print("\n* The most popular hour to start using bikeshare:", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # To display most commonly used start station
    Popular_Start_Station = df['Start Station'].mode()[0]
    print("\n* The most popular start station:\n", Popular_Start_Station)

    # To do display most commonly used end station
    Popular_End_Station = df['End Station'].mode()[0]
    print("\n* The most popular end station:\n", Popular_End_Station)

    # To display most frequent combination of start station and end station trip
    Group_By = df.groupby(['Start Station','End Station'])
    Popular_Combination = Group_By.size().sort_values(ascending=False).head(1)
    print("\n* Most popular combination of Start Station and End Station trip:\n'", Popular_Combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # To display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print("\n* Total Travel Time:", Total_Travel_Time)

    # To display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print("\n* Avarage Travel Time:", Mean_Travel_Time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # To display counts of user types
    User_Type = df['User Type'].value_counts()
    print("\n* User Type Stats:\n", User_Type)

    # To display counts of gender
    #'washington.csv' doesn't contain a Gender column
    # therefore, this try clause is done to make sure that only df with 'Gender' column are displayed
    try:
        Gender_Stats = df['Gender'].value_counts()
        print("\n* Gender Stats:\n", Gender_Stats)
    except:
        print("\n*This file does not contain a 'Gender' column.")

    # Display earliest, most recent, and most common year of birth
    #Similarly, 'washington.csv' doesn't contain a 'Birth Year' column
    try:
        Earliest_Year = int(df['Birth Year'].min())
        print("\n* Earliest Year:",Earliest_Year)

        Most_Recent_Year = int(df['Birth Year'].max())
        print("\n* Most Recent Year:",Most_Recent_Year)

        Most_Common_Year = int(df['Birth Year'].mode()[0])
        print("\n* Most Common Year:",Most_Common_Year)
    except:
        print("\n*This file does not contain a 'Birth Year' column.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_row_data(df):
    '''
        Displays raw data on user request to compute the stats
    '''
    print(pd.set_option("display.max_columns",200))
    next_rows = 0
    while True:
        raw_data = input('\n Would you like to see next five row of raw data? Enter yes or no.\n')
        if raw_data.lower() != 'yes':
            return
        next_rows = next_rows+5
        print(df.iloc[next_rows:next_rows+5])

    print('-'*80)

def main():
    while True:
        chosen_city, chosen_month, chosen_day = get_filters()
        df = load_data(chosen_city, chosen_month, chosen_day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            raw_data = input('\n Would you like to see first five row of raw data? Enter yes or no.\n')
            if raw_data.lower() != 'yes':
                break
            display_row_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
