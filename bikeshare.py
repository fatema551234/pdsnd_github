import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ["january", "february", "march", "april", "may", "june", "all"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nPlease specify a city, 'chicago, new york city or washington'?\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("\nCan you choose the right city, please!")
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nChoose a month to filter it from January to June, Or type 'All' for all months?\n").lower()
        if month in months:
            break
        else:
            print("\nCan you choose and type from 'january', 'february', 'march', 'april', 'may', 'june' Or 'all', please!")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nType any day of week you want Or type 'All' for all?\n").lower()
        if day in days:
            break
        else:
            print("\nCan you type the right day, please!")

    print('='*70)
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
    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.day_name()

    if month != "all":
        month = months.index(month) +1
        df = df[df["month"] == month]

    if day != "all":
        df = df[df["day"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    print("\nThe most common month :", df["month"].mode()[0])
    # display the most common day of week
    print("\nThe most common day: ", df["day"].mode()[0])
    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    print("\nThe most common start hour :", df["hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    print("\nMost commonly used start station :", df["Start Station"].mode()[0])
    # display most commonly used end station
    print("\nMost commonly used end atation :", df["End Station"].mode()[0])
    # display most frequent combination of start station and end station trip
    most_f_combination = (df["Start Station"] + ' + ' + df["End Station"]).mode()[0]
    print("\nMost frequent combination of start and end station trip: ", most_f_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    print("\nTotal travel time: ", df["Trip Duration"].sum())
    # display mean travel time
    print("\nMean travel time: ", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    print("\n The count of user types: ", df["User Type"].value_counts())
    # Display counts of gender
    try:
        print("\nThe count of gender: ", df["Gender"].value_counts())
    except:
        print("\nThe gender doesn't include in data")
    # Display earliest, most recent, and most common year of birth
    try:
        print("\nEarliest year of birth: ", df["Birth Year"].min())
    except:
        print("\nThe earliest year of birth doesn't include in data")
    try:
        print("\nMost recent year of birth: ", df["Birth Year"].max())
    except:
        print("\nThe most recent year of birth doesn't include in data")
    try:
        print("\nMost common year of birth: ", df["Birth Year"].mode()[0])
    except:
        print("\nThe most common year of birth doesn't include in data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw(df):
    raw = 0
    while True:
        msg = input("\nDo you want to display 5 raws of data as well, 'Y' OR 'N'?\n").lower()
        if msg == 'n':
            break
        elif msg == 'y':
            print(df[raw:raw+5])
            raw += 5
        else:
            print("\nPlease enter 'y' OR 'n'")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
