import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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
    while True:
        city = input("please enter the city you want filter").lower()
        if city not in CITY_DATA:
            print("Sorry,please try again")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("please select month would you like to filter").lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'jule', 'august', 'septemper',
                         'october', 'november', 'december', 'all']:
            print("Sorry,please try again")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("please enter the day you want to filter").lower()
        if day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']:
            print("Sorry,please try again")

    print('-' * 40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_com_m = df['month'].mode()[0]
    print("most common month:", most_com_m)

    # TO DO: display the most common day of week
    most_com_d = df['day_of_week'].mode()[0]
    print("most common day of week is :", most_com_d)

    # TO DO: display the most common start hour
    most_com_SH = df['hour'].mode()[0]
    print("most common start hour:", most_com_SH)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_st = df['Start station'].value_counts().idxmax()
    print("\nmost commonly used start station:", Start_st)

    # TO DO: display most commonly used end station
    End_st = df['End station'].value_counts().idxmax()
    print("\nmost commonly used end ststion:", End_st)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_st = df.groupby(['Start station', 'End station']).count()
    print("\nmost commonly used combination of start station and end station trip:", Start_st, "and", End_st)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tv_t = df['Trip Duration'].sum()
    print("the total travel time is:", total_tv_t, "sec")

    # TO DO: display mean travel time
    mean_tv_t = df['Trip Duration'].mean()
    print("mean travel time is :", mean_tv_t, "sec")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_t = df['User Type'].value_counts()
    print("user type:\n", User_t)

    # TO DO: Display counts of gender
    try:
        gender_type = df['Gender'].value_counts()
        print("\n gender types:", gender_type)
    except KeyError:
        print("No data available for this month")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earlest_y = df['Birth Year'].min()
        print("\n earlest year :", earlest_y)
    except KeyError:
        print("\n No data available for this month")

    try:
        most_recent_y = df['Birth Year'].max()
        print("\n most recent year:", most_recent_y)
    except KeyError:
        print("No data avaliable for this month")

    try:
        most_com_y = df['Birth Year'].value_counts().idxmax()
        print("\nmost common year:", most_com_y)
    except KeyError:
        print("No data available for this month")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    # Ask user if they want to view 5 row of data


def show_row(df):
    row_data = 0
    while True:
        view_row = input("you want see row data? please enter yes or no")
        if view_row == "yes":
            row_data += 5
        elif view_row == "no":
            break
        else:
            print("Try again , Good bye")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_row(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
